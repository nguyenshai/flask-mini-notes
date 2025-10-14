#auth/__init__.py

from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user_by_email = User.query.filter_by(email=email).first()
        user_by_username = User.query.filter_by(username=username).first()

        # Check if email or username already exists
        if user_by_email or user_by_username:
            flash('Email or username already exists', category='error')
        else:
            # Hash password before saving
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully', category='success')
            return redirect(url_for('auth.login'))

    return render_template('sign_up.html', user=current_user)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        # Validate credentials
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash('Login successful', category='success')
            return redirect(url_for('notes.home'))
        else:
            flash('Invalid credentials', category='error')

    return render_template('login.html', user=current_user)

@auth_bp.route('/logout')
@login_required
def logout():
    # Log out current user
    logout_user()
    flash('Logged out successfully', category='info')
    return redirect(url_for('auth.login'))