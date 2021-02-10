import random


def play():
    user = input(
        "Pick your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie, a tie, no one wins'
    if is_win(user, computer):
        return 'You da champ!'

    return 'You lost, give me a quarter'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return 'true'
print(play())    

#  def is_loss(player, opponent):
#      if (player == 'r' and opponent == 'p') or (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's' ):     
#      return 'loss'  
