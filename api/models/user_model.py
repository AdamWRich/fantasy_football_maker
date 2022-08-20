from flask import flash, session
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
    NAME_REGEX = re.comile(r'[^A-z\s\d][\\\^]?')

    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.team_id = None


    # This method uses a BaseModel method to check for / find email in users table
    @classmethod
    def get_by_email(cls, email):
        return cls.filter_one_by({'email':email})


    # This method adds user to db
    @classmethod 
    def save(cls, user):

        query = """
            INSERT INTO users
                (
                    first_name,
                    username,
                    email,
                    password
                )
            VALUES
                (
                    %(first_name)s,
                    %(username)s,
                    %(email)s,
                    %(password)s
                )
        """

        new_user_id = MySQLConnection(cls.db).query_db(query, user)
        
        return None if not new_user_id else cls.get_by_id(new_user_id)


    # This method is where user-data will be manipulated PRIOR to sending to the db (method above)
    @classmethod
    def add_user(cls, user):
        return cls.save({
            "first_name": user['first_name'],
            "username": user['username'],
            "email": user['email'],
            "password": bcrypt.generate_password_hash(user['password']),
        })

    # Log in method, checks user-inputted password against Bcrypt again.
    # Or should we log in with the username? Then users couldn't have the same username...
    @classmethod
    def login(cls, user):

        found_user = UserModel.get_by_email(user['email'])
        if found_user is not None:
            if bcrypt.check_password_hash(found_user.password, user['password']):
                session['user_id'] = found_user.id
                return found_user
        
        return None
    
    @classmethod
    def validate_registration_data(cls, user):

        errors = []

        if 'first_name' in user:
            if len(user['first_name']) <= 2:
                errors.append("First name must be more than 2 characters")

            # I added a 'no special characters' check, can remove if it doesn't work.
            if not cls.NAME_REGEX.match(user['first_name']):
                errors.append("First name cannot include any special characters")
        else:

            errors.append("First name required")

        if 'username' in user:
            if len(user['username']) <= 2:
                errors.append("Username must be more than 2 characters")

        else:
            errors.append("Username required")

        if 'email' in user:
            if UserModel.get_by_email(user['email']) is not None:
                errors.append("That email is associated with another account")

            if len(user['email']) == 0:
                errors.append("An email address is required")

            elif not cls.EMAIL_REGEX.match(user['email']):
                errors.append("Invalid email format")
        else:

            errors.append("Email required")

        return errors