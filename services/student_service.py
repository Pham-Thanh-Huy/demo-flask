import logging
from models.student import Student
from dtos.base_response import BaseResponse
from dtos.student_dto import StudentDTO

class StudentService:
    @staticmethod
    def get_all_student() -> BaseResponse[list[dict]]:  # Sửa type hint cho rõ ràng
        try:
            students = Student.query.all()
            if not students:
                return BaseResponse(data=[], message="No students found", status_code=200)

            students_dto = [StudentDTO.from_model(student) for student in students]
            students_dict = [student_dto.to_dict() for student_dto in students_dto]
            return BaseResponse(data=students_dict, message="Success", status_code=200)
        except Exception as e:
            logging.error(f"[ERROR-TO-GET-STUDENT] {e}")
            return BaseResponse(data=None, message=str(e), status_code=500)