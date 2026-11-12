import unittest

from player import Player
from player_stats import PlayerStats


class StubReader:
    def __init__(self, players):
        self._players = players
        self.calls = 0

    def read_players(self):
        self.calls += 1
        return list(self._players)


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player({"name": "Aho", "nationality": "FIN", "team": "TOR", "goals": 25, "assists": 35}),
            Player({"name": "Bertuzzi", "nationality": "CAN", "team": "TOR", "goals": 18, "assists": 28}),
            Player({"name": "Crosby", "nationality": "USA", "team": "PIT", "goals": 30, "assists": 22}),
            Player({"name": "Draisaitl", "nationality": "GER", "team": "EDM", "goals": 41, "assists": 51}),
            Player({"name": "Eichel", "nationality": "USA", "team": "VGK", "goals": 27, "assists": 39}),
            Player({"name": "Fiala", "nationality": "USA", "team": "LAK", "goals": 23, "assists": 36}),
        ]
        self.reader = StubReader(self.players)
        self.stats = PlayerStats(self.reader)

    def test_top_scorers_by_nationality_returns_sorted_players(self):
        result = self.stats.top_scorers_by_nationality("USA")

        self.assertEqual([player.name for player in result], ["Eichel", "Fiala", "Crosby"])
        self.assertEqual(self.reader.calls, 1)

    def test_top_scorers_by_team_returns_sorted_players(self):
        result = self.stats.top_scorers_by_team("TOR")

        self.assertEqual([player.name for player in result], ["Aho", "Bertuzzi"])
        self.assertEqual(self.reader.calls, 1)

    def test_top_goal_scorers_returns_requested_count_in_descending_order(self):
        result = self.stats.top_goal_scorers(3)

        self.assertEqual([player.name for player in result], ["Draisaitl", "Crosby", "Eichel"])
        self.assertEqual(self.reader.calls, 1)


if __name__ == "__main__":
    unittest.main()
