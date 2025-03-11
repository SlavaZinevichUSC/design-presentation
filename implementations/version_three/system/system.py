from infra import initialize_infrasctructure
from data import initialize_data_domain
from auth import initialize_auth_domain
from ui import initialize_ui
from system.registrar import RegistrarResolver

def build_application():
    registrar = RegistrarResolver()
    resolver = registrar
    initialize_infrasctructure(registrar, resolver)
    data_domain = initialize_data_domain(registrar, resolver)
    authentication_domain = initialize_auth_domain(registrar, resolver)
    ui_domain = initialize_ui(registrar, resolver)
    return ui_domain

ui = build_application()