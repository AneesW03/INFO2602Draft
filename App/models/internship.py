from App.database import db

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=False)
    company_name = db.Column(db.String(255), nullable=False, unique=False)
    location = db.Column(db.String(255), nullable=False, unique=False)
    start_date = db.Column(db.String(255), nullable=False, unique=False)
    duration = db.Column(db.String(255), nullable=False, unique=False)
    stipend = db.Column(db.String(80), nullable=False, unique=False)

    def __init__(self, title, company_name, location, start_date, duration, stipend):
        self.title = title
        self.company_name = company_name
        self.location = location
        self.start_date = start_date
        self.duration = duration
        self.stipend = stipend

    def get_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "company_name": self.company_name,
            "location": self.location,
            "start_date": self.start_date,
            "duration": self.duration,
            "stipend": self.stipend
        }