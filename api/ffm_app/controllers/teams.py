from ffm_app import app
from flask import jsonify, request, session, redirect, flash
from ffm_app.models.user_model import UserModel
from ffm_app.models.team_model import TeamModel



@app.route('/team/add', methods=['POST'])
def add_team():
    team_data = request.form
    TeamModel.add(team_data)
    return redirect('/dashboard')




# @app.route('/team/update', methods=['POST'])
# def update_team():
#     # Right now this will only change team name.
#     updated_team_data = request.get_json()

#     if updated_team_data is not None:
#         updated_team = TeamModel.update(updated_team_data)
#         if updated_team:
#             return jsonify(updated_team.to_json()), 200
    
#     return jsonify({}), 422



@app.route('/team/delete/<id>', methods=['POST'])
def delete_team(id):
    team_user_id = TeamModel.get_by_id(id)
    if team_user_id.user == session['user_id'] and id is not None:
        TeamModel.delete(id)
        return jsonify({'status': 'ok'}), 200

    return jsonify({}), 422


@app.route('/team/<int:id>')
def get_team(id):

    team = TeamModel.get_by_id(id)
    print(team)
    if team is not None:
        return jsonify(team.to_json()), 200