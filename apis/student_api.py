from flask import Blueprint, jsonify, request
from services.student_service import  StudentService
student_bp = Blueprint('students', __name__)

@student_bp.route("/get-all", methods=['GET'])
def get_students():
    response = StudentService.get_all_student()
    return jsonify(response), response['status_code']

@student_bp.route("/get-by-id/<int:student_id>", methods = ['GET'])
def get_student_by_id(student_id : int):
    response = StudentService.get_by_id(student_id)
    return jsonify(response), response['status_code']

@student_bp.route("/add", methods = ['POST'])
def add_student():
    response = StudentService.add_student(request)
    return jsonify(response), response['status_code']