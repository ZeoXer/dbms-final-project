from flask import Blueprint, jsonify, request
from models import Department, Teacher, List, FacultyType, Class, Resume
from sqlalchemy import and_, func
from __init__ import db

departmentView = Blueprint('departmentView', __name__)


@departmentView.route('/departments', methods=['GET'])
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


@departmentView.route('/teachers/<int:department_id>', methods=['GET'])
def get_teachers(department_id):
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


@departmentView.route('/list/<int:department_id>', methods=['GET'])
def get_department_list(department_id):
    """
    獲取指定系所所有教師的學術、實務和教學貢獻清單
    ---
    tags: ['Department']
    parameters:
        - name: department_id
          in: path
          type: integer
          required: true
          description: 系所編號
        - name: start
          in: query
          type: integer
          required: false
          description: 起始年份
        - name: end
          in: query
          type: integer
          required: false
          description: 結束年份
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
                        name_zh:
                            type: string
                            description: 教師中文名稱
                        list:
                            type: array
                            items:
                                type: object
                                properties:
                                    item_name:
                                        type: string
                                        description: 項目名稱
                                    item_year:
                                        type: integer
                                        description: 項目年份
                                    journal_name:
                                        type: string
                                        description: 期刊名稱
                                    journal_type:
                                        type: string
                                        description: 期刊類型
                                    co_worker_in:
                                        type: string
                                        description: 校內合著者
                                    co_worker_out:
                                        type: string
                                        description: 校外合著者
                                    scholarship_type:
                                        type: string
                                        description: 獎學金類型
                                    equis:
                                        type: string
                                        description: EQUIS 類別
    """
    teachers, _ = get_teachers(department_id)
    start_year = request.args.get('start', type=int, default=0)
    end_year = request.args.get('end', type=int, default=9999)
    result = []

    # 檢查起始年份是否大於結束年份
    if (start_year and end_year) and (start_year > end_year):
        return jsonify({"error": "起始年份需大於結束年份"}), 400

    for teacher in teachers.get_json():
        list = List.query.filter(
            and_(List.teacher_id == teacher["id"], List.item_year
                 >= start_year, List.item_year <= end_year)).all()
        result.append({
            "id":
            teacher["id"],
            "name_zh":
            teacher["name_zh"],
            "list": [{
                "item_name": item.item_name,
                "item_year": item.item_year,
                "journal": item.journal,
                "journal_type": item.journal_type,
                "co_worker_in": item.co_worker_in,
                "co_worker_out": item.co_worker_out,
                "scholarship_type": item.scholarship_type,
                "equis": item.equis
            } for item in list]
        })

    return jsonify(result), 200


@departmentView.route('/class/<int:department_id>/<int:year>/<int:semester>',
                      methods=['GET'])
def get_department_class(department_id, year, semester):
    """
    獲取指定系所所有教師的各班級開課數
    ---
    tags: ['Department']
    parameters:
        - name: department_id
          in: path
          type: integer
          required: true
          description: 系所編號
        - name: year
          in: path
          type: integer
          required: true
          description: 學年度
        - name: semester
          in: path
          type: integer
          required: true
          description: 學期
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
                        name_zh:
                            type: string
                            description: 教師中文名稱
                        faculty_type:
                            type: string
                            description: 教師專兼別
                        class_list:
                            type: array
                            items:
                                type: object
                                properties:
                                    學士班:
                                        type: string
                                        description: 學士班開課數
                                    一般碩士班:
                                        type: string
                                        description: 一般碩士班開課數
                                    博士班:
                                        type: string
                                        description: 博士班開課數
                                    MBA:
                                        type: string
                                        description: MBA開課數
                                    IMBA:
                                        type: string
                                        description: IMBA開課數
                                    EMBA:
                                        type: string
                                        description: EMBA開課數
                                    DBA:
                                        type: string
                                        description: DBA開課數
    """

    def get_class_total_num(teacher_id):
        class_numbers = Class.query.filter(
            and_(Class.teacher_id == teacher_id, Class.year == year,
                 Class.semester == semester)).with_entities(
                     Class.degree, func.sum(Class.class_number)).group_by(
                         Class.degree).all()
        total_class_numbers = {
            degree: sum(num for _, num in class_numbers if _ == degree) or "0"
            for degree in degree_list
        }
        return total_class_numbers

    def get_faculty_type(teacher_id):
        faculty_type = FacultyType.query.filter(
            and_(teacher_id == teacher_id, year == year,
                 semester == semester)).with_entities(
                     FacultyType.faculty_type).first()
        return faculty_type[0] if faculty_type is not None else "無資料"

    teachers, _ = get_teachers(department_id)
    teacher_class_list = []
    degree_list = ['學士班', '一般碩士班', '博士班', 'MBA', 'IMBA', 'EMBA', 'DBA']

    for teacher in teachers.get_json():
        faculty_type = get_faculty_type(teacher["id"])
        class_number = get_class_total_num(teacher["id"])
        teacher_class_list.append({
            "id": teacher["id"],
            "name_zh": teacher["name_zh"],
            "faculty_type": faculty_type,
            "class_number_list": class_number
        })

    return jsonify(teacher_class_list), 200


