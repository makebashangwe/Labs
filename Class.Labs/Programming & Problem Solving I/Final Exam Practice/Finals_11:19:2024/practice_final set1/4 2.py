import random

playing = True
while playing:
    guessed = False
    number = random.randint(1,10)
    print(number)
    while True:
        try:
            guess = input("Enter a number between 1 and 10 (type 'exit' to quit): ").lower()
            if guess == "exit":
                print("Goodbye.")
                quit()
            guess = int(guess)
            if 1<=guess<=10:                    
                if guess == number:
                    print("Congratulations! You guessed the number!")
                    guessed = True
                    break
                else:
                    print("Incorrect, try again.")
            else:
                print("Enter a number between 1  and 10.")
        except ValueError:
            print("Enter an integer.")
        
    playAgain = input("Play again? (Y/N): ").lower()
    if playAgain == "y":
        playing = True
    else:
        print("Goodbye")
        playing = False
        quit()