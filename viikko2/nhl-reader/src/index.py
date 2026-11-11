from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


def ask_for_inputs():
    season = input("Season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]: ")
    nationality = input("Nationality [USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]: ")
    return season, nationality


def build_table(season, nationality, players):
    table = Table(title=f"Season {season} players from {nationality}")
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


def main():
    console = Console()
    season, nationality = ask_for_inputs()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)
    table = build_table(season, nationality, players)
    console.print(table)


if __name__ == "__main__":
    main()
