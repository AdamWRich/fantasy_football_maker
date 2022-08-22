from ffm_app import app
from ffm_app.models.base_models import BaseModel
from ffm_app.models.team_model import TeamModel
from ffm_app.models.user_model import UserModel
from ffm_app.config.connecttoMySQL import MySQLConnection

class OffensePlayerModel(BaseModel):

    table =  "players_offense"
    json_fields = ['id', 'first_name', 'last_name', 'team', 'position', 'yards', 'tds', 'team_id']

    basic_select = """
        players_offense.id AS id,
        name

        teams.id AS team_id
    """

    basic_joins = """
        LEFT JOIN users ON users.id = teams.user_id
    """

    def __init__(self, data, team_id = None):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.position = data['position']
        self.yards = data['yards']
        self.tds = data['tds']
        self.team_id = team_id


    @classmethod
    def add_player_to_team(cls, team):

        query = """
            UPDATE players_offense
                (
                    team_id
                )
            VALUES
                (
                    %(team_id)s
                )
        """

        player_team_id = MySQLConnection(cls.db).query_db(query, {
            'team_id':team['team_id']
        })

        return None if not player_team_id else cls.get_by_id(player_team_id)

    # @classmethod
    # def update(cls, update_data):

    #     query = """
    #         UPDATE teams
    #         SET
    #             name = %(name)s
    #         WHERE 
    #             id = %(id)s
    #     """

    #     team_id = MySQLConnection(cls.db).query_db(query, {
    #         'name':update_data['name'],
    #         'id': update_data['team_id']
    #     })

    #     return cls.get_by_id(update_data['team_id']) if team_id else None
