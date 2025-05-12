#!/usr/bin/python3
def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Don't print the divider after the last row
            print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    
    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Invalid input! Please enter a number from {min(valid_range)} to {max(valid_range)}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Enter row and column numbers (0-2) to place your mark.")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        # Get valid row and column inputs
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {current_player}: ", [0, 1, 2])
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {current_player}: ", [0, 1, 2])
        
        # Check if the selected position is empty
        if board[row][col] == " ":
            board[row][col] = current_player
            
            # Check if the current player won
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            # Check if the board is full (tie)
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            # Switch players
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
