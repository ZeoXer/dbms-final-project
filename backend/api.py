from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from models import Department, Teacher, List, FacultyType, Class, Resume
from __init__ import db
from sqlalchemy.sql import text
from sqlalchemy import and_, func

api = Blueprint('api', __name__)

@api.route('/')
def login():
    return render_template('login.html')

@api.route('/teacher/<int:teacher_id>', methods=['GET'])
def get_teacher_info(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return jsonify({
        'teacher_id': teacher.teacher_id,
        'name_zh': teacher.Cname,
        'name_en': teacher.Ename,
        'title': teacher.job_title,
        'year_to_school': teacher.year,
        'department_id': teacher.dep_id
    })

@api.route('/teacher', methods=['GET'])
def get_teacher():
    teacher_id = request.args.get('teacher_id', '').strip()
    print(f"接收到的 teacher_id: {teacher_id}")
    if not teacher_id:
        print(f"教師: {teacher_id}")
        return jsonify({"error": "教師編號缺失"}), 400
    
    try:
        teacher_id = int(teacher_id)
    except ValueError:
        return jsonify({"error": "教師編號無效"}), 400

    teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
    if not teacher:
        return jsonify({"error": "教師未找到"}), 404

    return jsonify({
        'teacher_id': teacher.teacher_id,
        'name_zh': teacher.Cname,
        'name_en': teacher.Ename,
        'title': teacher.job_title,
        'year_to_school': teacher.year,
        'department_id': teacher.dep_id
    })

@api.route('/resume.html')
def resume():
    teacher_id = request.args.get('teacher_id', '').strip()
    
    if not teacher_id:
        return "教師編號缺失", 400
    
    try:
        teacher_id = int(teacher_id)
    except ValueError:
        return "教師編號無效", 400

    teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
    if not teacher:
        return "教師未找到", 404

    return render_template('resume.html', teacher=teacher)

@api.route('/contribute_list.html')
def contribute_list():
    return render_template('contribute_list.html')

@api.route('/get_department.html')
def get_department():
    return render_template('get_department.html')

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
            'id': department.department_id,
            'name_en': department.department_Ename,
            'name_zh': department.department_Cname,
        })
    return jsonify(department_list), 200

@api.route('/teachers/<int:department_id>', methods=['GET'])
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
    teachers = Teacher.query.filter_by(dep_id=department_id).all()
    teacher_list = []
    for teacher in teachers:
        teacher_list.append({
            'id': teacher.teacher_id,
            'name_zh': teacher.Cname,
            'name_en': teacher.Ename,
            "title": teacher.job_title,
            "year_to_school": teacher.year
        })
    return jsonify(teacher_list), 200

@api.route('/list/<int:department_id>', methods=['GET'])
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
                "journal_name": item.journal,
                "journal_type": item.journal_type,
                "co_worker_in": item.co_worker_in,
                "co_worker_out": item.co_worker_out,
                "scholarship_type": item.scholarship_type,
                "equis": item.equis
            } for item in list]
        })

    return jsonify(result), 200

@api.route('/class/<int:department_id>/<int:year>/<int:semester>',
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
                     Class.degree, func.sum(Class.num_class)).group_by(
                         Class.degree).all()
        print(class_numbers)
        total_class_numbers = {
            degree: sum(num for _, num in class_numbers if _ == degree) or "0"
            for degree in degree_list
        }
        return total_class_numbers

    def get_faculty_type(teacher_id):
        faculty_type = FacultyType.query.filter(
            and_(teacher_id == teacher_id, year == year,
                 semester == semester)).with_entities(
                     FacultyType.teacher_type).first()
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

@api.route('/resume/<int:department_id>', methods=['GET'])
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
    department = Department.query.filter_by(department_id=department_id).first().department_Cname
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


