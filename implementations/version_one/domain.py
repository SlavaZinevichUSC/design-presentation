#DOMAIN DRIVEN DESIGN:
#Problem: create an application that has users, each of whom has a balance that can update.

#The application will have 3 parts: Database, Authentication service, UI

class Domain:
    def __init__(self, name):
        self.name = name

    def do_something(self, *args, **kwargs):
        pass

    def __repr__(self):
        return f"<Domain: {self.name}>"
