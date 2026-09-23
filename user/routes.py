from flask import Blueprint,request

users_bp=Blueprint('user',__name__)

@users_bp.route('/')
def users():
    return "List Of Users"

@users_bp.route('/profile',methods=['post'])
def profile():
    return 'this the progile page'


@users_bp.route('go/<id>',methods=['put','get','post'])
def user(id):
    return f'this is the user id : {id} '

@users_bp.route('/summa/<path:subpath>')
def summa(subpath):
    return f' this is the summa path {subpath}'

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login submitted"
    return "Login page"