@api.route('/intellectual_contributions.html', methods=['GET'])
def generate_intellectual_contributions():
    queries = [
        """
        DROP VIEW IF EXISTS all_list, all_list_with_aacsb, teacher_list, all_class, all_class_with_contri;
        """,
        """
        CREATE VIEW all_list AS
        SELECT 
            T.teacher_id,
            T.dep_id,
            scholarship_type, 
            equis,
            CASE 
                WHEN T.teacher_id IN (
                    SELECT teacher_id 
                    FROM facultytype 
                    WHERE (year = 112 AND semester = 1 AND teacher_type = '專任') 
                      AND teacher_id IN (
                        SELECT teacher_id 
                        FROM facultytype 
                        WHERE year = 112 AND semester = 2 AND teacher_type = '專任'
                      )
                ) THEN 1
                ELSE 0
            END AS full_time
        FROM teacher AS T, list AS L
        WHERE T.teacher_id = L.teacher_id AND (item_year BETWEEN 2019 AND 2024);
        """,
        """
        CREATE VIEW all_list_with_aacsb AS
        SELECT 
            *,
            CASE 
                WHEN equis = 'E1:Academic Research Articles' THEN 'A1:Peer-Reviewed Journals Articles'
                WHEN equis = 'E2:Practices-oriented Articles' THEN 'A1:Peer-Reviewed Journals Articles'
                WHEN equis = "E3:Studies and Reports commissioned by companies and gov't agencies(企業、政府、科技部產學合作計畫)" THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
                WHEN equis = 'E4:Papers in Academic conferences' THEN 'A1:Peer-Reviewed Journals Articles'
                WHEN equis = 'E5:Papers in Professional conferences' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
                WHEN equis = 'E6:Published Case Studies' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
                WHEN equis = 'E7:Books (e.g. research monographs)' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
                WHEN equis = 'E8:Chapters in books' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
                WHEN equis = 'E9:Textbooks' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
                WHEN equis = 'E10:Chapters in textbooks' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
                WHEN equis = 'E11:Articles on Pedagogic Development and Innovation' THEN 'A3:All other intellectual contributions'
                WHEN equis = "E12:Studies and Reports produced as part of an int'l network" THEN 'A3:All other intellectual contributions'
                WHEN equis = 'E13:Published Teaching Materials' THEN 'A3:All other intellectual contributions'
                WHEN equis = 'E14:Doctoral theses completed-supervised by core faculty' THEN 'A3:All other intellectual contributions'
                WHEN equis = 'E15:Other(Competitive Research Awards Received)獲重要研究獎項次數' THEN 'A2:Additional peer- or editorial-reviewed intellectual contributions'
                WHEN equis = 'E15:Other(Please describe)其他(科技部學術型計畫 MOST Research Project)' THEN 'A3:All other intellectual contributions'
                ELSE NULL
            END AS aacsb
        FROM all_list;
        """,
        """
        CREATE VIEW teacher_list AS
        SELECT 
            teacher_id,
            dep_id,
            SUM(CASE WHEN scholarship_type = 'Basic_or_Discovery_Scholarship' THEN 1 ELSE 0 END) AS Basic_or_Discovery_Scholarship,
            SUM(CASE WHEN scholarship_type = 'Applied_or_Integration_Application_Scholarship' THEN 1 ELSE 0 END) AS Applied_or_Integration_Application_Scholarship,
            SUM(CASE WHEN scholarship_type = 'Teaching_and_Learning_Scholarship' THEN 1 ELSE 0 END) AS Teaching_and_Learning_Scholarship,
            SUM(CASE WHEN scholarship_type = 'Basic_or_Discovery_Scholarship' THEN 1 ELSE 0 END) +
            SUM(CASE WHEN scholarship_type = 'Applied_or_Integration_Application_Scholarship' THEN 1 ELSE 0 END) +
            SUM(CASE WHEN scholarship_type = 'Teaching_and_Learning_Scholarship' THEN 1 ELSE 0 END) AS BAT_Total,
            SUM(CASE WHEN aacsb = 'A1:Peer-Reviewed Journals Articles' THEN 1 ELSE 0 END) AS `Peer-Reviewed Journals Articles`,
            SUM(CASE WHEN aacsb = 'A2:Additional peer- or editorial-reviewed intellectual contributions' THEN 1 ELSE 0 END) AS `Additional peer-or-editorial-reviewed intellectual contributions`,
            SUM(CASE WHEN aacsb = 'A3:All other intellectual contributions' THEN 1 ELSE 0 END) AS `All other intellectual contributions`,
            SUM(CASE WHEN aacsb = 'A1:Peer-Reviewed Journals Articles' THEN 1 ELSE 0 END) +
            SUM(CASE WHEN aacsb = 'A2:Additional peer- or editorial-reviewed intellectual contributions' THEN 1 ELSE 0 END) +
            SUM(CASE WHEN aacsb = 'A3:All other intellectual contributions' THEN 1 ELSE 0 END) AS PAA_Total,
            full_time
        FROM all_list_with_aacsb
        WHERE dep_id != 300
        GROUP BY teacher_id, dep_id
        ORDER BY dep_id, teacher_id;
        """,
        """
        CREATE VIEW all_class AS
        SELECT 
            T.teacher_id,
            T.dep_id,
            SUM(CASE WHEN C.year=112 AND C.semester=1 THEN C.num_class ELSE 0 END) AS s1_num_class,
            SUM(CASE WHEN C.year=112 AND C.semester=2 THEN C.num_class ELSE 0 END) AS s2_num_class,
            CASE 
                WHEN T.teacher_id IN (
                    SELECT teacher_id 
                    FROM facultytype 
                    WHERE (year = 112 AND semester = 1 AND teacher_type = '專任') 
                ) THEN 1*0.5
                ELSE 0.05*0.5
            END AS s1_type,
            CASE 
                WHEN T.teacher_id IN (
                    SELECT teacher_id 
                    FROM facultytype 
                    WHERE (year = 112 AND semester = 2 AND teacher_type = '專任') 
                ) THEN 1*0.5
                ELSE 0.05*0.5
            END AS s2_type
        FROM teacher AS T, class AS C
        WHERE T.teacher_id = C.teacher_id AND T.dep_id != 300
        GROUP BY T.teacher_id, T.dep_id;
        """,
        """
        CREATE VIEW all_class_with_contri AS
        SELECT 
            *,
            (CASE WHEN s1_type = 0.5 THEN s1_type ELSE s1_type * s1_num_class END) +
            (CASE WHEN s2_type = 0.5 THEN s2_type ELSE s2_type * s2_num_class END) AS contri
        FROM all_class
        ORDER BY dep_id, teacher_id;
        """,
        """
        SELECT 
            department_Ename, 
            SUM(Basic_or_Discovery_Scholarship) AS Basic_or_Discovery_Scholarship,
            SUM(Applied_or_Integration_Application_Scholarship) AS Applied_or_Integration_Application_Scholarship,
            SUM(Teaching_and_Learning_Scholarship) AS Teaching_and_Learning_Scholarship,
            SUM(BAT_Total) AS BAT_Total,
            SUM(`Peer-Reviewed Journals Articles`) AS `Peer-Reviewed Journals Articles`,
            SUM(`Additional peer-or-editorial-reviewed intellectual contributions`) AS `Additional peer-or-editorial-reviewed intellectual contributions`,
            SUM(`All other intellectual contributions`) AS `All other intellectual contributions`,
            SUM(PAA_Total) AS PAA_Total,
            ROUND(SUM(CASE WHEN full_time = 1 THEN 1 ELSE 0 END) / SUM(CASE WHEN full_time >=0 THEN 1 ELSE 0 END), 4) AS `Percent of Participating Faculty Producing ICs`,
            ROUND(SUM(contri * BAT_Total) / SUM(BAT_Total), 4) AS `Percentage of Total Full Time Equivalent (FTE) Faculty Producing ICs`
        FROM 
            (teacher_list
            JOIN (
                SELECT teacher_id AS t_id, dep_id AS d_id, contri
                FROM all_class_with_contri
            ) AS teacher_class
            ON teacher_list.teacher_id = teacher_class.t_id AND teacher_list.dep_id = teacher_class.d_id),
            department AS D
        WHERE dep_id = D.department_id
        GROUP BY department_Ename
        ORDER BY department_Ename;
        """
    ]

    with db.engine.connect() as conn:
        for query in queries[:-1]:
            conn.execute(text(query))

        result = conn.execute(text(queries[-1]))
        data = result.fetchall()

    data_list = [
        {
            'department_Ename': row[0],
            'Basic_or_Discovery_Scholarship': row[1],
            'Applied_or_Integration_Application_Scholarship': row[2],
            'Teaching_and_Learning_Scholarship': row[3],
            'BAT_Total': row[4],
            'Peer_Reviewed_Journals_Articles': row[5],
            'Additional_peer_or_editorial_reviewed_intellectual_contributions': row[6],
            'All_other_intellectual_contributions': row[7],
            'PAA_Total': row[8],
            'Percent_of_Participating_Faculty_Producing_ICs': row[9],
            'Percentage_of_Total_Full_Time_Equivalent_FTE_Faculty_Producing_ICs': row[10],
        } for row in data
    ]

    return render_template('intellectual_contributions.html', data=data_list)


