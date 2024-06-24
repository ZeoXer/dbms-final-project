import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def register_blueprints(app):
    from api import api
    from teacherView import teacherView
    from departmentView import departmentView
    app.register_blueprint(api)
    app.register_blueprint(teacherView, url_prefix='/teacherView')
    app.register_blueprint(departmentView, url_prefix='/departmentView')
