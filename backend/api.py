from flask import Blueprint, jsonify
from models import Department, Teacher

api = Blueprint('api', __name__)


@api.route('/health', methods=['GET'])
def health():
    return 'API is up and running!', 200


@api.route('/departments', methods=['GET'])
def get_departments():
    """
    獲取所有系所名單資訊
    ---
    tags: ['Department']
    responses:
      200:
        schema:
            type: array
            items:
                type: object
                properties:
                    id:
                        type: integer
                        description: 系所編號
                    name_en:
                        type: string
                        description: 系所英文名稱
                    name_zh:
                        type: string
                        description: 系所中文名稱
    """
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
    """
    獲取指定系所的所有教師名單資訊
    ---
    tags: ['Department']
    parameters:
        - name: department_id
          in: path
          type: integer
          required: true
          description: 系所編號
    responses:
        200:
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                            description: 教師編號
                        name_en:
                            type: string
                            description: 教師英文名稱
                        name_zh:
                            type: string
                            description: 教師中文名稱
                        title:
                            type: string
                            description: 教師職稱
                        year_to_school:
                            type: integer
                            description: 教師到校年份
    """
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
