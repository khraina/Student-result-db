from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))


class Sem1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=False)
    RegNo = db.Column(db.String(10), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    PHT100 = db.Column(db.String(10), nullable=False)
    MAT101 = db.Column(db.String(10), nullable=False)
    HUN101 = db.Column(db.String(10), nullable=False)
    EST100 = db.Column(db.String(10), nullable=False)
    EST130 = db.Column(db.String(10), nullable=False)
    PHL120 = db.Column(db.String(10), nullable=False)
    ESL130 = db.Column(db.String(10), nullable=False)
    Earned_Credits = db.Column(db.Integer, nullable=False)
    Cumilative_Credits = db.Column(db.Integer, nullable=False)
    SGPA = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.Integer, nullable=False)


class Sem2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=False)
    RegNo = db.Column(db.String(10), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    EST120 = db.Column(db.String(10), nullable=False)
    CYT100 = db.Column(db.String(10), nullable=False)
    EST110 = db.Column(db.String(10), nullable=False)
    MAT102 = db.Column(db.String(10), nullable=False)
    EST102 = db.Column(db.String(10), nullable=False)
    HUN102 = db.Column(db.String(10), nullable=False)
    CYL120 = db.Column(db.String(10), nullable=False)
    ESL120 = db.Column(db.String(10), nullable=False)
    ESL102 = db.Column(db.String(10), nullable=False)
    Earned_Credits = db.Column(db.Integer, nullable=False)
    Cumilative_Credits = db.Column(db.Integer, nullable=False)
    SGPA = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.Integer, nullable=False)


class Sem3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=False)
    RegNo = db.Column(db.String(10), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    MAT203 = db.Column(db.String(10), nullable=False)
    CST201 = db.Column(db.String(10), nullable=False)
    CST203 = db.Column(db.String(10), nullable=False)
    CST205 = db.Column(db.String(10), nullable=False)
    HUT200 = db.Column(db.String(10), nullable=False)
    MCN201 = db.Column(db.String(10), nullable=False)
    CSL201 = db.Column(db.String(10), nullable=False)
    CSL203 = db.Column(db.String(10), nullable=False)
    Earned_Credits = db.Column(db.Integer, nullable=False)
    Cumilative_Credits = db.Column(db.Integer, nullable=False)
    SGPA = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.Integer, nullable=False)


class Sem4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=False)
    RegNo = db.Column(db.String(10), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    EST200 = db.Column(db.String(10), nullable=False)
    MCN202 = db.Column(db.String(10), nullable=False)
    CST202 = db.Column(db.String(10), nullable=False)
    CST204 = db.Column(db.String(10), nullable=False)
    CST206 = db.Column(db.String(10), nullable=False)
    CSL202 = db.Column(db.String(10), nullable=False)
    CSL204 = db.Column(db.String(10), nullable=False)
    MAT206 = db.Column(db.String(10), nullable=False)
    Earned_Credits = db.Column(db.Integer, nullable=False)
    Cumilative_Credits = db.Column(db.Integer, nullable=False)
    SGPA = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.Integer, nullable=False)


class Sem5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=False)
    RegNo = db.Column(db.String(10), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    MCN301 = db.Column(db.String(10), nullable=False)
    CST301 = db.Column(db.String(10), nullable=False)
    CST303 = db.Column(db.String(10), nullable=False)
    CST305 = db.Column(db.String(10), nullable=False)
    CST307 = db.Column(db.String(10), nullable=False)
    CST309 = db.Column(db.String(10), nullable=False)
    CSL331 = db.Column(db.String(10), nullable=False)
    CSL333 = db.Column(db.String(10), nullable=False)
    Earned_Credits = db.Column(db.Integer, nullable=False)
    Cumilative_Credits = db.Column(db.Integer, nullable=False)
    SGPA = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.Integer, nullable=False)


class Sem6(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=False)
    RegNo = db.Column(db.String(10), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    CST302 = db.Column(db.String(10), nullable=False)
    CST304 = db.Column(db.String(10), nullable=False)
    CST306 = db.Column(db.String(10), nullable=False)
    CST322 = db.Column(db.String(10), nullable=True)  # Electiv I
    CST332 = db.Column(db.String(10), nullable=True)  # Electiv I
    HUT300 = db.Column(db.String(10), nullable=False)
    CST308 = db.Column(db.String(10), nullable=False)
    CSL332 = db.Column(db.String(10), nullable=False)
    Earned_Credits = db.Column(db.Integer, nullable=False)
    Cumilative_Credits = db.Column(db.Integer, nullable=False)
    SGPA = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.Integer, nullable=False)


class Sem7(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=False)
    RegNo = db.Column(db.String(10), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    CST401 = db.Column(db.String(10), nullable=False)
    CST423 = db.Column(db.String(10), nullable=False)
    CST433 = db.Column(db.String(10), nullable=False)
    MCN401 = db.Column(db.String(10), nullable=False)
    CSL411 = db.Column(db.String(10), nullable=False)
    CSQ413 = db.Column(db.String(10), nullable=False)
    CSD415 = db.Column(db.String(10), nullable=False)
    CST455 = db.Column(db.String(10), nullable=False)
    Earned_Credits = db.Column(db.Integer, nullable=False)
    Cumilative_Credits = db.Column(db.Integer, nullable=False)
    SGPA = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.Integer, nullable=False)


class Sem8(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, nullable=False)
    RegNo = db.Column(db.String(10), nullable=False)
    Name = db.Column(db.String(50), nullable=False)
    CST402 = db.Column(db.String(10), nullable=False)
    CST434 = db.Column(db.String(10), nullable=False)
    CST414 = db.Column(db.String(10), nullable=False)
    CST466 = db.Column(db.String(10), nullable=False)
    CST416 = db.Column(db.String(10), nullable=False)
    CST428 = db.Column(db.String(10), nullable=False)
    CST448 = db.Column(db.String(10), nullable=False)
    CST404 = db.Column(db.String(10), nullable=False)
    CSD416 = db.Column(db.String(10), nullable=False)
    Earned_Credits = db.Column(db.Integer, nullable=False)
    Cumilative_Credits = db.Column(db.Integer, nullable=False)
    SGPA = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.Integer, nullable=False)
