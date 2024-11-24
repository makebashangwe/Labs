''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Assignment3B
'''

def playAgain():
    playAgainInput = input("Would you like to play again? (yes/no): ").lower()

    if playAgainInput == "yes":
        return True  # Continue playing
    elif playAgainInput == "no":
        print("Thank you for playing!")
        return False  # Stop the game
    else:
        print("Invalid input, please enter 'yes' or 'no'.")
        return playAgain()

gameLoop = True

while gameLoop:
    direction = input("You're in the forest. Please chose a direction to move in (north, south, east, west): ").lower()

    match direction:
        case "north":
            action = input(
                f"You move {direction} and find a river. What will you do next? Swim/Build a Raft?: ").lower()
            if "swim" in action:
                print("You swim across the river and find a hidden treasure.")

            elif "build" in action:
                print("You made it to the other side and reunited with your long lost dog, Buddy.")

            else:
                input("Nothing happened. You didn't follow instructions.")

        case "south":
            action = input(
                f"You move {direction} and find a river. What will you do next? Climb a tree/ Walk deeper into the forest?: ").lower()
            if "climb" in action:
                print("You fall and break your leg, causing you to perish from blood loss.")

            elif "walk" in action:
                print("You got lost and went back to your survival roots. You were never seen again.")

            else:
                input("Nothing happened. You didn't follow instructions.")

        case "east":
            action = input(
                f"You move {direction} and find a river. What will you do next? Climb the Mountain or Go Around It?: ")
            if "climb" in action:
                print("Your leg slips and you fall and hit your head hard on sharp rocks in the river.")

            elif "go" in action:
                print("You went around and died of hunger because you can't fish.")

            else:
                input("Nothing happened. You didn't follow instructions.")

        case "west":
            action = input(
                f"You move {direction} and find a river. What will you do next? Enter the Cave or Walk Past It?: ")
            if "enter" in action:
                print("You enter the cave and find treasure and a sleeping dragon.")

            elif "walk" in action:
                print("You walk past it and catch up with a group of hikers who can guide you back home.")

            else:
                input("Nothing happened. You didn't follow instructions.")

        case _:
            input("Nothing happened. You didn't follow instructions.")

    gameLoop = playAgain()
