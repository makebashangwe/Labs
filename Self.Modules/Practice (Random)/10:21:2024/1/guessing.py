import random
def newnum ():
    num = random.randint(1,10)
    print(num) #debugging
    return num
    
guess = 0
num = newnum()

playing = True


while True:
    while playing:
        while guess != num:
            while True:
                try:
                    guess = int(input("Please enter your guess (1-10): "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            if guess < num:
                print("Too low.")
            elif guess > num:
                print("Too  high!")
            elif guess == num:
                print("You've guessed correctly!")
                break
        playAgain = input("Would you like to play again? (Y/N)")
        if playAgain == "Y":
            playing = True
            num = newnum()
        if playAgain == "N":
            print("Thanks for playing!")
            playing = False
            quit()
            break
