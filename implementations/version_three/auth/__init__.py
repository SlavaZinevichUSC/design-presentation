from auth.authentication import AuthenticationDomain


def initialize_auth_domain(registrar, resolver):
    authentication_domain = AuthenticationDomain(name = 'authentication', resolver = resolver)
    registrar.register(name = 'domain_auth', entity = authentication_domain)
    registrar.register(name = 'user_authentication', entity = authentication_domain.get_user_authentication())
    return authentication_domain
