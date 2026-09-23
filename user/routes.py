from flask import Blueprint

users_bp=Blueprint('user',__name__)

@users_bp.route('/')
def users():
    return "List Of Users"

@users_bp.route('/profile')
def profile():
    return 'this the progile page'