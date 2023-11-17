
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None

game_Still_on = True


# print the game board
def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "       1 | 2 | 3")
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5] + "       4 | 5 | 6")
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "       7 | 8 | 9")
    print("\n")
# print_board(board)


# Take player input
def player_input(board):
    choice = int(input(f"It's {current_player}'s turn. Choose your spot 1-9: "))
    if 1 <= choice <= 9 and board[choice - 1] == "-":
        board[choice-1] = current_player

    elif choice > 9:
        print("Oops🤭! You're out of range. Choose a spot from 1-9")

    elif board[choice - 1] != "-":
        print("Oops🤭! Player already in that spot")


# Check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        # set winner equal to any in the three spots
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[4]
        return True

    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = board[8]
        return True


def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        # set winner equal to any in the three spots
        winner = board[3]
        return True

    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[7]
        return True

    elif board[2] == board[5] == board[8] and board[8] != "-":
        winner = board[8]
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[4]
        return True


def check_tie(board):
    global game_Still_on
    if "-" not in board:
        print_board(board)
        print("It's a tie 🤝 ")
        game_Still_on = False


def check_win():
    if check_diagonal(board) or check_vertical(board) or check_horizontal(board):
        print(f"The winner is {winner} 🎊✨")


# Switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


while game_Still_on:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
