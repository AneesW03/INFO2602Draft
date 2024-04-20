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
    status = db.Column(db.Enum(Status), nullable=False)
    

    def __init__(self,student_id,internship_id,status):
        self.student_id = student_id
        self.internship_id = internship_id
        self.status = status
    
    def get_json(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'status': self.status
        }
