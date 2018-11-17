""" Github """

import requests
from integrations.utils import generate_url
from .forms import GithubForm

GITHUB_AUTH_URL = 'https://github.com/login/oauth/authorize'
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'

class Github:
    """ Authentication with Github """

    def __init__(self, fields):
        """ Set instance parameters """
        self.client_id = fields.client_id
        self.secret = fields.secret
        self.redirect_uri = fields.callbackUrl
        self.scope = fields.scope
        self.state = fields.state

    def get_form(self):
        return GithubForm

    def get_auth_url(self):
        """ Get the authentication url for redirection """
        params = [
            ('client_id', self.client_id),
            ('redirect_uri', self.redirect_uri),
            ('scope', self.scope),
            ('state', self.state),
        ]
        return generate_url(GITHUB_AUTH_URL, params)

    def get_auth_response(self, params):
        """ Get the authentication token """
        payload = {
            'client_id': self.client_id,
            'client_secret': self.secret,
            'code':params.get('code', ''),
        }
        response = requests.post(GITHUB_TOKEN_URL, verify=False, data=payload, headers={"Accept":"application/json"})
        if response.status_code is not 200:
            raise ValueError(response.json())
        return response.json()
