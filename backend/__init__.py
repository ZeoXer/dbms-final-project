import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
swagger_config = {
    "headers": [],
    "specs": [{
        "endpoint": "apispec_1",
        "route": "/apispec_1.json",
        "rule_filter": lambda rule: True,
        "model_filter": lambda tag: True,
    }],
    "static_url_path":
    "/flasgger_static",
    "swagger_ui":
    True,
    "specs_route":
    "/swagger/",
    "title":
    "教師履歷管理系統 API 文件",
}
swagger = Swagger(app, config=swagger_config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Department, Teacher
from api import api
from teacherView import teacherView

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(teacherView, url_prefix='/teacherView')
