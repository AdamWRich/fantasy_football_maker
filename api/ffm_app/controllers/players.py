import json
from ffm_app import app
from flask import jsonify, request, session, redirect, render_template
from ffm_app.models.user_model import UserModel
from ffm_app.models.team_model import TeamModel
from ffm_app.models.team_model import PlayerModel
from ffm_app.config.player_data.players_json import player_data


@app.route('/player/view/<player_id>')
def view_all_players(player_id):
    current_player = player_data[player_id]
    print(current_player)
    return render_template('playerdetails.html', player = current_player)

@app.route('/player/view-all/<int:team_id>')
def view_all_players_without_team(team_id):
    user = UserModel.get_by_id(session['user_id'])
    available_players = []
    for player in player_data.values():
            available_players.append(player)
    return render_template("allplayers.html", user = user, players = available_players, team_id = team_id)



@app.route('/player/add/<int:team_id>/<player_id>', methods=['POST'])
def add_player_to_team(player_id, team_id):
    player_to_add = PlayerModel.save_player(player_data[player_id])
    print(player_to_add)
    data = {
        'player_id':player_to_add,
        'team_id':team_id,
        'table':"players_offense"
    }
    PlayerModel.add_player_to_team(data)
    return redirect('/dashboard')



@app.route('/player/remove/', methods=['POST'])
def remove_player_from_team():
    data = {
        'player_id':request.form['player_id']
    }
    print(data['player_id'])
    PlayerModel.remove_player_from_team(data)
    return redirect('/dashboard')
