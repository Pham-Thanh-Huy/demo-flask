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
                return BaseResponse(None, "Không có học sinh nào trong hệ thống!",
                                    200).to_dict()
            students_dto = [StudentDTO.from_model(student).to_dict() for student in students]
            return BaseResponse(students_dto, ConstantUtil.SUCCESS, 200).to_dict()
        except Exception as e:
            logging.error(f"[ERROR-TO-GET-STUDENT] {e}")
            return BaseResponse(None, str(e), 500).to_dict()

    @staticmethod
    def get_by_id(student_id: int) -> dict:
        try:
            student = Student.query.filter(Student.id == student_id).first()
            if not student:
                return BaseResponse(
                    None,
                    f"Không tìm thấy học sinh với id là {student_id}",
                    404
                ).to_dict()

            student_dto = StudentDTO.from_model(student).to_dict()
            return BaseResponse(student_dto, ConstantUtil.SUCCESS, 200).to_dict()
        except Exception as e:
            logging.error(f"[ERROR-TO-GET-STUDENT-BY-ID {e}]")
            return BaseResponse(
                None,
                f"Lỗi: {e}",
                404
            ).to_dict()


    @staticmethod
    def add_student(request : Request):
      try:
          data = request.get_json()
          if not data:
              return BaseResponse(None, ConstantUtil.DATA_CANNOT_EMPTY, 400).to_dict()

          try:
              schema = StudentSchema()
              schema.load(data)
          except ValidationError as validate:
              return BaseResponse(None, validate.messages, 400).to_dict()

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
          return BaseResponse(student_dto.to_dict(), "Thêm học sinh thành công", 201).to_dict()
      except UnsupportedMediaType as e:
          return BaseResponse(None, "I do not support this mediatype please use application/json", 400).to_dict()
      except Exception as e:
          logging.error(f"[ERROR-TO-ADD-STUDENT {e}")
          return BaseResponse(None, str(e), 500).to_dict()