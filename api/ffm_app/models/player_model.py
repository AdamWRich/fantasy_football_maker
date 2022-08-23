from ffm_app import app
from ffm_app.models.base_models import BaseModel
from ffm_app.models.user_model import UserModel
from ffm_app.config.connecttoMySQL import MySQLConnection
from ffm_app.config.player_data import players_json



class PlayerModel(BaseModel):
    def __init__(self, data):
        self.team_id = None

    @classmethod
    def save_player(cls, data):
        if data['position'] != "DEF":
            query = """
                INSERT INTO players_offense
                (
                        first_name,
                        last_name,
                        team,
                        position,
                        yards,
                        tds
                    )
                VALUES
                    (
                        %(first_name)s,
                        %(last_name)s,
                        %(team)s,
                        %(position)s,
                        %(yards)s,
                        %(tds)s
                    )
            """
        else:
            query = """
                INSERT INTO players_defense
                (
                        team_name,
                        tackles,
                        ints
                    )
                VALUES
                    (
                        %(team_name)s,
                        %(tackles)s,
                        %(ints)s
                    )
            """
        player_id = MySQLConnection(cls.db).query_db(query, data)
        return player_id if player_id else None


    @classmethod
    def add_player_to_team(cls, data):
        query = """
            UPDATE %(table)s
            SET
                team_id = %(team_id)s
            WHERE 
                id = %(player_id)s
        """
        results = MySQLConnection(cls.db).query_db(query, data)
        return results[0] if results[0] else None


    @classmethod
    def remove_player_from_team(cls, data):
        query = """
            DELETE FROM  %(table)s
            WHERE
                id = %(player_id)s
        """
        
        removed_player_id = MySQLConnection(cls.db).query_db(query, data)

        return removed_player_id if removed_player_id else None