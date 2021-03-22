import random


def play():
    """
    This is the basic Rock Scizzors and Paper game and has simple rules defined in the readme file!
    Here we are implementing it against the computer

    :return:
    """
    user = input("Enter 'R' for Rock, 'S' for Scissors & 'P' for Paper:\n").upper()
    computer = random.choice(['R', 'S', 'P'])
    # Check for Tie
    if computer == user:
        return "It's a tie!"
    # Check for winner
    if is_win(user, computer):
        return "You Won"
    # Check blank entry
    if user == '':
        return "Can't be blank; Try Again!"
    # Check for any other invalid entry
    if (user != 'R') and (user != 'P') and (user != 'S'):
        return "Invalid Entry! Please Try Again!"
    # Other wise
    return "You Lost!"


def is_win(player, opponent):

    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or\
            (player == 'P' and opponent == 'R'):
        return True


while True:
    # If you want to play on and on

    print(play())