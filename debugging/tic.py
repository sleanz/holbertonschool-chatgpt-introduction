def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if len(set(board[row][col] for row in board)) == 1 and board[0][col] != " ":
            return True

    if len(set(board[i][i] for i in range(len(board)))) == 1 and board[0][0] != " ":
        return True

    if len(set(board[i][2 - i] for i in range(len(board)))) == 1 and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    board[row][col] = player
                    if check_winner(board):
                        print_board(board)
                        print("Player " + player + " wins!")
                        break
                    elif all(all(cell != " " for cell in row) for row in board):
                        print_board(board)
                        print("It's a draw!")
                        break
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input! Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

        except TypeError:
            print("Invalid input! Please enter valid indices.")

tic_tac_toe()
