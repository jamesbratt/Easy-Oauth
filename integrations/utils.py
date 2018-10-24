""" Generic utility methods for integration classes """

def generate_url(endpoint, params):
    """ Building the oauth authorisation url """
    url = endpoint
    for i, (param_key, param) in enumerate(params):
        symbol = '&'
        if i is 0:
            symbol = '?'
        url += str(symbol + param_key + '=' + param)
    return url
