from App.database import db
from enum import Enum

class Status(Enum):
    AWAITING_RESPONSE = "Awaiting Response"
    ACCEPTED = "Application Accepted"
    DENIED = "Application Denied"

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'), nullable=False)
    student_text = db.Column(db.String(255), unique=False, nullable=True)
    admin_text = db.Column(db.String(255), unique=False, nullable=True)
    status = db.Column(db.Enum(Status), nullable=False)
    

    def __init__(self,student_id,internship_id,student_text,admin_text,status):
        self.student_id = student_id
        self.internship_id = internship_id
        self.student_text = student_text
        self.admin_text = admin_text
        self.status = status