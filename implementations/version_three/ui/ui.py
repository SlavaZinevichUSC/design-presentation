from domain import Domain
from auth.authentication import Authentication
from data.database import User
from system.registrar import Resolver


class ViewModel:
    def __init__(self, name: str):
        self.name = name

    def display(self):
        #list api of vm
        pass

    def __repr__(self):
        print(f"To see available functionality, call .display()")

class InteractionViewModel(ViewModel):
    def __init__(self, user: User):
        super().__init__('interaction_vm')
        self.user = user

    def display(self):
        print(f".update_balance(amount)\n.show_balance()")
        print(f"when done, call ui.save(this_vm)")

    def update_balance(self, amount):
        self.user.balance += amount

    def show_balance(self):
        print(f"Balance: {self.user.balance}")


class LoginViewModel(ViewModel):
    def __init__(self, authentication: Authentication):
        super().__init__('login_vm')
        self.authentication = authentication

    def display(self):
        print(f".login(username, password)\n.validate(username")

    def validate(self, username):
        return self.authentication.check_user(username)

    def login(self, username, password):
        user = self.authentication.authenticate(username, password)
        if user:
            print(f"Welcome {user.username}")
            return InteractionViewModel(user)
        else:
            print("Invalid username or password")
            return None

class ValidateViewModel(ViewModel):
    def __init__(self, authentication: Authentication):
        super().__init__('validate_vm')
        self.authentication = authentication

    def display(self):
        print(f".validate(username)")

    def validate(self, username):
        validation = self.authentication.check_user(username)
        if validation:
            print(f"Username {username} is valid")
        else:
            print(f"Username {username} is invalid")
        return validation

#Front-end
class UI(Domain):
    def __init__(self, name, resolver: Resolver):
        super().__init__(name)
        self.authentication = resolver.resolve('user_authentication')
        self.logger = resolver.resolve('logger')

    def get_login_vm(self):
        self.logger.log("get_login_vm called")
        return LoginViewModel(self.authentication)

    def get_validate_vm(self, username):
        return ValidateViewModel(self.authentication)

    def save(self, vm):
        self.logger.flush()
        self.authentication.store_user(vm.user)


