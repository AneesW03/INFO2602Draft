from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from enum import Enum
from.index import index_views

from App.controllers import (
    login,
    get_all_users
)

from App.models import Role

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')
   
# Redirects to the default page where a user can login
@auth_views.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')    

# Authenticates a user and redirects them to their home page
@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    token = login(data['username'], data['password'])
    response = redirect(url_for('user_views.home_page'))
    set_access_cookies(response, token) 
    return response

# Allows a user to logout of the application
@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(url_for('auth_views.login_page')) 
    flash("Logged Out!")
    unset_jwt_cookies(response)
    return response