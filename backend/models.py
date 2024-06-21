from main import db


class Department(db.Model):
    __tablename__ = "Department"
    id = db.Column(db.Integer, primary_key=True)
    name_en = db.Column(db.String(80), nullable=False)
    name_zh = db.Column(db.String(80), nullable=False)
    teachers = db.relationship("Teacher", backref="department", lazy=True)

    def __repr__(self):
        return f'<Department {self.name_zh}>'


class Teacher(db.Model):
    __tablename__ = "Teacher"
    id = db.Column(db.Integer, primary_key=True)
    name_zh = db.Column(db.String(80), nullable=False)
    name_en = db.Column(db.String(80), nullable=True)
    title = db.Column(db.String(80), nullable=True)
    year_to_school = db.Column(db.Integer, nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey("Department.id"), nullable=False)

    def __repr__(self):
        return f'<Teacher {self.name_zh}>'


class FacultyType(db.Model):
    __tablename__ = "FacultyType"
    teacher_id = db.Column(db.Integer, db.ForeignKey("Teacher.id"))
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    faculty_type = db.Column(db.String(80))

    __table_args__ = (
        db.PrimaryKeyConstraint('teacher_id', 'year', 'semester'),
    )

    def __repr__(self):
        return f'<FacultyType {self.teacher_id} {self.year}-{self.semester}>'


class Class(db.Model):
    __tablename__ = "Class"
    teacher_id = db.Column(db.Integer)
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    degree = db.Column(db.String(80))
    class_number = db.Column(db.Integer)
    
    __table_args__ = (
        db.PrimaryKeyConstraint('teacher_id', 'year', 'semester', 'degree'),
        db.ForeignKeyConstraint(['teacher_id', 'year', 'semester'], ['FacultyType.teacher_id', 'FacultyType.year', 'FacultyType.semester'])
    )
    
    def __repr__(self):
        return f'<Class {self.name} {self.year}-{self.semester} {self.degree} {self.class_number}>'
    
    
class PartTime(db.Model):
    __tablename__ = "PartTime"
    teacher_id = db.Column(db.Integer, db.ForeignKey("Teacher.id"))
    pt_company = db.Column(db.String(80))
    pt_department = db.Column(db.String(80))
    pt_position = db.Column(db.String(80))
    pt_start = db.Column(db.String(10))
    pt_end = db.Column(db.String(10))
    
    __table_args__ = (
        db.PrimaryKeyConstraint('teacher_id', 'pt_company', 'pt_department', 'pt_position', 'pt_start', 'pt_end'),
    )
    
    def __repr__(self):
        return f'<PartTime {self.teacher_id} {self.pt_company} {self.pt_department} {self.pt_position} {self.pt_start}-{self.pt_end}>'
    

class List(db.Model):
    __tablename__ = "List"
    teacher_id = db.Column(db.Integer, db.ForeignKey("Teacher.id"))
    item_name= db.Column(db.String(500))
    item_year = db.Column(db.Integer)
    journal = db.Column(db.String(255))
    journal_type = db.Column(db.String(1))
    co_worker_in = db.Column(db.String(255))
    co_worker_out = db.Column(db.String(255))
    scholarship_type = db.Column(db.String(50))
    equis = db.Column(db.String(100))
    
    __table_args__ = (
        db.PrimaryKeyConstraint('teacher_id', 'item_name', 'item_year'),
    )
    
    def __repr__(self):
        return f'<List {self.teacher_id} {self.item_name}>'
    

class Resume(db.Model):
    __tablename__ = "Resume"
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
    
    __table_args__ = (
        db.PrimaryKeyConstraint('teacher_id', 'resume_year'),
    )

    def __repr__(self):
        return f'<Resume {self.teacher_id} - {self.resume_year}>'
