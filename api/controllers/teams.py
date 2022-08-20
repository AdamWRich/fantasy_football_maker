from api import app
from flask import jsonify, request, session, redirect
from api.models.user_model import UserModel
from api.models.team_model import TeamModel

@app.route('/team/add', methods=['POST'])
def add_team(user, data):
    
    new_team = TeamModel.add(user, data)

    if new_team is not None:
        return jsonify(new_team.to_json()), 201
    
    return jsonify({}), 422

@app.route('/team/update', methods=['POST'])
def update_team(user, data):

    team = TeamModel.filter_one_by({
        'users_id':user.id,
        'id':data['id']
    })

    if team is not None:
        updated_team = TeamModel.update(team)
        if updated_team:
            return jsonify(updated_team.to_json()), 200
    
    return jsonify({}), 422

@app.route('/team/delete/<id>', methods=['POST'])
def delete_team(id, user):

    team = TeamModel.filter_one_by({
        'users_id':user.id,
        'id':id
    })

    if team is not None:
        TeamModel.delete(id)
        return jsonify({'status': 'ok'}), 200

    return jsonify({}), 422

@app.route('/team/<id>')
def get_team(id, user):

    team = TeamModel.filter_one_by({
        'users_id':user.id,
        'id':id
    })

    if team is not None:
        return jsonify(team.to_json()), 200