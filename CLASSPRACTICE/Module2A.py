'''
Problem Statement: Write a program in which you allow your user to guess a secret number between
 1 and 10.  For this example, set your secret number to a literal for easy testing.
 When you are done, think about how you can modify the program to allow the user to
 continue to guess until they get it right.  Also, think about how you could use conditionals
 to give them valuable feedback to reach the answer
 '''

import random
playAgain = "yes"

while playAgain == "yes":
    secretNumber = random.randint(1, 10)
    guess = None
    guessCounter = 3

    while guessCounter > 0 and guess != secretNumber:
        print(f"Guesses left : {guessCounter}")
        guess = int(input("Enter a number between 1 and 10: "))

        if guess < secretNumber:
            print("Too Low, Try Again!")
            guessCounter = guessCounter - 1

        elif guess > secretNumber:
            print("Too High, Try Again!")
            guessCounter = guessCounter - 1

        else:
            print("Congrats! You guessed the secret number!")
            playAgain = input("Would you like to play again? (yes or no): ").strip().lower()
            if playAgain == "no":
                print("Thanks for playing!")
                quit()
    if guessCounter == 0 and guess != secretNumber:
        print("Womp Womp. Sorry, you've used all your attempts. The number was", secretNumber)
        playAgain = input("Would you like to play again? (yes or no): ").strip().lower()
        if playAgain == "no":
            print("Thanks for playing!")
            quit()