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
