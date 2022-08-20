from api import app
from api.models.base_models import BaseModel
# from api.models.player_model import PlayerModel
from api.models.user_model import UserModel
from api.config import MySQLConnection

class TeamModel(BaseModel):

    table = "teams"
    json_fields = ['id', 'name', 'user_id']

    basic_select = """
        teams.id AS id,
        name

        users.id AS user_id
    """

    basic_joins = """
        LEFT JOIN users ON users.id = teams.user_id
    """

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user = UserModel({
            'id': data['id'],
            'username': data['username'], 
            'email': data['email'],
            'password': data['password'],
            'team_id': data['team_id']
        })
        self.players = None

    @classmethod
    def add(cls, new_team):

        query = """
            INSERT INTO teams
                (
                    name
                    users_id
                )
            VALUES
                (
                    %(name)s
                    %(user_id)s
                )
        """

        new_team_id = MySQLConnection(cls.db).query_db(query, {
            'name': new_team['name'],
            'user_id':new_team['user_id']
        })

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

        team_id = MySQLConnection(cls.db).query_db(query, {
            'name':update_data['name'],
            'id': update_data['team_id']
        })

        return cls.get_by_id(update_data['team_id']) if team_id else None
