from sqlalchemy.orm import backref

from library.database import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    page_count = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable = False)

    # Thiết lập relationship với Student
    student = db.relationship('Student', backref=backref('books', lazy='dynamic'))

    def __init__(self, name, page_count, author_id, category_id, student_id):
        self.name = name
        self.page_count = page_count
        self.author_id = author_id
        self.category_id = category_id
        self.student_id = student_id
