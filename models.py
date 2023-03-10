from flask_login import UserMixin
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
# from main import db

class User(UserMixin):
    def __init__(self, id, login, email):
         self.id = id
         self.login = login
         self.email = email
         self.team_value = 0
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password, cursor):
        cursor.execute('select password from users where id = (?)', [self.id])
        hashed_password = cursor.fetchone()[0]
        return check_password_hash(hashed_password,password)
    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
         return self.id

# class User(UserMixin):
#   id = ''
# #   id = db.Column(db.Integer, primary_key=True)
# #   username = db.Column(db.String(50), index=True, unique=True)
# #   email = db.Column(db.String(150), unique = True, index = True)
# #   password_hash = db.Column(db.String(150))
# #   joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)
#     # access = db.Column(db.Integer) 0-user, 1-dev, 2-admin
#     #available_money


class Player():
    id = ''
    name = ''
    surname = ''
    goals = 0
    assists = 0
    clean_sheets = 0
    yellow_cards = 0
    red_cards = 0
    minutes = 0
    total_points = 0
    value = 0
