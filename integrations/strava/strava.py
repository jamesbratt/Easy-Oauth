""" Strava """

import requests
from integrations.registry import add_integration_to_registry
from integrations.utils import generate_url
from .forms import StravaForm

STRAVA_AUTH_URL = 'https://www.strava.com/oauth/authorize'
STRAVA_TOKEN_URL = 'https://www.strava.com/oauth/token'

class Strava:
    """ Authentication with Strava """

    FORM_FIELDS = ['title', 'secret', 'client_id', 'callbackUrl', 'scope', 'state']

    def __init__(self, fields):
        """ Set instance parameters """
        self.client_id = fields.client_id
        self.secret = fields.secret
        self.redirect_uri = fields.callbackUrl
        self.response_type = 'code'
        self.approval_prompt = 'force'
        self.scope = fields.scope
        self.state = fields.state

    def get_form(self):
        return StravaForm

    def get_auth_url(self):
        """ Get the authentication url for redirection """
        params = [
            ('client_id', self.client_id),
            ('redirect_uri', self.redirect_uri),
            ('response_type', self.response_type),
            ('approval_prompt', self.approval_prompt),
            ('scope', self.scope),
            ('state', self.state),
        ]
        return generate_url(STRAVA_AUTH_URL, params)

    def get_auth_response(self, params):
        """ Get the authentication token """
        payload = {
            'client_id': self.client_id,
            'client_secret': self.secret,
            'code':params.get('code', ''),
        }
        response = requests.post(STRAVA_TOKEN_URL, verify=False, data=payload)
        if response.status_code is not 200:
            raise ValueError(response.json())
        return response.json()

add_integration_to_registry(Strava)
