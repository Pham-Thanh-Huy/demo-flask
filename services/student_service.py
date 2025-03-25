import logging
from typing import Dict
from models.student import Student
from dtos.base_response import BaseResponse
from dtos.student_dto import StudentDTO

class StudentService:
    @staticmethod
    def get_all_student() -> Dict:
        try:
            students = Student.query.all()
            if not students:
                return BaseResponse(data=[], message="Student empty!", status_code=200).to_dict()

            students_dto = [StudentDTO.from_model(student) for student in students]
            student_dict = [student.to_dict() for student in students_dto]
            return BaseResponse(data=student_dict, message="Success", status_code=200).to_dict()
        except Exception as e:
            logging.error(f"[ERROR-TO-GET-STUDENT] {e}")
            return BaseResponse(data=None, message=str(e), status_code=500).to_dict()