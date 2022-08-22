from flask import jsonify, json
import requests


# Weekly game schedules and scores (can grab times and locations if interested)
url = "https://nfl-schedule.p.rapidapi.com/v1/schedules"

headers = {
	"X-RapidAPI-Key": "8aabf3df13mshf320515c323dc95p151b82jsncb13f13b694a",
	"X-RapidAPI-Host": "nfl-schedule.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

schedule = json.loads(response.text)
print(schedule['message'])


all_games = []

for game in schedule['data']:
    name = game['shortName']
    away_score = game['awayTeam']['score']
    home_score = game['homeTeam']['score']
    final_score = (f'{away_score} - {home_score}')
    single_game_data = {
        "name": name,
        "final_score":final_score
    }
    all_games.append(single_game_data)

print(all_games)