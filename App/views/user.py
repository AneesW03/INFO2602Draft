from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user
from.index import index_views
from App.models import Role
from App.controllers import (
    get_all_internships,
    create_internship,
    get_internships_by_company_name,
    create_application,
    get_all_applications,
    accept_application,
    decline_application,
    get_application,
    search_internships
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

# Redirects to the home page which depends on the type of user (student, admin, company)
@user_views.route('/home/<int:id>', methods=['GET'])
@user_views.route('/home', methods=['GET'])
@jwt_required()
def home_page(id=None):
    selected_application = None
    if current_user.role == Role.STUDENT:
        if id != None:
            selected_application = get_application(id)
        internships = get_all_internships()
        return render_template('student.html', internships=internships, selected_application=selected_application)
    if current_user.role == Role.COMPANY:
        internships = get_internships_by_company_name(current_user.company_name)
        return render_template('company.html', internships=internships)
    if current_user.role == Role.ADMIN:
        if id != None:
            selected_application = get_application(id)
        applications = get_all_applications()
        return render_template('admin.html', applications=applications, selected_application=selected_application)

@user_views.route('/search', methods=['POST'])
@jwt_required()
def search_action():
    data = request.form
    internships = search_internships(data['search'])
    return render_template('student.html', internships=internships, selected_application=None)

# Allows a company to create and list a new internship
@user_views.route('/create_internship', methods=['POST'])
@jwt_required()
def create_internship_action():
    data = request.form
    create_internship(data['internship_title'],current_user.company_name,data['location'],data['start_date'],data['duration'],data['stipend'])
    flash('Internship Added Successfully')
    return redirect(request.referrer)

# Allows a student to apply for an internship
@user_views.route('/apply/<int:id>', methods=['POST'])
@jwt_required()
def add_application_action(id):
    data = request.form
    result = create_application(current_user.id, id, data['student_text'], 'AWAITING_RESPONSE')
    if result:
        flash('Application Submitted Successfully')
    else:
        flash('Error, Only One Application Allowed')
    return redirect(request.referrer)

# Allows an admin to accept or decline a student's application for an internship
@user_views.route('/response/<int:id>', methods=["POST"])
@jwt_required()
def accept_application_action(id):
    data = request.form
    if data['decision'] == 'ACCEPT':
        accept_application(id, data['admin_text'])
    else:
        decline_application(id, data['admin_text'])
    flash('Application Updated Successfully')
    return redirect(request.referrer)
