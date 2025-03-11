from infra.tools import OutputScreen, OutputScreenExclaim, OutputInterface

def initialize_infrasctructure(registrar, resolver):
    registrar.register('screen', OutputScreenExclaim())
    return