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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': 
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low #could also be high b/c low = high  
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        print(f'Yay the computer got it right {guess} and will start to takeover the world now!')  

        computer_guess(1000)       