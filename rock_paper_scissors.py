import random


def play():
    user = input(
        "Pick your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie, a tie, no one wins \n'
    elif is_win(user, computer):
        return 'You da champ! \n'
    else:
        return 'You lost, give me a quarter \n'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

while True:
    print(play())
    cont = input("Do you wish to continue: (Y/N)").lower()
    if cont != 'y':
        break       

#  def is_loss(player, opponent):
#      if (player == 'r' and opponent == 'p') or (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's' ):     
#      return 'loss'  
