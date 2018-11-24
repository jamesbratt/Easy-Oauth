""" Twitter """

import requests
from integrations.utils import generate_url
from .forms import TwitterForm

TWITTER_OAUTH_REQUEST_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_AUTH_URL = 'https://api.twitter.com/oauth/authorize'
TWITTER_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'

class Twitter:
    """ Authentication with Twitter """

    def __init__(self, fields):
        """ Set instance parameters """
        self.oauth_consumer_key = fields.oauth_consumer_key
        self.redirect_uri = fields.callbackUrl

    def get_form(self):
        return TwitterForm

    def get_auth_url(self):
        """ Get the authentication url for redirection """

        payload = {
            'oauth_consumer_key': self.oauth_consumer_key,
            'oauth_callback': self.redirect_uri,
        }
        response = requests.post(TWITTER_OAUTH_REQUEST_URL, verify=False, data=payload)
        if response.status_code is not 200:
            raise ValueError(response.json())

        params = [
            ('oauth_token', ''),
            ('oauth_verifier', ''),
        ]
        return generate_url(TWITTER_AUTH_URL, params)

    def get_auth_response(self, params):
        """ Get the authentication token """
        payload = {
            'oauth_consumer_key': self.oauth_consumer_key,
            'oauth_token':params.get('oauth_token', ''),
            'oauth_verifier':params.get('oauth_verifier', ''),
        }
        response = requests.post(TWITTER_TOKEN_URL, verify=False, data=payload)
        if response.status_code is not 200:
            raise ValueError(response.json())
        return response.json()
