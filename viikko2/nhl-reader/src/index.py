from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def ask_for_inputs():
    season = input("Season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]: ")
    filter_type = input("Filter by [nationality/team]: ")
    value = input("Nationality [USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]: ")
    if filter_type == "team":
        value = input("Team: ")
    return season, filter_type, value


def build_table(title, players):
    table = Table(title=title)
    table.add_column("Released", justify="left", style="cyan")
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    return table


def get_players_for_filter(stats, season, filter_type, filter_value):
    if filter_type == "nationality":
        return stats.top_scorers_by_nationality(filter_value), f"Season {season} players from {filter_value}"
    return stats.players_by_team(filter_value), f"Season {season} players from {filter_value} team"


def load_stats(season):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    return PlayerStats(PlayerReader(url))


def main():
    console = Console()
    season, filter_type, filter_value = ask_for_inputs()
    stats = load_stats(season)
    players, title = get_players_for_filter(stats, season, filter_type, filter_value)
    console.print(build_table(title, players))


if __name__ == "__main__":
    main()
