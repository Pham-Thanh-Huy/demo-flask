import logging
from flask import Request
from marshmallow import ValidationError
from werkzeug.exceptions import UnsupportedMediaType

from library.database import db
from models.book import Book
from dtos.base_response import BaseResponse
from dtos.book_dto import BookDTO
from dtos.validation.book_schema import BookSchema
from models.student import Student
from utils.constant import ConstantUtil

class BookService:
    @staticmethod
    def add_book(request: Request) -> dict:
        try:
            data = request.get_json()
            if not data:
                return BaseResponse.bad_request(None, ConstantUtil.DATA_CANNOT_EMPTY)

            try:
                schema = BookSchema()
                schema.load(data)
            except ValidationError as validate:
                return BaseResponse.bad_request(None, validate.messages)

            student = Student.query.get(data["student_id"])
            if not student:
                return BaseResponse.bad_request(None, f"Student with id {data['student_id']} does not exist")

            new_book = Book(
                name=data["name"],
                page_count=data["page_count"],
                author_id=data.get("author_id"),
                student_id=data["student_id"]
            )

            db.session.add(new_book)
            db.session.commit()

            book_dto = BookDTO.from_model(new_book)
            return BaseResponse.success(book_dto.to_dict(), "Add book success")

        except UnsupportedMediaType as e:
            return BaseResponse.bad_request(None, "I do not support this mediatype please use application/json")
        except Exception as e:
            logging.error(f"[ERROR-TO-ADD-BOOK] {e}")
            return BaseResponse.internal_server_error(None, str(e))

    @staticmethod
    def get_all_books() -> dict:
        try:
            books = Book.query.all()
            if not books:
                return BaseResponse.success(None, "No books found")
            books_dto = [BookDTO.from_model(book).to_dict() for book in books]
            return BaseResponse.success(books_dto)
        except Exception as e:
            logging.error(f"[ERROR-TO-GET-BOOKS] {e}")
            return BaseResponse.internal_server_error(None, str(e))

    @staticmethod
    def get_book_by_id(book_id: int) -> dict:
        try:
            book = Book.query.filter(Book.id == book_id).first()
            if not book:
                return BaseResponse.not_found(None, f"Không tìm thấy sách với id là {book_id}")
            book_dto = BookDTO.from_model(book).to_dict()
            return BaseResponse.success(book_dto)
        except Exception as e:
            logging.error(f"[ERROR-TO-GET-BOOK-BY-ID] {e}")
            return BaseResponse.internal_server_error(None, str(e))