from flask import (
    Blueprint, render_template, request,
    redirect, url_for, flash, current_app
)
import os
from werkzeug.utils import secure_filename

from user.models import User
from extension import db  # CHANGE 1: Import db directly
from utills.file_helper import valid_file

home = Blueprint(
    "home",
    __name__,
    template_folder="../templates/home"
)


# =========================
# READ - Display all users
# =========================
@home.get('/')
def homes():
    # CHANGE 2: Fetch users from the database
    users = User.query.all()

    return render_template(
        'users/list.html',
        users=users
    )


# =========================
# SHOW CREATE FORM

@home.get('/create')
def show_create_form():
    return render_template('users/create.html')


# =========================
# CREATE - Add a new user

@home.post('/create')
def handle_create_form():
    name = request.form.get('name')
    email = request.form.get('email')
    file = request.files.get('file')

    # CHANGE 3: Validate required fields
    if not name or not email:
        flash("Name and email are required!")
        return redirect(url_for('home.show_create_form'))

    # File upload (optional)
    if file and file.filename:
        if not valid_file(file.filename):
            flash("Invalid file type!")
            return redirect(url_for('home.show_create_form'))

        safe_file_name = secure_filename(file.filename)

        upload_folder = current_app.config['UPLOAD_FOLDER']
        os.makedirs(upload_folder, exist_ok=True)

        upload_file = os.path.join(
            upload_folder,
            safe_file_name
        )

        file.save(upload_file)
        flash("File is uploaded!")

    # Create a database record
    user_new = User(name=name, email=email)

    db.session.add(user_new)
    db.session.commit()

    flash("User is created!")

    # CHANGE 4: Redirect to the user list after creating
    return redirect(url_for('home.homes'))


# =========================
# UPDATE - Edit a user
# =========================
@home.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def show_edit_form(user_id):

    # CHANGE 5: Get the user from the database
    user = db.session.get(User, user_id)

    if user is None:
        flash("User not found!")
        return redirect(url_for('home.homes'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            flash("Name and email are required!")
            return render_template(
                'users/edit.html',
                user=user
            )

        # CHANGE 6: Update database model attributes
        user.name = name
        user.email = email

        # CHANGE 7: Save the changes to the database
        db.session.commit()

        flash("User is updated!")
        return redirect(url_for('home.homes'))

    return render_template(
        'users/edit.html',
        user=user
    )


# =========================
# DELETE - Remove a user
# =========================
@home.post('/delete/<int:user_id>')
def handle_delete_form(user_id):

    # CHANGE 8: Find the user in the database
    user = db.session.get(User, user_id)

    if user is None:
        flash("User not found!")
        return redirect(url_for('home.homes'))

    # CHANGE 9: Delete the database record
    db.session.delete(user)
    db.session.commit()

    flash("User is deleted!")

    return redirect(url_for('home.homes'))