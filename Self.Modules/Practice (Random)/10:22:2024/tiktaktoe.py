
width = 3
height = 3

board = []

for i in range(height):
    board.append(['-']* width)

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

print_board(board)
playing = True

def check_winner(board):
    # Check horizontal wins
    for row in board:
        if row[0] == row[1] == row[2] != '-':
            return row[0]  # Return the winning symbol (X or O)

    # Check vertical wins
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '-':
            return board[0][col]  # Return the winning symbol (X or O)

    # Check diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]  # Main diagonal (top-left to bottom-right)
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]  # Anti-diagonal (top-right to bottom-left)

    return None  # No winner yet

while playing:
    print("Format: only numbers (0-2), in format (x,y)")
    while True:
        try:
            player1 = input("Player 1 coordinates: ").strip('()').split(',')
            p1_coordinates = list(map(int,player1))
            break
        except ValueError:
            print("Try again, invalid input.")
    if p1_coordinates[0]<3 and p1_coordinates[1]<3:
        if board[p1_coordinates[0]][p1_coordinates[1]] == '-':
            board[p1_coordinates[0]][p1_coordinates[1]] = 'X'
        else: 
            print("Cell is occupied already.")
    else: 
        print("Invalid Input, try again.")

    print_board(board)
    while True:
        try:
            player2 = input("Player 2 coordinates (x,y): ").strip('()').split(',')
            p2_coordinates = list(map(int,player2))
            break
        except ValueError:
            print("Invalid Input, try again.")
    if p2_coordinates[0]<3 and p2_coordinates[1]<3:
        if board[p2_coordinates[0]][p2_coordinates[1]] == '-':
            board[p2_coordinates[0]][p2_coordinates[1]] = 'O'
        else: 
            print("Cell is occupied already.")
    else: 
        print("Invalid input.")

    print_board(board)
    win = check_winner(board)
    if win == 'X':
        print(f"You win: Player 1, {check_winner(board)}!")
        playing = False
    elif win == 'O':
        print(f"You win: Player 2, {check_winner(board)}!")
        playing = False
    else:
        continue
playAgain = input("Would you like to play again? (Y/N)").upper()
if playAgain == 'Y':
    playing = True
else:
    print("Thanks for playing.")
    quit()