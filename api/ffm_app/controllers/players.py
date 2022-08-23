import json
from ffm_app import app
from flask import jsonify, request, session, redirect
from ffm_app.models.user_model import UserModel
from ffm_app.models.team_model import TeamModel
from ffm_app.config.players.players_offense import player_data


# @app.route('/player/view-all/<team_id>')
# def view_all_players(team_id):
#     current_team = TeamModel.get_by_id(team_id)
#     available_players = []
#     for player in player_data:
#         if player not in current_team.players:

#     return jsonify(), 200



@app.route('/player/add/<team_id>', methods=['POST'])
def add_player_to_team():
    player_to_add  = request.get_json()

