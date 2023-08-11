import random


def play():
    user = input(
        "What is your choice? 'r' for rock, 'p' for paper, and 's' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It was a tie!"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You won!"

    return "You lost!"


def is_win(player, opponent):
    # will return true if the player wins
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
