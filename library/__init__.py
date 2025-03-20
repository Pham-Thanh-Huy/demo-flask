from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from apis.book_api import books
db = SQLAlchemy()

def create_app(config_file="config.py") -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(books, url_prefix="/books")
    with app.app_context():
        db.create_all()
    return app