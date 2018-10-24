from .registry import addIntegrationToRegistry

class Strava:
    def __init__(self):
        print('strava init')

addIntegrationToRegistry(Strava)