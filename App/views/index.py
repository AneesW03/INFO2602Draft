from flask import Blueprint, redirect, render_template, request, jsonify
from App.models import db
from App.controllers import (create_user, get_all_internships, parse_internships, create_companies)
from flask_jwt_extended import jwt_required, current_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass','STUDENT', None)
    create_user('adm', 'admpass', 'ADMIN', None)
    parse_internships()
    create_companies()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})