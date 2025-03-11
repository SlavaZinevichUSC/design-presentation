from domain import Domain

class Database:
    def __init__(self, name):
        self.name = name

class DatabaseGetterService:
    def __init__(self):
        pass

    def get_database(self, name):
        return None #or notimplementedexception

class DataDomain(Domain, DatabaseGetterService):
    def __init__(self, name, databases:  [Database]):
        Domain.__init__(self,name)
        DatabaseGetterService.__init__(self)
        self.databases = dict([(db.name, db) for db in databases])

    def get_database(self, name):
        return self.databases.get(name, None)


from dataclasses import dataclass
@dataclass
class User:
    id: int
    username: str
    password: str = '0000'
    balance: int = 0


class Userbase(Database):
    def __init__(self, name):
        super().__init__(name)

    def get_user(self, username):
        return User('1', 'user')

    def add_user(self, user: User):
        pass #or notimplementexception

    def update_user(self, user: User):
        pass

    def delete_user(self, id):
        pass

    #Add a simple implementation

class SimpleUserbase(Userbase):
    def __init__(self, name, users:dict[int, User] = None):
        super().__init__(name)
        self.users = users if users else {1: User(1, 'user')}

    def get_user(self, username):
        for user in self.users.values():
            if user.username == username:
                return user
        return None

    def add_user(self, user: User):
        if user.id not in self.users:
            self.users[user.id] = user
            return True
        return False

    def update_user(self, user: User):
        if user.id not in self.users:
            return False
        self.users[user.id] = user
        return True

    def delete_user(self, id):
        if id in self.users:
            del self.users[id]
            return True
        return False


