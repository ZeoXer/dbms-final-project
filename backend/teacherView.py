from flask import Blueprint, jsonify, request, redirect, url_for
from models import Department, Teacher, List, Resume
from main import db

teacherView = Blueprint('teacherView', __name__)

###test###
@teacherView.route('/test')
def hi():
    return 'test'


###教師介面(temporary)##
@teacherView.route('/<int:teacher_id>')
def teacher_main(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    html_content = f'{teacher.name_zh}, {teacher.id}'
    html_content += f' <li><a href="{url_for("teacherView.teacher_basic_info", teacher_id=teacher_id)}">1基本資料</a></li>'
    html_content += f' <li><a href="{url_for("teacherView.teacher_academic", teacher_id=teacher_id)}">2學術</a></li>'

    return html_content


###1資本資料###
@teacherView.route('/<int:teacher_id>/basic_info', methods=['GET','POST'])
def teacher_basic_info(teacher_id):

    teacher = Teacher.query.get_or_404(teacher_id)
    resume = Resume.query.filter_by(teacher_id=teacher.id).first()

    ### submit 之後 redirection ###
    if request.method == 'POST':        
        
        #get data

        db.session.commit()
        return redirect(url_for('teacher_main', teacher_id=teacher_id))
    
    ### 
    if request.method == 'GET':

        teacher_info = {
        'id': teacher.id,
        'name_zh': teacher.name_zh,
        'name_en': teacher.name_en,
        'title': teacher.title,
        'year_to_school': teacher.year_to_school,
        'department_id': teacher.department_id,
        #學群:?
        'highest_edu_degree': resume.highest_edu_degree,
        'highest_edu_department': resume.highest_edu_department,
        'highest_edu_school': resume.highest_edu_school,
        'highest_edu_graduation_year': resume.highest_edu_graduation_year,
        'experience': resume.experience,
        'teaching_interests': resume.teaching_interests,
        'research_interests': resume.research_interests,
        'discipline': resume.discipline,
        'ADM': resume.ADM,
        'ED': resume.ED,
        'SER': resume.SER,
        'PA1_1_IP1_1': resume.PA1_1_IP1_1,
        'PA1_2': resume.PA1_2,
        'PA1_3': resume.PA1_3,
        'ADM': resume.ADM,
        'PA1_4': resume.PA1_4,
        'PA1_5': resume.PA1_5,
        'PA1_6': resume.PA1_6,
        'PA1_7_IP1_3': resume.PA1_7_IP1_3,
        'PA1_8_SP1_3': resume.PA1_8_SP1_3,
        'SP1_1': resume.SP1_1,
        'SP1_2': resume.SP1_2,
        'IP1a': resume.IP1a,
        'IP1_4': resume.IP1_4,
        'IP1_5': resume.IP1_5,
        #'年份': ?
        }

    return jsonify(teacher_info), 200