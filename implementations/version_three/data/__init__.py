from data.database import SimpleUserbase, DataDomain, DatabaseGetterService


def initialize_data_domain(registrar, resolver):
    data_domain = DataDomain(name = 'data_domain', databases = [SimpleUserbase(name = 'user_db')])
    registrar.register('domain_data', data_domain)
    registrar.register('database_repo', data_domain)
    return data_domain

