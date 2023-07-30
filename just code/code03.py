# Tic-Tac-Toe

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_draw(board):
    return " " not in board

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == " ":
                return move - 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def play_game():
    board = [" "] * 9
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)

        player = players[turn]
        move = get_player_move(board, player)

        board[move] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        turn = 1 - turn

if __name__ == "__main__":
    play_game()