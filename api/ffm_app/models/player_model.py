from ffm_app import app
from ffm_app.models.base_models import BaseModel
# from api.models.player_model import PlayerModel
from ffm_app.models.user_model import UserModel
from ffm_app.config.connecttoMySQL import MySQLConnection



class PlayerModel(BaseModel):
    def __init__(self, data):
        self.team_id = None

    @classmethod
    def create_player_object(cls, data):
        if data['position'] != "DEF":
            query = """
                INSERT INTO {table}
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
                INSERT INTO {table}
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
        return player_id

    @classmethod
    def add_player_to_team(cls, data, table):
        query_table = table
        query = """
            UPDATE {query_table}
            SET
                team_id = %(team_id)s
            WHERE 
                id = %(player_id)s
        """
        results = MySQLConnection(cls.db).query_db(query, data)
        return results[0]

    @classmethod
    def remove_player_from_team(cls, data):
        query = """
            UPDATE {table}
            SET
                team_id = None
            WHERE
                id = %(player_id)s
        """
        
        removed_player_id = MySQLConnection(cls.db).query_db(query, data)

        return cls.get_by_id(data['player_id']) if removed_player_id else None