from flask import Blueprint, jsonify
from services.student_service import  StudentService
student_bp = Blueprint('students', __name__)

@student_bp.route("/get-all", methods=['GET'])
def get_students():
    student_service = StudentService()
    response = student_service.get_all_student()
    return jsonify(response), response['status_code']