from domain import Domain
from data.database import Userbase, User
from system.registrar import Resolver

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
    def __init__(self, name, resolver: Resolver):
        super().__init__(name)
        self.database = resolver.resolve('database_repo').get_database('user_db')
        self.user_authentication = Authentication(self.database)

    def get_user_authentication(self):
        return self.user_authentication
