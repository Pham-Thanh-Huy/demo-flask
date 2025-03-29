from flask import Blueprint, request, jsonify

from services.book_service import BookService

book_bp = Blueprint('books', __name__)

@book_bp.route('/add-book', methods=['POST'])
def add_book():
    response = BookService.add_book(request)
    return jsonify(response), response['status_code']

@book_bp.route('/get-all', methods=['GET'])
def get_all():
    response = BookService.get_all_books()
    return jsonify(response), response['status_code']