# @api.route('/test', methods=['GET'])
# def test_teacher():
#     teacher_id = 101388  # 指定 teacher_id 為 101388
#     teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
    
#     if not teacher:
#         return jsonify({"error": "教師未找到"}), 404

#     teacher_data = {
#         'teacher_id': teacher.teacher_id,
#         'name_zh': teacher.Cname,
#         'name_en': teacher.Ename,
#         'title': teacher.job_title,
#         'year_to_school': teacher.year,
#         'department_id': teacher.dep_id
#     }

#     print(f"找到教師: {teacher}")  
#     print(f"教師詳細資料: {teacher.__dict__}")  

#     return jsonify(teacher_data)

# @api.route('/all_teachers', methods=['GET'])
# def get_all_teachers():
#     teachers = Teacher.query.all()
#     teachers_list = []
#     for teacher in teachers:
#         teachers_list.append({
#             'teacher_id': teacher.teacher_id,
#             'name_zh': teacher.Cname,
#             'name_en': teacher.Ename,
#             'title': teacher.job_title,
#             'year_to_school': teacher.year,
#             'department_id': teacher.dep_id
#         })
#         print(f"教師詳細資料: {teacher.__dict__}")

#     return jsonify(teachers_list)

@api.route('/<int:teacher_id>')
def teacher_main(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    html_content = f'{teacher.Cname}, {teacher.teacher_id}'
    html_content += f' <li><a href="{url_for("api.teacher_basic_info", teacher_id=teacher_id)}">1基本資料</a></li>'
    html_content += f' <li><a href="{url_for("api.teacher_contribution", teacher_id=teacher_id)}">2學術</a></li>'
    return html_content


@api.route('/teacher/<int:teacher_id>/basic_info', methods=['POST'])
def teacher_basic_info(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    resume = Resume.query.filter_by(teacher_id=teacher.teacher_id).first()

    data = request.json
    teacher.Cname = data.get('chinese-name')
    teacher.Ename = data.get('english-name')
    teacher.job_title = data.get('title')
    teacher.year = data.get('join-year')
    teacher.dep_id = data.get('department')

    resume.highest_edu_degree = data.get('highest-degree')
    resume.highest_edu_department = data.get('degree-department')
    resume.highest_edu_school = data.get('degree-school')
    resume.highest_edu_graduation_year = data.get('degree-year')
    resume.experience = data.get('experience')
    resume.teaching_interests = data.get('teaching-interests')
    resume.research_interests = data.get('research-interests')
    resume.discipline = data.get('discipline')

    # Convert string '0'/'1' to boolean
    resume.ADM = data.get('admin-position') == "1"
    resume.ED = data.get('executive-class') == "1"
    resume.SER = data.get('other-services') == "1"
    resume.PA1_1_IP1_1 = data.get('secondment') == "1"
    resume.PA1_2 = data.get('industry-interaction') == "1"
    resume.PA1_3 = data.get('industry-participation') == "1"
    resume.PA1_4 = data.get('association-position') == "1"
    resume.PA1_5 = data.get('association-activity') == "1"
    resume.PA1_6 = data.get('long-term-consulting') == "1"
    resume.PA1_7_IP1_3 = data.get('board-position') == "1"
    resume.PA1_8_SP1_3 = data.get('business-education') == "1"
    resume.SP1_1 = data.get('academic-industry-activity') == "1"
    resume.SP1_2 = data.get('industry-position') == "1"
    resume.IP1a = data.get('full-part-time-industry') == "1"
    resume.IP1_2 = data.get('business-owner') == "1"
    resume.IP1_4 = data.get('active-in-industry') == "1"
    resume.IP1_5 = data.get('professional-certification') == "1"

    db.session.commit()
    print(resume.__dict__)
    return jsonify({"message": "更新成功"}), 200

@api.route('/teacher/<int:teacher_id>/contribution', methods=['GET', 'POST', 'DELETE'])
def teacher_contribution(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    lists = List.query.filter_by(teacher_id=teacher.teacher_id).all()

    if request.method == 'POST':
        data = request.json
        if data:
            for item_data in data:
                new_list_item = List(
                    teacher_id=teacher.teacher_id,
                    item_name=item_data.get('item_name'),
                    item_year=item_data.get('item_year'),
                    journal=item_data.get('journal'),
                    journal_type=item_data.get('journal_type'),
                    co_worker_in=item_data.get('co_worker_in'),
                    co_worker_out=item_data.get('co_worker_out'),
                    scholarship_type=item_data.get('scholarship_type'),
                    equis=item_data.get('equis')
                )
                db.session.add(new_list_item)
        db.session.commit()
        return jsonify({"message": "資料已成功送出"}), 200

    elif request.method == 'DELETE':
        data = request.json
        if data:
            for item_data in data:
                list_item = List.query.filter_by(
                    teacher_id=teacher.teacher_id,
                    item_name=item_data.get('item_name'),
                    item_year=item_data.get('item_year')
                ).first()
                if list_item:
                    db.session.delete(list_item)
        db.session.commit()
        return jsonify({"message": "資料已成功刪除"}), 200

    elif request.method == 'GET':
        contribution_list = []
        for item in lists:
            contribution_list.append({
                'id': teacher.teacher_id,
                'item_name': item.item_name,
                'item_year': item.item_year,
                'journal': item.journal,
                'journal_type': item.journal_type,
                'co_worker_in': item.co_worker_in,
                'co_worker_out': item.co_worker_out,
                'scholarship_type': item.scholarship_type,
                'equis': item.equis
            })
        return jsonify(contribution_list), 200

# @api.route('/<int:teacher_id>/basic_info', methods=['GET', 'POST'])
# def teacher_basic_info(teacher_id):
#     teacher = Teacher.query.get_or_404(teacher_id)
#     resume = Resume.query.filter_by(teacher_id=teacher.teacher_id).first()

#     if request.method == 'POST':
#         teacher.name_zh = request.form.get('name_zh')
#         teacher.name_en = request.form.get('name_en')
#         teacher.title = request.form.get('title')
#         teacher.year_to_school = request.form.get('year_to_school')
#         teacher.department_id = request.form.get('department_id')
        
#         resume.highest_edu_degree = request.form.get('highest_edu_degree')
#         resume.highest_edu_department = request.form.get('highest_edu_department')
#         resume.highest_edu_school = request.form.get('highest_edu_school')
#         resume.highest_edu_graduation_year = request.form.get('highest_edu_graduation_year')
#         resume.experience = request.form.get('experience')
#         resume.teaching_interests = request.form.get('teaching_interests')
#         resume.research_interests = request.form.get('research_interests')
#         resume.discipline = request.form.get('discipline')
#         resume.ADM = request.form.get('ADM', False)
#         resume.ED = request.form.get('ED', False)
#         resume.SER = request.form.get('SER', False)
#         resume.PA1_1_IP1_1 = request.form.get('PA1_1_IP1_1', False)
#         resume.PA1_2 = request.form.get('PA1_2', False)
#         resume.PA1_3 = request.form.get('PA1_3', False)
#         resume.PA1_4 = request.form.get('PA1_4', False)
#         resume.PA1_5 = request.form.get('PA1_5', False)
#         resume.PA1_6 = request.form.get('PA1_6', False)
#         resume.PA1_7_IP1_3 = request.form.get('PA1_7_IP1_3', False)
#         resume.PA1_8_SP1_3 = request.form.get('PA1_8_SP1_3', False)
#         resume.SP1_1 = request.form.get('SP1_1', False)
#         resume.SP1_2 = request.form.get('SP1_2', False)
#         resume.IP1a = request.form.get('IP1a', False)
#         resume.IP1_4 = request.form.get('IP1_4', False)
#         resume.IP1_5 = request.form.get('IP1_5', False)

#         db.session.commit()
#         print("更新成功")
#         return redirect(url_for('api.teacher_basic_info', teacher_id=teacher_id))
    
#     if request.method == 'GET':
#         teacher_info = {
#             'id': teacher.teacher_id,
#             'name_zh': teacher.Cname,
#             'name_en': teacher.Ename,
#             'title': teacher.job_title,
#             'year_to_school': teacher.year,
#             'department_id': teacher.dep_id,
#             'highest_edu_degree': resume.highest_edu_degree,
#             'highest_edu_department': resume.highest_edu_department,
#             'highest_edu_school': resume.highest_edu_school,
#             'highest_edu_graduation_year': resume.highest_edu_graduation_year,
#             'experience': resume.experience,
#             'teaching_interests': resume.teaching_interests,
#             'research_interests': resume.research_interests,
#             'discipline': resume.discipline,
#             'ADM': resume.ADM,
#             'ED': resume.ED,
#             'SER': resume.SER,
#             'PA1_1_IP1_1': resume.PA1_1_IP1_1,
#             'PA1_2': resume.PA1_2,
#             'PA1_3': resume.PA1_3,
#             'PA1_4': resume.PA1_4,
#             'PA1_5': resume.PA1_5,
#             'PA1_6': resume.PA1_6,
#             'PA1_7_IP1_3': resume.PA1_7_IP1_3,
#             'PA1_8_SP1_3': resume.PA1_8_SP1_3,
#             'SP1_1': resume.SP1_1,
#             'SP1_2': resume.SP1_2,
#             'IP1a': resume.IP1a,
#             'IP1_4': resume.IP1_4,
#             'IP1_5': resume.IP1_5
#         }

#         return jsonify(teacher_info), 200

# @api.route('/<int:teacher_id>/contribution', methods=['GET', 'POST'])
# def teacher_contribution(teacher_id):
#     teacher = Teacher.query.get_or_404(teacher_id)
#     resume = Resume.query.filter_by(teacher_id=teacher.teacher_id).first()
#     lists = List.query.filter_by(teacher_id=teacher.teacher_id).all()

#     if request.method == 'POST':
#         data = request.json
#         if data:
#             for item_data in data:
#                 new_list_item = List(
#                     teacher_id=teacher.teacher_id,
#                     item_name=item_data.get('item_name'),
#                     item_year=item_data.get('item_year'),
#                     journal=item_data.get('journal'),
#                     journal_type=item_data.get('journal_type'),
#                     co_worker_in=item_data.get('co_worker_in'),
#                     co_worker_out=item_data.get('co_worker_out'),
#                     scholarship_type=item_data.get('scholarship_type'),
#                     equis=item_data.get('equis')
#                 )
#                 db.session.add(new_list_item)
#         db.session.commit()

#     if request.method == 'GET':
#         if lists:
#             contribution_list = []
#             for item in lists:
#                 contribution_list.append({
#                     'id': teacher.teacher_id,
#                     'item_name': item.item_name,
#                     'item_year': item.item_year,
#                     'journal': item.journal,
#                     'journal_type': item.journal_type,
#                     'co_worker_in': item.co_worker_in,
#                     'co_worker_out': item.co_worker_out,
#                     'scholarship_type': item.scholarship_type,
#                     'equis': item.equis
#                 })
#         else:
#             print("No items found for the given teacher_id.")

#         return jsonify(contribution_list), 200
    