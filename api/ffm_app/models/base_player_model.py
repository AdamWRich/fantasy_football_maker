from ffm_app import app
from ffm_app.models.base_models import BaseModel
from ffm_app.models.team_model import TeamModel
from ffm_app.models.user_model import UserModel
from ffm_app.config.connecttoMySQL import MySQLConnection

class PlayerModel(BaseModel):

    table =  "players_{side}"
    json_fields = []

    # basic_select = """
    #     players_{side}.id AS id,
    #     name

    #     users.id AS user_id
    # """

    # basic_joins = """
    #     LEFT JOIN users ON users.id = teams.user_id
    # """

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.position = data['position']

    # @classmethod
    # def add(cls, new_team):

    #     query = """
    #         INSERT INTO teams
    #             (
    #                 name
    #                 users_id
    #             )
    #         VALUES
    #             (
    #                 %(name)s
    #                 %(user_id)s
    #             )
    #     """

    #     new_team_id = MySQLConnection(cls.db).query_db(query, {
    #         'name': new_team['name'],
    #         'user_id':new_team['user_id']
    #     })

    #     return None if not new_team_id else cls.get_by_id(new_team_id)

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
