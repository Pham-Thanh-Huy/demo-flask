import logging
from mailbox import Message
from typing import Dict

from werkzeug.exceptions import UnsupportedMediaType

from library.database import db
from flask import Request
from marshmallow import ValidationError

from dtos.validation.student_schema import StudentSchema
from models.student import Student
from dtos.base_response import BaseResponse
from dtos.student_dto import StudentDTO
import json

from utils.constant import ConstantUtil


class StudentService:
    @staticmethod
    def get_all_student() -> dict:
        try:
            students = Student.query.all()
            if not students:
                return BaseResponse.success(None, ConstantUtil.STUDENTS_NOT_EXISTS)
            students_dto = [StudentDTO.from_model(student).to_dict() for student in students]
            return BaseResponse.success(students_dto)
        except Exception as e:
            logging.error(f"[ERROR-TO-GET-STUDENT] {e}")
            return BaseResponse.internal_server_error(None, str(e))

    @staticmethod
    def get_by_id(student_id: int) -> dict:
        try:
            student = Student.query.filter(Student.id == student_id).first()
            if not student:
                return BaseResponse.not_found(None, f"Không tìm thấy học sinh với id là {student_id}")

            student_dto = StudentDTO.from_model(student).to_dict()
            return BaseResponse.success(student_dto)
        except Exception as e:
            logging.error(f"[ERROR-TO-GET-STUDENT-BY-ID {e}]")
            return BaseResponse.internal_server_error(None, str(e))


    @staticmethod
    def add_student(request : Request):
      try:
          data = request.get_json()
          if not data:
              return BaseResponse.bad_request(None, ConstantUtil.DATA_CANNOT_EMPTY)

          try:
              schema = StudentSchema()
              schema.load(data)
          except ValidationError as validate:
              return BaseResponse.bad_request(None, validate.messages)

          new_student = Student(
              name=data["name"],
              birth_date=data["birth_date"],
              gender=data["gender"],
              class_name=data["class_name"]
          )

          # save in database
          db.session.add(new_student)
          db.session.commit()

          # Chuyển đối tượng Student thành DTO và trả về response
          student_dto = StudentDTO.from_model(new_student)  # new_student là đối tượng Student
          return BaseResponse.success(student_dto.to_dict(), "Add student success")
      except UnsupportedMediaType as e:
          return BaseResponse.bad_request(None, "I do not support this mediatype please use application/json")
      except Exception as e:
          logging.error(f"[ERROR-TO-ADD-STUDENT {e}")
          return BaseResponse.internal_server_error(None, str(e))