from flask import render_template, redirect, url_for, request, Blueprint, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('account register', category='success')
        return redirect(url_for('auth.login'))
    
    return render_template('teacher/teacher_register.html')  # Create this template

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        SecretKey = request.form.get('SecretKey')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password) and SecretKey == "secret":

            flash('Logged in successfully!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('TeacherViews.home'))
        else:
            flash('account does not exist.', category='error')
        
    return render_template('teacher/teacher_login.html') 

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
