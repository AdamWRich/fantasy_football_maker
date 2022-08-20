from api import app
from flask import jsonify, request, session, redirect
from api.models.user_model import UserModel

def get_user_obect(user):
    return {
        "id":user.id
    }

@app.route('/user/register', methods=['POST'])
def register():
    user_data = request.get_json()

    registration_errors = UserModel.validate_registration_data(user_data)
    if len(registration_errors) > 0:
        return jsonify(
            {
                'errors':registration_errors
            }
        ), 422
    new_user = UserModel.add_user(user_data)
    if new_user is None:
        return jsonify(
            {
                'result':'invalid'
            }
        ), 400
    
    return jsonify(), 200

@app.route('/user/login', methods=['POST'])
def login():

    credentials = request.get_json()
    user = UserModel.login(credentials)

    if user is None:
        return jsonify({}), 401

    return jsonify({}), 200

@app.route('/user/logout')
def logout():
    session.clear()
    return jsonify ({}), 200

# for up to date User info
@app.route('/user/current-user')
def get_current_user():
    current_user = UserModel.get_by_id(session['user_id'])
    if 'user_id' not in session:
        return redirect('/user/logout')
    
    return jsonify(current_user), 200



