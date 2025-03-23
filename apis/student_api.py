from flask import Blueprint, jsonify

from dtos.base_response import BaseResponse
from dtos.student_dto import StudentDTO
from services.student_service import  StudentService
student_bp = Blueprint('students', __name__)

@student_bp.route("/get-all", methods = ['GET'])
def get_students() -> BaseResponse[list[StudentDTO]]:
    response = StudentService.get_all_student()
    return jsonify(response.to_dict()), response.status_code