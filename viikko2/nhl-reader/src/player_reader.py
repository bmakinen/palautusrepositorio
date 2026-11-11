import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def read_players(self):
        response = requests.get(self.url, timeout=10).json()
        players = [
            Player(player_dict)
            for player_dict in response]
        return players
