# pylint: disable=too-many-public-methods
class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self._reader.read_players()
        players = [player for player in players if player.nationality == nationality]
        return sorted(players, key=lambda player: player.points, reverse=True)

    def top_scorers_by_team(self, team):
        players = self._reader.read_players()
        players = [player for player in players if player.team == team]
        return sorted(players, key=lambda player: player.points, reverse=True)

    def top_goal_scorers(self, how_many):
        players = self._reader.read_players()
        return sorted(players, key=lambda player: player.goals, reverse=True)[:how_many]
