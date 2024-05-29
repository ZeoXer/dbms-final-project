from flask import Blueprint, jsonify
from models import Department, Teacher

api = Blueprint('api', __name__)


@api.route('/health', methods=['GET'])
def health():
    return 'API is up and running!', 200


@api.route('/departments', methods=['GET'])
def get_departments():
    departments = Department.query.all()
    department_list = []
    for department in departments:
        department_list.append({
            'id': department.id,
            'name_en': department.name_en,
            'name_zh': department.name_zh,
        })
    return jsonify(department_list), 200


@api.route('/teachers/<int:department_id>', methods=['GET'])
def get_teachers_by_department_id(department_id):
    teachers = Teacher.query.filter_by(department_id=department_id).all()
    teacher_list = []
    for teacher in teachers:
        teacher_list.append({
            'id': teacher.id,
            'name_zh': teacher.name_zh,
            'name_en': teacher.name_en,
            "title": teacher.title,
            "year_to_school": teacher.year_to_school
        })
    return jsonify(teacher_list), 200
