from flask import render_template, redirect, request, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user 
from core import db
from core.models import User
from core.auth import bp
from werkzeug.security import generate_password_hash, check_password_hash

@bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in', 'success')
                login_user(user, remember=True)
                return redirect(url_for('main.index'))
            else:
                flash('Password is incorrect', 'error')
        else: 
            flash('User does not exist', 'error')
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    return render_template(
        'login.html',
        title='Login',
        current_user = current_user
    )


@bp.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password = request.form.get('password')
        password_2 = request.form.get('password_2')

        email_exists = User.query.filter_by(email=email).first()


        if email_exists:
            flash('Email is already in use', 'error')
        elif password != password_2:
            flash('Passwords do not match', 'error')
        elif len(str(email)) < 4:
            flash('Email is too short', 'error')
        elif len(str(password)) < 6:
            flash('Password is too short', 'error')
        elif '@' not in email:
            flash('Please enter a valid email address', 'error')
        else:
            new_user = User(
                email = email,
                first_name = first_name.title(),
                password = generate_password_hash(password, method='sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash(f'Welcome {new_user.first_name}', 'success')
            return redirect(url_for('main.app'))
    if current_user.is_authenticated:
        return redirect(url_for('main.app'))
    return render_template(
        'register.html',
        title = 'Register'
    )
