# Function to display the board (clean format)
def display_board(board):
    print("\n   0   1   2")
    print("  -----------")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(f" {board[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("  -----------")


# Function to check winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# Main game function
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for move in range(9):
        print(f"\nPlayer {current_player}'s turn")
        display_board(board)

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        # Input validation
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid position! Choose values between 0 and 2.")
            continue

        # Check if cell is empty
        if board[row][col] != " ":
            print("Cell already occupied! Try again.")
            continue

        # Place move
        board[row][col] = current_player

        # Check winner
        if check_winner(board, current_player):
            display_board(board)
            print(f"\n🎉 Player {current_player} wins!")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    # Draw condition
    display_board(board)
    print("\nIt's a draw!")


# Run the game
tic_tac_toe()

