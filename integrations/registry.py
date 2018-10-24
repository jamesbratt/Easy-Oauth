""" Registry for integration classes """

REGISTRY = {}

def add_integration_to_registry(integration):
    """ Add an integration class to the registry """
    REGISTRY[integration.__name__] = integration

def get_integration_from_registry(registration_key):
    """ Get a specific integration class to the registry """
    return REGISTRY[registration_key]
