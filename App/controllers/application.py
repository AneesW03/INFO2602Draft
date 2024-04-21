from App.models import Application, Status
from App.database import db

def create_application(student_id, internship_id, student_text, status):
    newApplication = Application(
        student_id = student_id,
        internship_id = internship_id,
        student_text = student_text,
        admin_text = None,
        status = status
    )
    db.session.add(newApplication)
    db.session.commit()
    return newApplication

def get_application(id):
    return Application.query.get(id)

def get_all_applications():
    return Application.query.all()

def accept_application(id, admin_text):
    application = Application.query.get(id)
    db.session.delete(application)
    application.status = Status.ACCEPTED
    application.admin_text = admin_text
    db.session.add(application)
    db.session.commit()

def decline_application(id, admin_text):
    application = Application.query.get(id)
    db.session.delete(application)
    application.status = Status.DENIED
    application.admin_text = admin_text
    db.session.add(application)
    db.session.commit()