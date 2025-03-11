from domain import Domain
from data.database import Userbase, User

class Authentication:
    def __init__(self, database: Userbase):
        self.database = database

    def check_user(self, username):
        return self.database.get_user(username) is not None

    def authenticate(self, username, password):
        user = self.database.get_user(username)
        if user and user.password == password:
            return user
        return None

    def store_user(self, user: User):
        return self.database.add_user(user)
class AuthenticationDomain(Domain):
    def __init__(self, name, database: Userbase):
        super().__init__(name)
        self.database = database

    def get_user_authentication(self):
        return Authentication(self.database)
