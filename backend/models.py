from main import db


class Department(db.Model):
    __tablename__ = "Department"
    id = db.Column(db.Integer, primary_key=True)
    name_zh = db.Column(db.String(80), nullable=False)
    name_en = db.Column(db.String(80), nullable=False)
    teachers = db.relationship("Teacher", backref="department", lazy=True)

    def __repr__(self):
        return f'<Department {self.name}>'


class Teacher(db.Model):
    __tablename__ = "Teacher"
    id = db.Column(db.Integer, primary_key=True)
    name_zh = db.Column(db.String(80), nullable=False)
    name_en = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    year_to_school = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("Department.id"), nullable=False)

    def __repr__(self):
        return f'<Teacher {self.name}>'
