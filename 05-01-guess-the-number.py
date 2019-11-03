# a game for guessing a number

import random

num_of_chances = 5
secret_number = random.randint(1,20)
#print(secret_number)

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 0 and 20.')
print('Can you guess the number? I will give you ' + str(num_of_chances) + ' chances.')

for guessesTaken in range(num_of_chances+1):
    if guessesTaken == num_of_chances:
        print('You have run out of chances... I was thinking of the number: ' + str(secret_number))
        break

    try:
        if guessesTaken == num_of_chances-1:
            print('You have 1 guess remaining, uh oh ;-) \n')
        else:
            print('You have ' + str(num_of_chances-guessesTaken) + ' guesses remaining.\n')
        
        guess = int(input('Guess: '))
        
        if int(guess) < secret_number:
            print('Sorry, too low.')

        elif int(guess) > secret_number:
            print('Sorry, too high.')

        else:
            print('Congrats,' + name + '! That is the correct guess.')
            if guessesTaken+1 == 1:
                print('You got it in a single try!')
            else:  
                print('You got it in ' + str(guessesTaken + 1) + ' tries.')
            break

    except:
        print('You need to enter an integer ... try again.')
    



