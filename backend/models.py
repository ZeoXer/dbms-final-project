from main import db


class Department(db.Model):
    __tablename__ = "Department"
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(80), nullable=False)
    name_zh = db.Column(db.String(80), nullable=False)
    teachers = db.relationship("Teacher", backref="department", lazy=True)

    def __repr__(self):
        return f'<Department {self.name}>'


class Teacher(db.Model):
    __tablename__ = "Teacher"
    department_id = db.Column(db.Integer, db.ForeignKey("Department.id"), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    name_zh = db.Column(db.String(80), nullable=False)
    name_en = db.Column(db.String(80), nullable=True)
    title = db.Column(db.String(80), nullable=True)
    year_to_school = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Teacher {self.name}>'
        

class Resume(db.Model):
    __tablename__ = "resume"
    teacher_id = db.Column(db.Integer, db.ForeignKey("Teacher.id"), primary_key=True)
    resume_year = db.Column(db.Integer, primary_key=True)
    highest_edu_degree = db.Column(db.String(10), nullable=False)
    highest_edu_department = db.Column(db.String(500), nullable=True)
    highest_edu_school = db.Column(db.String(45), nullable=True)
    highest_edu_graduation_year = db.Column(db.String(4), nullable=False)
    experience = db.Column(db.String(4000), nullable=False)
    teaching_interests = db.Column(db.String(600), nullable=False)
    research_interests = db.Column(db.String(500), nullable=False)
    discipline = db.Column(db.String(500), nullable=True)
    ADM = db.Column(db.Boolean, nullable=False)
    ED = db.Column(db.Boolean, nullable=False)
    SER = db.Column(db.Boolean, nullable=False)
    PA1_1_IP1_1 = db.Column("PA1-1&IP1-1", db.Boolean, nullable=False)
    PA1_2 = db.Column("PA1-2", db.Boolean, nullable=False)
    PA1_3 = db.Column("PA1-3",db.Boolean, nullable=False)
    PA1_4 = db.Column("PA1-4",db.Boolean, nullable=False)
    PA1_5 = db.Column("PA1-5",db.Boolean, nullable=False)
    PA1_6 = db.Column("PA1-6",db.Boolean, nullable=False)
    PA1_7_IP1_3 = db.Column("PA1-7&IP1-3",db.Boolean, nullable=False)
    PA1_8_SP1_3 = db.Column("PA1-8&SP1-3",db.Boolean, nullable=False)
    SP1_1 = db.Column("SP1-1",db.Boolean, nullable=False)
    SP1_2 = db.Column("SP1-2",db.Boolean, nullable=False)
    IP1a = db.Column("IP1a",db.Boolean, nullable=False)
    IP1_2 = db.Column("IP1-2",db.Boolean, nullable=False)
    IP1_4 = db.Column("IP1-4",db.Boolean, nullable=False)
    IP1_5 = db.Column("IP1-5",db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Resume {self.teacher_id} - {self.resume_year}>'
    

class List(db.Model):
    __tablename__ = "List"
    teacher_id = db.Column(db.Integer, db.ForeignKey("Teacher.id"), primary_key=True)
    item_name = db.Column(db.String(600), nullable=False)
    item_year = db.Column(db.Integer, nullable=False)
    journal = db.Column(db.String(1000), nullable=True)
    journal_type = db.Column(db.String(1), nullable=True)
    co_worker_in = db.Column(db.String(500), nullable=True)
    co_worker_out = db.Column(db.String(500), nullable=True)
    scholarship_type = db.Column(db.String(50), nullable=True)
    equis = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<List {self.item_name}>'

    



    
