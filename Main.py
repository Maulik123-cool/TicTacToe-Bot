# Tic Tac Toe Game in Python

# Create the board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Check for a win
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check for a draw
def check_draw():
    return all(cell != " " for cell in board)

# Main game loop
def play_game():
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
            board[move] = current_player
            print_board()

            if check_win(current_player):
                print(f"Player {current_player} wins!")
                break
            elif check_draw():
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Run the game
if __name__ == "__main__":
    play_game()


def print_board():
    print()
    print(f"board ")