from flask import Flask
from pymysql import install_as_MySQLdb
from apis.book_api import books
from .database import db
import models

install_as_MySQLdb()

def create_app(config_file="config.py") -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(books, url_prefix="/books")

    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print("Lỗi kết nối CSDL:", e)
    return app
