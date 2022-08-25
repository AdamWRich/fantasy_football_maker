from ffm_app import app
from ffm_app.models.base_models import BaseModel
from ffm_app.models.player_model import PlayerModel
from ffm_app.models.user_model import UserModel
from ffm_app.config.connecttoMySQL import MySQLConnection

class TeamModel(BaseModel):

    table = "teams"
    json_fields = ['id', 'name', 'user_id']

    basic_select = """
        teams.id AS id,
        name,

        users.id AS user_id
    """

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user = UserModel.get_by_id(data['user_id'])
        self.players = []

    @classmethod
    def add(cls, new_team):

        query = """
            INSERT INTO teams
                (
                    name,
                    user_id
                )
            VALUES
                (
                    %(name)s,
                    %(user_id)s
                )
        """
        new_team_id = MySQLConnection(cls.db).query_db(query, new_team)
        

        return None if not new_team_id else cls.get_by_id(new_team_id)

    @classmethod
    def get_team_from_user_id(cls, data):
        offense_query = """
            SELECT *
            FROM teams
            LEFT JOIN players_offense
            ON players_offense.team_id = teams.id
            WHERE user_id = %(user_id)s
        """
        results1 = MySQLConnection(cls.db).query_db(offense_query, data)

        if results1 == ():
            print("No teams associated with user")
            return None
        single_team_data = {
            'id': results1[0]['id'],
            'name':results1[0]['name'],
            'user_id':results1[0]['user_id']
        }

        current_team_object = TeamModel(single_team_data)
        for row in results1:
            player_data = {
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "team_name":row['last_name'],
                "position":row['position'],
                "yards":row['yards'],
                "tds":row['tds']
            }
            player_object = PlayerModel(player_data)
            current_team_object.players.append(player_object)
        
        defense_query = """
            SELECT *
            FROM teams
            LEFT JOIN players_defense
            ON players_defense.team_id = teams.id
            WHERE user_id = %(user_id)s
        """
        results2 = MySQLConnection(cls.db).query_db(defense_query, data)
        for row in results2:
            def_team_data = {
                'team_name':row['team_name'],
                'sacks':row['sacks'],
                'ints':row['ints']
            }
            def_player_object = PlayerModel(def_team_data)
            current_team_object.players.append(def_player_object)
        
        return current_team_object


    @classmethod
    def update(cls, update_data):

        query = """
            UPDATE teams
            SET
                name = %(name)s
            WHERE 
                id = %(id)s
        """

        team_id = MySQLConnection(cls.db).query_db(query, update_data)

        return cls.get_by_id(update_data['id']) if team_id else None
