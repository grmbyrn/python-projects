import random


def play():
    user = input("R for Rock, P for Paper or S for Scissors.\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Tie game'

    if is_win(user, computer):
        return 'You won!'

    return 'The computer won!'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
