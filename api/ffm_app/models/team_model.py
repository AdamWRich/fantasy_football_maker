from ffm_app import app
from ffm_app.models.base_models import BaseModel
# from api.models.player_model import PlayerModel
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

    basic_joins = """
        LEFT JOIN users ON users.id = teams.user_id
    """

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user = UserModel.get_by_id(data['user_id'])
        self.players = None

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
        print("HERE!")
        new_team_id = MySQLConnection(cls.db).query_db(query, new_team)
        

        return None if not new_team_id else cls.get_by_id(new_team_id)

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
