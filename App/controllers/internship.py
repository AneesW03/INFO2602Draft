import csv
from App.models import Internship
from App.database import db
from sqlalchemy import func

def create_internship(title, company_name, location, start_date, duration, stipend):
    newInternship = Internship(
        title=title,
        company_name=company_name,
        location=location,
        start_date=start_date,
        duration=duration,
        stipend=stipend
    )
    db.session.add(newInternship)
    db.session.commit()
    return newInternship

def parse_internships():
    with open('internship.csv') as file:
        reader = csv.DictReader(file)
        newInternships = []
        for row in reader:
            newInternships.append( Internship(
                title = row['internship_title'],
                company_name = row['company_name'],
                location = row['location'],
                start_date = row['start_date'],
                duration = row['duration'],
                stipend = row['stipend']
            ))
        db.session.add_all(newInternships)
        db.session.commit()

def get_internship_by_title(internship_title):
    return Internship.query.filter_by(internship_title=internship_title).all()

def get_internship(id):
    return Internship.query.filter_by(id=id).first()

def get_all_internships():
    return Internship.query.all()

def get_internships_by_company_name(company_name):
    return Internship.query.filter_by(company_name=company_name).all()

def get_all_internships_json():
    internships = Internship.query.all()
    if not internships:
        return []
    internships = [internship.get_json() for internship in internships]
    return internships

def search_internships(searchString):
    return Internship.query.filter(func.lower(Internship.title).like(f'%{searchString.lower()}%')).all()