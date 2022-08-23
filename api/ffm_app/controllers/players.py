import json
from ffm_app import app
from flask import jsonify, request, session, redirect
from ffm_app.models.user_model import UserModel
from ffm_app.models.team_model import TeamModel
from ffm_app.models.team_model import PlayerModel

from ffm_app.config.player_data.players_json import player_data


@app.route('/player/view-all/<team_id>')
def view_all_players(team_id):
    current_team = TeamModel.get_one_team_with_players(team_id)
    if current_team:
        available_players = {}
        for key, value in player_data.items():
                if key not in current_team.players:
                    available_players[key] = value

        return jsonify(available_players), 200
    return jsonify({
        'error':'unable to find team_id'
    }), 400

@app.route('/player/view-all/')
def view_all_players_without_team():
    available_players = {}
    for key, value in player_data.items():
            available_players[key] = value
    
    return jsonify(available_players), 200



@app.route('/player/add/<player_id>/<team_id>', methods=['POST'])
def add_player_to_team(player_id, team_id):
    player_to_add = PlayerModel.save_player(player_data[player_id])
    print(player_to_add)
    data = {
        'player_id':player_to_add['id'],
        'team_id':team_id
    }
    if player_to_add['position'] == "DEF":
        data['table']  = "players_defense"
    else:
        data['table'] = "players_offense"
    added_to_team = PlayerModel.add_player_to_team(data)
    if added_to_team:
        return jsonify({}), 200
    else:
        return jsonify({
            'error': 'unable to add player to team'
        }), 400


@app.route('/player/remove/<player_id>/<team_id>', methods=['POST'])
def remove_player_from_team(player_id, team_id):
    player_position = PlayerModel.get_by_id(player_id)['position']
    data = {
        'player_id':player_id
    }
    if player_position == "DEF":
        data['table']  = "players_defense"
    else:
        data['table'] = "players_offense"
    removed_player = PlayerModel.remove_player_from_team(data)
    if removed_player:
        return jsonify({}), 200
    else:
        return jsonify({
            "error":"unable to remove from team"
        }), 400
