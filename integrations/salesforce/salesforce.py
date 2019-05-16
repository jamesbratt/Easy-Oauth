""" Salesforce """

import requests
from integrations.utils import generate_url
from .forms import SalesforceForm

SALESFORCE_AUTH_URL = 'https://login.salesforce.com/services/oauth2/authorize'
SALESFORCE_TOKEN_URL = 'https://login.salesforce.com/services/oauth2/token'

class Salesforce:
    """ Authentication with Salesforce """

    def __init__(self, fields):
        """ Set instance parameters """
        self.secret = fields.secret
        self.client_id = fields.client_id
        self.redirect_uri = fields.callbackUrl
        self.scope = fields.scope
        self.response_type = 'code'

    def get_form(self):
        return SalesforceForm

    def get_auth_url(self):
        """ Get the authentication url for redirection """
        params = [
            ('client_id', self.client_id),
            ('redirect_uri', self.redirect_uri),
            ('scope', self.scope),
            ('response_type', self.response_type)
        ]
        return generate_url(SALESFORCE_AUTH_URL, params)

    def get_auth_response(self, params):
        """ Get the authentication token """
        payload = {
            'client_id': self.client_id,
            'client_secret': self.secret,
            'code':params.get('code', ''),
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri
        }
        response = requests.post(SALESFORCE_TOKEN_URL, verify=False, data=payload, headers={"Accept":"application/json"})
        if response.status_code is not 200:
            raise ValueError(response.json())
        return response.json()
