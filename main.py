import random


def get_players(player_amount=2):
    """
    Get the names of all playing players.

    :param player_amount: The number of players playing.
    :rtype: list
    :return: players
    """
    if player_amount > 2:
        return
    message = "Please enter the name of player"
    players_range = range(1, player_amount + 1)
    return [input("{} {}: ".format(message, i)) for i in players_range]


def get_ladders():
    """
    Get the starting cell positions of all the ladders.

    :rtype: list
    :return: ladders
    """
    ladders = []
    for i in range(15):
        while True:
            ladder = random.randint(5, 85)
            if not(ladder in ladders or ladder + 15 == ladder):
                ladders.append(ladder)
                break
            else:
                continue
    return ladders


def get_snakes(ladders):
    """
    Get the starting cell positions of all the snakes.

    :rtype: list
    :return: snakes
    """
    snakes = []
    for i in range(10):
        while True:
            snake = random.randint(20, 95)
            if not(snake in snakes or snake - 10 == snake or snake in ladders):
                snakes.append(snake)
                break
            else:
                continue
    return snakes


def roll_dice():
    """
    Returns an integer between 1 and 6 (inclusive).

    :return: integer
    """
    return random.randint(1, 6)


def main():
    """ Starts the program. """
    players = get_players(2)
    ladders = get_ladders()
    snakes = get_snakes(ladders)

    ladders.sort()
    snakes.sort()

    print("\nList of Players: {}".format(players))
    print("Ladders' cells: {}".format(ladders))
    print("Snakes' cells: {}".format(snakes))

    positions = {player: 0 for player in players}
    winner = None

    while winner is None:
        for player in players:
            if player == players[0]:
                print()

            roll = roll_dice()
            positions[player] += roll
            print("{}'s dice roll is {} , Their new position is: {}"
                  .format(player, roll, positions[player]))

            if positions[player] > 99:
                winner = player
                break

            if positions[player] in ladders or positions[player] in snakes:
                if positions[player] in ladders:
                    message = "Great {}! It's a ladder, climb up by 15 cells."
                    positions[player] += 15
                else:
                    message = "Oops {}! You've been bitten, go down 10 cells."
                    positions[player] -= 10
                print(message.format(player) + " Your new position is {}."
                      .format(positions[player]))
            else:
                continue

    print("\nHurray! The winner is {}".format(winner))
    input("Press any key to exit.")


if __name__ == '__main__':
    main()
