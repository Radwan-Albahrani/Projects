# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # Create a variable called teams, to store teams from database.
    teams = []

    # Get filename from arguments given
    filename = sys.argv[1]

    # Load Data into "Teams" List
    teams = load(filename)

    counts = {}
    # Simulate N tournaments. Every time you get a winner, add a win count for the winner in Counts dictionary
    for i in range(N):
        winner = simulate_tournament(teams)
        # Get key if it exists, if it doesnt, initialize it to 0 then add 1 to it.
        counts[winner] = counts.get(winner, 0) + 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = int(team1["rating"])
    rating2 = int(team2["rating"])
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # Make a copy of teams in a variable called value
    value = teams

    # While value is not equal 1, simulate  a round, and return the winners of this round into value.
    while len(value) != 1:
        value = simulate_round(value)
    # Once done, sift through value and return the name of the winning team.
    return value[0]["team"]


def load(file):
    # Create variable to hold teams
    database = []

    # Open given file
    with open(file) as csvfile:
        # Start a DictReader object to read file correctly
        reader = csv.DictReader(csvfile)

        # Loop through file and add every row into database.
        for row in reader:
            database.append(row)
    # Return database
    return database


if __name__ == "__main__":
    main()
