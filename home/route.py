from flask import Blueprint,url_for,render_template,request,redirect,flash,current_app
# from user.models import users
import os
from werkzeug.utils import secure_filename
from utills.file_helper import valid_file
home=Blueprint("home",__name__,template_folder='../templates/home')

@home.get('/')
def homes():
    return render_template('users/list.html',users=users)

@home.get('/create')
def show_create_form():
   return render_template('users/create.html')


@home.post('/create')
def handle_create_form():
   name=request.form.get('name')
   email=request.form.get('email')
   file=request.files.get('file')
  
   if file and file.filename:
    if valid_file(file.filename):
        safe_file_name = secure_filename(file.filename)

        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)

        upload_file = os.path.join(
            upload_folder,
            safe_file_name
        )

        file.save(upload_file)

        flash("File is Uploaded!")
    else:
        flash("Invalid file type!")

#    if not name and not email:
#         return redirect(url_for('home.homes'))
   
#    if file and valid_file(file):
#       safe_file_name=secure_filename(file)
#       upload_file=os.path.join(current_app.config['UPLOAD_FOLDER'],safe_file_name)
#       file.save()
#       flash("File is Uploaded ")
   users.append(
    {
               'id':len(users)+1,
               'name':name,
               'email':email
           }
       )
   flash("User Is Created! ")
      
   
   return render_template('users/create.html')



# @home.route('/edit/<int:user_id>' ,methods=['get','post','update'])
# def show_edit_form(user_id):
#     # for u in users:
#     #   if u['id']==user_id:
#     #      user=u
#     #      break
    
#     user=next((u for u in users if u['id'] ==user_id),None)
    

#     if not user:
#       return redirect(url_for('home.homes'))


#     return render_template('users/edit.html',user=user)

@home.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def show_edit_form(user_id):

    user = next(
        (u for u in users if u['id'] == user_id),
        None
    )

    if not user:
        return redirect(url_for('home.homes'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if name and email:
            user['name'] = name
            user['email'] = email

            flash("User Is Updated !")
            return redirect(url_for('home.homes'))
    
    return render_template('users/edit.html', user=user)



@home.post('/delete/<int:user_id>')
def handle_delete_form(user_id):

    user = next(
        (u for u in users if u['id'] == user_id),
        None
    )

    if not user:
        return redirect(url_for('home.homes'))

    users.remove(user)
    flash("User Is Deleted !")

    return redirect(url_for('home.homes'))