@departmentView.route('/resume/<int:department_id>', methods=['GET'])
def get_department_resume(department_id):
    """
    獲取指定系所所有教師的履歷清單
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
                        name_zh:
                            type: string
                            description: 教師中文名稱
                        name_en:
                            type: string
                            description: 教師英文名稱
                        title:
                            type: string
                            description: 教師職稱
                        year_to_school:
                            type: integer
                            description: 教師到校年份
                        department:
                            type: string
                            description: 系所名稱
                        resumes:
                            type: array
                            items:
                                type: object
                                properties:
                                    highest_edu_degree:
                                        type: string
                                        description: 最高學歷學位
                                    highest_edu_department:
                                        type: string
                                        description: 最高學歷系所
                                    highest_edu_school:
                                        type: string
                                        description: 最高學歷學校
                                    highest_edu_graduation_year:
                                        type: integer
                                        description: 最高學歷畢業年份
                                    experience:
                                        type: string
                                        description: 經歷
                                    teaching_interests:
                                        type: string
                                        description: 教學興趣
                                    research_interests:
                                        type: string
                                        description: 研究興趣
                                    discipline:
                                        type: string
                                        description: 學術專長
                                    ADM:
                                        type: boolean
                                        description: ADM
                                    ED:
                                        type: boolean
                                        description: ED
                                    SER:
                                        type: boolean
                                        description: SER
                                    PA1_1_IP1_1:
                                        type: boolean
                                        description: PA1-1&IP1-1
                                    PA1_2:
                                        type: boolean
                                        description: PA1-2
                                    PA1_3:
                                        type: boolean
                                        description: PA1-3
                                    PA1_4:
                                        type: boolean
                                        description: PA1-4
                                    PA1_5:
                                        type: boolean
                                        description: PA1-5
                                    PA1_6:
                                        type: boolean
                                        description: PA1-6
                                    PA1_7_IP1_3:
                                        type: boolean
                                        description: PA1-7&IP1-3
                                    PA1_8_SP1_3:
                                        type: boolean
                                        description: PA1-8&SP1-3
                                    SP1_1:
                                        type: boolean
                                        description: SP1-1
                                    SP1_2:
                                        type: boolean
                                        description: SP1-2
                                    IP1a:
                                        type: boolean
                                        description: IP1a
                                    IP1_2:
                                        type: boolean
                                        description: IP1-2
                                    IP1_4:
                                        type: boolean
                                        description: IP1-4
                                    IP1_5:
                                        type: boolean
                                        description: IP1-5
                                    resume_year:
                                        type: integer
                                        description: 履歷年份
    """
    teachers, _ = get_teachers(department_id)
    department = Department.query.filter_by(id=department_id).first().name_zh
    teacher_resume_list = []

    for teacher in teachers.get_json():
        resumes = Resume.query.filter_by(teacher_id=teacher["id"]).all()
        resume_list = []
        for resume in resumes:
            resume_list.append({
                "highest_edu_degree": resume.highest_edu_degree,
                "highest_edu_department": resume.highest_edu_department,
                "highest_edu_school": resume.highest_edu_school,
                "highest_edu_graduation_year":
                resume.highest_edu_graduation_year,
                "experience": resume.experience,
                "teaching_interests": resume.teaching_interests,
                "research_interests": resume.research_interests,
                "discipline": resume.discipline,
                "ADM": resume.ADM,
                "ED": resume.ED,
                "SER": resume.SER,
                "PA1_1_IP1_1": resume.PA1_1_IP1_1,
                "PA1_2": resume.PA1_2,
                "PA1_3": resume.PA1_3,
                "PA1_4": resume.PA1_4,
                "PA1_5": resume.PA1_5,
                "PA1_6": resume.PA1_6,
                "PA1_7_IP1_3": resume.PA1_7_IP1_3,
                "PA1_8_SP1_3": resume.PA1_8_SP1_3,
                "SP1_1": resume.SP1_1,
                "SP1_2": resume.SP1_2,
                "IP1a": resume.IP1a,
                "IP1_2": resume.IP1_2,
                "IP1_4": resume.IP1_4,
                "IP1_5": resume.IP1_5,
                "resume_year": resume.resume_year
            })
        teacher_resume_list.append({
            "id": teacher["id"],
            "name_zh": teacher["name_zh"],
            "name_en": teacher["name_en"],
            "title": teacher["title"],
            "year_to_school": teacher["year_to_school"],
            "department": department,
            "resumes": resume_list
        })

    return jsonify(teacher_resume_list), 200
