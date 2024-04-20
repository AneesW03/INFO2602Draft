from App.models import Application, Status
from App.database import db

def create_application(student_id, internship_id, status):
    newApplication = Application(
        student_id = student_id,
        internship_id = internship_id,
        status = status
    )
    db.session.add(newApplication)
    db.session.commit()
    return newApplication

def get_all_applications():
    return Application.query.all()

def accept_application(id):
    application = Application.query.get(id)
    db.session.delete(application)
    application.status = Status.ACCEPTED
    db.session.add(application)
    db.session.commit()

def decline_application(id):
    application = Application.query.get(id)
    db.session.delete(application)
    application.status = Status.DENIED
    db.session.add(application)
    db.session.commit()