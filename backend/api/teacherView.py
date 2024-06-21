from flask import Blueprint, jsonify, request, redirect, url_for, render_template
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
    html_content += f' <li><a href="{url_for("teacherView.teacher_contribution", teacher_id=teacher_id)}">2學術</a></li>'

    return html_content


###1資本資料###
@teacherView.route('/<int:teacher_id>/basic_info', methods=['GET','POST'])
def teacher_basic_info(teacher_id):
    print("teacher_basic_info")
    teacher = Teacher.query.get_or_404(teacher_id)
    resume = Resume.query.filter_by(teacher_id=teacher.id).first()

    ### submit 之後 redirection ###
    if request.method == 'POST':
        
        teacher.name_zh = request.form.get('name_zh')
        teacher.name_en = request.form.get('name_en')
        teacher.title = request.form.get('title')
        teacher.year_to_school = request.form.get('year_to_school')
        teacher.department_id = request.form.get('department_id')
        
        resume.highest_edu_degree = request.form.get('highest_edu_degree')
        resume.highest_edu_department = request.form.get('highest_edu_department')
        resume.highest_edu_school = request.form.get('highest_edu_school')
        resume.highest_edu_graduation_year = request.form.get('highest_edu_graduation_year')
        resume.experience = request.form.get('experience')
        resume.teaching_interests = request.form.get('teaching_interests')
        resume.research_interests = request.form.get('research_interests')
        resume.discipline = request.form.get('discipline')
        resume.ADM = request.form.get('ADM')
        resume.ED = request.form.get('ED')
        resume.SER = request.form.get('SER')
        resume.PA1_1_IP1_1 = request.form.get('PA1_1_IP1_1')
        resume.PA1_2 = request.form.get('PA1_2')
        resume.PA1_3 = request.form.get('PA1_3')
        resume.PA1_4 = request.form.get('PA1_4')
        resume.PA1_5 = request.form.get('PA1_5')
        resume.PA1_6 = request.form.get('PA1_6')
        resume.PA1_7_IP1_3 = request.form.get('PA1_7_IP1_3')
        resume.PA1_8_SP1_3 = request.form.get('PA1_8_SP1_3')
        resume.SP1_1 = request.form.get('SP1_1')
        resume.SP1_2 = request.form.get('SP1_2')
        resume.IP1a = request.form.get('IP1a')
        resume.IP1_4 = request.form.get('IP1_4')
        resume.IP1_5 = request.form.get('IP1_5')

        #update data query
        db.session.commit()
        return redirect(url_for('teacher_basic_info', teacher_id=teacher_id))
    
    ### 一進來看到的畫面
    if request.method == 'GET':
        print("get")

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


###2 學術###
@teacherView.route('/<int:teacher_id>/contribution', methods=['GET','POST'])
def teacher_contribution(teacher_id):
    print("teacher_contribution")

    teacher = Teacher.query.get_or_404(teacher_id)
    resume = Resume.query.filter_by(teacher_id=teacher.id).first()
    lists = List.query.filter_by(teacher_id=teacher.id).all()

    #print(lists)

    if request.method == 'POST':

        data = request.json

        if data:
            for item_data in data:
                # 創建一個新的 List 對象來保存到數據庫
                new_list_item = List(
                    teacher_id=teacher.id,
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
        
        # Reflect all changes to the database
        db.session.commit()


        index = 0
   
    if request.method == 'GET':
        print("request GET")

        print(f"Teacher ID: {teacher.id}")  # check teacher_id
        print(f"Lists: {lists}")  # check query

        if list:
            contribution_list = []
            for item in lists:
                #print("    "+item.item_name)
                contribution_list.append({
                    'id': teacher.id,
                    'item_name' : item.item_name,
                    'item_year' : item.item_year,
                    'journal' : item.journal,
                    'journal_type' : item.journal_type,
                    'co_worker_in' : item.co_worker_in,
                    'co_worker_out' : item.co_worker_out,
                    'scholarship_type' : item.scholarship_type,
                    'equis' : item.equis

                })
                
        else:
            print("No items found for the given teacher_id.")


    return jsonify(contribution_list), 200