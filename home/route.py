from flask import Blueprint,url_for,render_template

home=Blueprint("home",__name__,template_folder='../templates/home')

@home.get('/')
def homes():
    return render_template('index.html')

# @home.get('/create')
# def show_create_form():
#     pass
# @home.post('/edit/<int:user_id>')
# def show_create_form():
#     pass