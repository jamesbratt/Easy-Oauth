REGISTRY = {}

def addIntegrationToRegistry(integration):
    REGISTRY[integration.__name__] = integration
    return

def getIntegrationFromRegistry(registrationKey):
    return REGISTRY[registrationKey]
