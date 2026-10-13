from flask import Blueprint,url_for,render_template,request,redirect,flash
from user.models import users
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
   if name and email:
       users.append(
           {
               'id':len(users)+1,
               'name':name,
               'email':email
           }
       )
       flash("User Is Created! ")
       return redirect(url_for('home.homes'))
   
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