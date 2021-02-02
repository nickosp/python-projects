import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} '))
        if guess < random_number:
            print('Sorry you are a bigtime disappointment. too low')
        elif guess > random_number:
                print('Sorry but you a bum today. too high')


    print (f'Yay, you crushed it. The number is {random_number}. The Champ is here. The champ is you kid! ')            
guess(10)