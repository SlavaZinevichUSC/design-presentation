from data.database import SimpleUserbase, DataDomain
from auth.authentication import Authentication, AuthenticationDomain
from ui.ui import UI

def build_application():
    data_domain = DataDomain(name = 'data_domain', databases = [SimpleUserbase(name = 'user_db')])
    authentication_domain = AuthenticationDomain(name = 'authentication', database = data_domain.get_database('user_db'))
    ui = UI(name = 'ui', authentication = authentication_domain.get_user_authentication())
    return ui

ui = build_application()

