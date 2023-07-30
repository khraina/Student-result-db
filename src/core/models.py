from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    students = db.relationship('Student', backref='user', lazy=True)
    teachers = db.relationship('Teacher', backref='user', lazy=True)

    def is_admin(self):
        return self.secret == 'your_secret_key'  # Replace with your admin email


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    reg_no = db.Column(db.String(150))
    name = db.Column(db.String(150))
    batch = db.Column(db.Integer)
    Earned_Credits = db.Column(db.Integer)
    Cumilative_Credits = db.Column(db.Integer)
    SGPA = db.Column(db.Integer)
    CGPA = db.Column(db.Integer)
    result_id = db.Column(db.Integer, db.ForeignKey('results.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))


class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    Sem = db.Column(db.Integer, nullable=False)
    SubCode = db.Column(db.String(10))
    results = db.relationship('Result', backref='subject', lazy=True)


class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(2))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))

class Sem1(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    RegNo = db.Column(db.String(10),nullable=False)
    Name = db.Column(db.String(50),nullable=False)
    PHT100 = db.Column(db.String(10),nullable=False)
    MAT101 = db.Column(db.String(10),nullable=False)
    HUN101 = db.Column(db.String(10),nullable=False)
    EST100 = db.Column(db.String(10),nullable=False)
    EST130 = db.Column(db.String(10),nullable=False)
    PHL120= db.Column(db.String(10),nullable=False)
    ESL130 = db.Column(db.String(10),nullable=False)
    Earned_Credits = db.Column(db.Integer,nullable=False)
    Cumilative_Credits = db.Column(db.Integer,nullable=False)
    SGPA = db.Column(db.Integer,nullable=False)
    CGPA = db.Column(db.Integer,nullable=False)

class Sem2(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    RegNo = db.Column(db.String(10),nullable=False)
    Name = db.Column(db.String(50),nullable=False)
    EST120 = db.Column(db.String(10),nullable=False)
    CYT100 = db.Column(db.String(10),nullable=False)
    EST110 = db.Column(db.String(10),nullable=False)
    MAT102 = db.Column(db.String(10),nullable=False)
    EST102 = db.Column(db.String(10),nullable=False)
    HUN102 = db.Column(db.String(10),nullable=False)
    CYL120 = db.Column(db.String(10),nullable=False)
    ESL120 = db.Column(db.String(10),nullable=False)
    EST102 = db.Column(db.String(10),nullable=False)
    Earned_Credits = db.Column(db.Integer,nullable=False)
    Cumilative_Credits = db.Column(db.Integer,nullable=False)
    SGPA = db.Column(db.Integer,nullable=False)
    CGPA = db.Column(db.Integer,nullable=False)

class Sem3(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    RegNo = db.Column(db.String(10),nullable=False)
    Name = db.Column(db.String(50),nullable=False)
    MAT203 = db.Column(db.String(10),nullable=False)
    CST201 = db.Column(db.String(10),nullable=False)
    CST203 = db.Column(db.String(10),nullable=False)
    CST205 = db.Column(db.String(10),nullable=False)
    HUT200 = db.Column(db.String(10),nullable=False)
    MCN201 = db.Column(db.String(10),nullable=False)
    CSL201 = db.Column(db.String(10),nullable=False)
    CSL203 = db.Column(db.String(10),nullable=False)
    Earned_Credits = db.Column(db.Integer,nullable=False)
    Cumilative_Credits = db.Column(db.Integer,nullable=False)
    SGPA = db.Column(db.Integer,nullable=False)
    CGPA = db.Column(db.Integer,nullable=False)

class Sem4(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    RegNo = db.Column(db.String(10),nullable=False)
    Name = db.Column(db.String(50),nullable=False)
    EST200 = db.Column(db.String(10),nullable=False)
    MCN202 = db.Column(db.String(10),nullable=False)
    CST202 = db.Column(db.String(10),nullable=False)
    CST204 = db.Column(db.String(10),nullable=False)
    CST206 = db.Column(db.String(10),nullable=False)
    CSL202 = db.Column(db.String(10),nullable=False)
    CSL204 = db.Column(db.String(10),nullable=False)
    MAT206 = db.Column(db.String(10),nullable=False)
    Earned_Credits = db.Column(db.Integer,nullable=False)
    Cumilative_Credits = db.Column(db.Integer,nullable=False)
    SGPA = db.Column(db.Integer,nullable=False)
    CGPA = db.Column(db.Integer,nullable=False)

class Sem5(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    RegNo = db.Column(db.String(10),nullable=False)
    Name = db.Column(db.String(50),nullable=False)
    MCN301 = db.Column(db.String(10),nullable=False)
    CST301 = db.Column(db.String(10),nullable=False)
    CST303 = db.Column(db.String(10),nullable=False)
    CST305 = db.Column(db.String(10),nullable=False)
    CST307 = db.Column(db.String(10),nullable=False)
    CST309 = db.Column(db.String(10),nullable=False)
    CSL331 = db.Column(db.String(10),nullable=False)
    CSL333 = db.Column(db.String(10),nullable=False)
    Earned_Credits = db.Column(db.Integer,nullable=False)
    Cumilative_Credits = db.Column(db.Integer,nullable=False)
    SGPA = db.Column(db.Integer,nullable=False)
    CGPA = db.Column(db.Integer,nullable=False)

class Sem6(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    RegNo = db.Column(db.String(10),nullable=False)
    Name = db.Column(db.String(50),nullable=False)
    CST302 = db.Column(db.String(10),nullable=False)
    CST304 = db.Column(db.String(10),nullable=False)
    CST306 = db.Column(db.String(10),nullable=False)
    CST322 = db.Column(db.String(10),nullable=True) #Electiv I
    CST332 = db.Column(db.String(10),nullable=True) #Electiv I
    HUT300 = db.Column(db.String(10),nullable=False)
    CST308 = db.Column(db.String(10),nullable=False)
    CSL332 = db.Column(db.String(10),nullable=False)
    Earned_Credits = db.Column(db.Integer,nullable=False)
    Cumilative_Credits = db.Column(db.Integer,nullable=False)
    SGPA = db.Column(db.Integer,nullable=False)
    CGPA = db.Column(db.Integer,nullable=False)

class Sem7(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    RegNo = db.Column(db.String(10),nullable=False)
    Name = db.Column(db.String(50),nullable=False)
    CST401 = db.Column(db.String(10),nullable=False)
    CST423 = db.Column(db.String(10),nullable=False)
    CST433 = db.Column(db.String(10),nullable=False)
    MCN401 = db.Column(db.String(10),nullable=False)
    CSL411 = db.Column(db.String(10),nullable=False)
    CSQ413 = db.Column(db.String(10),nullable=False)
    CSD415 = db.Column(db.String(10),nullable=False)
    CST455 = db.Column(db.String(10),nullable=False)
    Earned_Credits = db.Column(db.Integer,nullable=False)
    Cumilative_Credits = db.Column(db.Integer,nullable=False)
    SGPA = db.Column(db.Integer,nullable=False)
    CGPA = db.Column(db.Integer,nullable=False)

class Sem8(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    RegNo = db.Column(db.String(10),nullable=False)
    Name = db.Column(db.String(50),nullable=False)
    CST402 = db.Column(db.String(10),nullable=False)
    CST434 = db.Column(db.String(10),nullable=False)
    CST414 = db.Column(db.String(10),nullable=False)
    CST466 = db.Column(db.String(10),nullable=False)
    CST416 = db.Column(db.String(10),nullable=False)
    CST428 = db.Column(db.String(10),nullable=False)
    CST448 = db.Column(db.String(10),nullable=False)
    CST404 = db.Column(db.String(10),nullable=False)
    CSD416 = db.Column(db.String(10),nullable=False)
    Earned_Credits = db.Column(db.Integer,nullable=False)
    Cumilative_Credits = db.Column(db.Integer,nullable=False)
    SGPA = db.Column(db.Integer,nullable=False)
    CGPA = db.Column(db.Integer,nullable=False)