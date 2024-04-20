from App.models import User, Internship
from App.database import db

def create_user(username, password, role, company_name):
    newuser = User(username=username, password=password, role=role, company_name = company_name)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def create_companies():
    counter = 0
    internships = Internship.query.group_by(Internship.company_name).distinct(Internship.company_name).all()
    for internship in internships:
        username = f"comp{counter}"
        counter += 1
        newUser = User(username = username, 
                    password = 'comppass',
                    role = 'COMPANY',
                    company_name = internship.company_name)
        db.session.add(newUser)
    db.session.commit()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    