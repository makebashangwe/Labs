'''
Makeba Waddy
Assignment 6B: Dungeon Treasure Map
10/22/2024
CSE 1321L
'''
from termcolor import colored #for fun colors :)
import random # for random number generation

'''
width = 5 #debugging
height = 5 #debugging

'''
while True:
    try:
        width = int(input("Please enter the desired width: "))
        height = int(input("Please enter the desired height: "))
        break #ext if valid
    except ValueError:
        print(colored("Please enter a number. ", "red"))    

#the answer board
board = [] #Create a list called board, each cell will represent a row of the grid. 
             #In the first cell of the board list, you’ll place a list. 
numberOfUndiscoveredTreasures = 0 # Keep track of how many treasures you are adding to the board in a separate variable called numberOfUndiscoveredTreasures.

for i in range(height):
    board.append([]) # Repeat step (a) until you have a list that is the height the user asked for in step 1
    for j in range(width):
        random_float = random.random() ## a. Pick a random number between 0 and 1.
        if random_float >= 0.7:
            board[i].append('T') # If the number is greater than or equal to 0.7 you’ll add a Treasure ‘T’ to the next cell of the list.
            numberOfUndiscoveredTreasures += 1
        else: #  If the number is less than 0.7 you’ll add an open ‘O’ to the next cell of the list.
            board[i].append('O')

def print_board(board):
    print(colored("Here are the answers: \n", "green"))

    for row in board:
        print(' '.join(row))

#display board
display_board = [] #Create a list called board, each cell will represent a row of the grid. 
             #In the first cell of the board list, you’ll place a list. 

for i in range(height):
    display_board.append([]) # Repeat step (a) until you have a list that is the height the user asked for in step 1
    for j in range(width):
        display_board[i].append(colored('O',"blue"))
        
def print_display_board(display_board):
    for row in display_board:
        print(' '.join(row))
    

#print_board(board) ---> debugging statement for answers
print()
print_display_board(display_board)#actual game board


#game
print(f"There are {numberOfUndiscoveredTreasures} hidden Treasures!")

discovered_treasures = 0

while numberOfUndiscoveredTreasures != discovered_treasures:
    guess_row = input(f"Enter row to check (0, {width-1}): ")
    guess_column = input(f"Enter column to check (0, {height-1}): ")

    try:
        guess_column = int(guess_column)
        guess_row = int(guess_row)
        
        if guess_row < 0 or guess_row >= height or guess_column < 0 or guess_column >= width:
            print("Out of bounds. Try again.")
            continue
            
    except ValueError:
        print("Please enter a number!")
        continue

    if board[guess_row][guess_column] == 'T':
        print(f"You found a treasure at {guess_row,guess_column}!")
        discovered_treasures +=1
        board[guess_row][guess_column] = 'X'
        display_board[guess_row][guess_column] = colored('X', 'green')

    elif board[guess_row][guess_column] == 'O':
        print(f"No treasure found at {guess_row,guess_column}. \n Try again.")
        board[guess_row][guess_column] = 'X'
        display_board[guess_row][guess_column] = colored('X', 'red')

    print_display_board(display_board)

print(colored("Congratulations! You've found all the treasures!! ", "yellow"))
print()
print(print_board(board))


