from statistics_service import StatisticsService
from player import Player


class StubReader:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


def test_search_returns_matching_player_when_name_is_a_substring():
    players = [
        Player("Semenko", "EDM", 4, 12),
        Player("Lemieux", "PIT", 45, 54),
        Player("Kurri", "EDM", 37, 53),
    ]
    stats = StatisticsService(StubReader(players))

    result = stats.search("emen")

    assert result == players[0]


def test_search_returns_none_when_no_player_matches():
    players = [
        Player("Semenko", "EDM", 4, 12),
        Player("Lemieux", "PIT", 45, 54),
    ]
    stats = StatisticsService(StubReader(players))

    result = stats.search("Gretzky")

    assert result is None


def test_team_returns_all_players_from_requested_team():
    players = [
        Player("Semenko", "EDM", 4, 12),
        Player("Lemieux", "PIT", 45, 54),
        Player("Kurri", "EDM", 37, 53),
        Player("Yzerman", "DET", 42, 56),
    ]
    stats = StatisticsService(StubReader(players))

    result = stats.team("EDM")

    assert result == [players[0], players[2]]


def test_top_returns_players_sorted_by_points_and_includes_upper_bound():
    players = [
        Player("Semenko", "EDM", 4, 12),
        Player("Lemieux", "PIT", 45, 54),
        Player("Kurri", "EDM", 37, 53),
        Player("Yzerman", "DET", 42, 56),
        Player("Gretzky", "EDM", 35, 89),
    ]
    stats = StatisticsService(StubReader(players))

    result = stats.top(3)

    assert [player.name for player in result] == ["Gretzky", "Lemieux", "Yzerman"]
