from flask import Blueprint, render_template, request, redirect, url_for, flash
from extension import db
from user.models import User
from flask_login import login_user


auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth'
)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        # Check empty fields
        if not name or not email or not password:
            return render_template(
                'resgister.html',
                error='All fields are required'
            )

        # Check duplicate email
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return render_template(
                'resgister.html',
                error='Email already registered'
            )

        # Create user object
        user = User(
            name=name,
            email=email
        )

        # Hash password
        user.set_password(password)

        # Save to MySQL
        db.session.add(user)
        db.session.commit()

        flash('Registration successful!', 'success')

        return redirect(url_for('auth.handle_login'))

    return render_template('resgister.html')



@auth_bp.route('/login', methods=['GET', 'POST'])
def handle_login():

    if request.method == 'POST':

        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        # Find user by email
        user = User.query.filter_by(email=email).first()

        # Check user and password
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home.homes'))

        return render_template(
            'login.html',
            error='Invalid email or password'
        )

    return render_template('login.html')

