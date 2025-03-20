from flask import Blueprint

books = Blueprint('books', __name__)

@books.route("/hello")
def hello():
    return "Hello World!"