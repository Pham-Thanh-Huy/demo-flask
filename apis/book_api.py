from flask import Blueprint

book_bp = Blueprint('books', __name__)

@book_bp.route("/hello")
def hello():
    return "Hello World!"