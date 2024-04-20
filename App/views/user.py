from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user
from.index import index_views
from App.models import Role
from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    get_all_internships,
    create_internship,
    get_internships_by_company_name,
    create_application,
    get_all_applications,
    accept_application,
    decline_application
)


user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/home', methods=['GET'])
@jwt_required()
def home_page():
    if current_user.role == Role.STUDENT:
        internships = get_all_internships()
        return render_template('student.html', internships=internships)
    if current_user.role == Role.COMPANY:
        internships = get_internships_by_company_name(current_user.company_name)
        return render_template('company.html', internships=internships)
    if current_user.role == Role.ADMIN:
        applications = get_all_applications()
        return render_template('admin.html', applications=applications)

@user_views.route('/create_internship', methods=['POST'])
@jwt_required()
def create_internship_action():
    data = request.form
    create_internship(data['internship_title'],data['company_name'],data['location'],data['start_date'],data['duration'],data['stipend'])
    flash('Internship Added Successfully')
    return redirect(request.referrer)

@user_views.route('/apply/<int:id>', methods=['POST'])
@jwt_required()
def add_application_action(id):
    create_application(current_user.id, id, 'AWAITING_RESPONSE')
    flash('Application Submitted Successfully')
    return redirect(request.referrer)

@user_views.route('/accept/<int:id>', methods=["POST"])
@jwt_required()
def accept_application_action(id):
    accept_application(id)
    flash('Application Updated Successfully')
    return redirect(request.referrer)

@user_views.route('/decline/<int:id>', methods=['POST'])
@jwt_required()
def decline_application_action(id):
    decline_application(id)
    flash('Application Declined Successfully')
    return redirect(request.referrer)

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    user = create_user(data['username'], data['password'])
    return jsonify({'message': f"user {user.username} created with id {user.id}"})

