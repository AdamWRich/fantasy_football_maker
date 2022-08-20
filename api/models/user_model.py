from flask import flash
import re
from api import app
from flask_bcrypt import Bcrypt

from api.models.base_models import BaseModel

from api.config import MySQLConnection

bcrypt = Bcrypt(app)

class UserModel(BaseModel):

    table = "users"
    json_fields = ['id', 'email']

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self,data):
        self.id = data['id']
        
