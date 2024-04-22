from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from enum import Enum

class Role(Enum):
    STUDENT = "Student"
    COMPANY = "Company"
    ADMIN = "Admin"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)
    company_name = db.Column(db.String(120), nullable=True, unique=True)
    application = db.relationship('Application', backref=db.backref('user'), lazy=True)

    def __init__(self, username, password, role, company_name):
        self.username = username
        self.set_password(password)
        self.role = role
        self.company_name = company_name

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
