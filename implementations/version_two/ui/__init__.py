from ui.ui import UI

def initialize_ui(registrar, resolver):
    ui = UI(name='ui', resolver=resolver)
    registrar.register(name='ui', entity=ui)
    return ui