from .registry import addIntegrationToRegistry
from .utils import generateUrl

STRAVA_AUTH_URL = 'https://www.strava.com/oauth/authorize'

class Strava:
    """ Authentication with Strava """

    def __init__(self, fields):
        """ Set instance parameters """
        self.client_id = fields.client_id
        self.redirect_uri = fields.callbackUrl
        self.response_type = 'code'
        self.approval_prompt = 'force'
        self.scope = fields.scope
        self.state = fields.state

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
        return generateUrl(STRAVA_AUTH_URL, params)

addIntegrationToRegistry(Strava)
