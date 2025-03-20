from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    return app