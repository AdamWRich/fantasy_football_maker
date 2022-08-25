from ffm_app import app
from flask import request, session, redirect, render_template, flash
from ffm_app.models.user_model import UserModel

    
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect('/dashboard')
    return redirect('/login_register')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    user = UserModel.get_by_id(session['user_id'])
    return render_template('dashboard.html', user = user)

@app.route('/user/register', methods=['POST'])
def register():
    user_data = request.form
    registration_errors = UserModel.validate_registration_data(user_data)
    if len(registration_errors) > 0:
        print('error here')
        for message in registration_errors:
            flash(f'{message}', 'register')
        return redirect('/login_register', )
    new_user = UserModel.add_user(user_data)
    print(new_user)
    if new_user is None:
        flash(f'Error creating user', 'register')
        return redirect('/login_register')
    session['user_id'] = new_user  
    return redirect('/dashboard')

@app.route('/login_register')
def login_register():
    return render_template("login.html")

@app.route('/user/login', methods=['POST'])
def login():

    credentials = request.form
    user = UserModel.login(credentials)
    session['user_id'] = user.id
    print(session['user_id'])
    if user is not None:
        return redirect('/dashboard')
    else:
        flash('Email or password incorrect', 'login')
    return redirect('/login_register')

@app.route('/user/logout')
def logout():
    session.clear()
    return redirect('/login_register')

# for up to date User info
# @app.route('/user/current-user')
# def get_current_user():
#     current_user = UserModel.get_by_id(session['user_id'], True)
#     if 'user_id' not in session:
#         return redirect('/user/logout')
    
#     return jsonify(current_user), 200



