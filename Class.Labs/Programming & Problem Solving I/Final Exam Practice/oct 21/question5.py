'''
Question 2: Using a while loop, write a program that repeatedly asks the user 
to guess a secret number between 1 and 10. The loop should only stop when the 
user guesses the correct number.'''

import random
playing = True
while playing:
    guesses = 0
    guessed = False
    guess = ''
    number = random.randint(1,10)
    print(number) #debugging
    while not guessed:
        while guesses != 3:
            guess = input("Please guess a number: ").strip(' ')
            if not guess.isalpha():
                guess = int(guess)
                if guess == number:
                    guessed = True
                    break
                else:
                    print("Incorect.")
                    guesses = guesses + 1
            else:
                print("Please enter numbers only. Try again.")
        if guesses == 3 and guessed == False:
            print(f"You've used all your guesses. The number was {number}.")
            break
        if guessed == True:
            print(f"Correct! The number was {number}.")
            print(f"You used {guesses} guesses.")
    waiting = True
    while waiting:
        playAgain = input("Would you like to play again?(Y/N)").upper()
        if playAgain == "Y":
            playing = True
            waiting = False
        elif playAgain == "N":
            print("Thank you for playing!")
            playing = False
            waiting = False
        else:
            print("Incorrect Format.")
            waiting = True




