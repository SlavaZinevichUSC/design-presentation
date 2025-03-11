
class Registrar:
    def __init__(self):
        pass

    def register(self, entity_name: str, entity: object):
        pass

class Resolver:
    def __init__(self):
        pass

    def resolve(self, entity_name: str):
        pass

class RegistrarResolver(Registrar, Resolver):
    def __init__(self):
        Registrar.__init__(self)
        Resolver.__init__(self)
        self.inventory = {}

    def register(self, name: str, entity: object):
        self.inventory[name] = entity

    def resolve(self, entity_name: str):
        return self.inventory.get(entity_name, None)
