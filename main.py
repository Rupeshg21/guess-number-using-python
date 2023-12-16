import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input('enter a random number :'))
        if guess<random_number:
            print('sorry guess again.. its too low')
        elif guess>random_number:
            print('sorry guess again.. its too high')
    print('you have guessed the number correctly!!!')

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        guess=random.randint(low,high)
        feedback=input(f'is {guess} too high (h) , too low (l) or correct (c)?:')
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print('you have guessed correctly')
computer_guess(55)
