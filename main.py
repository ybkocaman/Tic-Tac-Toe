import random

# Step 1: Set up the game board
game_board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def display_board(board):
    print('\n')
    print("-------------")
    for row in board:
        print("  |  ".join(row))
        print("-------------")


def check_winner(board, player):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
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

    # If no winning conditions are met
    return False


def is_board_full(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O' or board[row][col] == 'X':
                return False
    return True


def computer_turn(board):
    # Check if the computer can win on the next move and place 'O' accordingly
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_winner(game_board, 'O'):
                    return
                board[row][col] = ' '

    # Check if the human player is about to win and block them
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_winner(board, 'X'):
                    board[row][col] = 'O'
                    return
                board[row][col] = ' '  # Reset the board

    # If no winning moves, choose a random available spot
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return


def get_player_move(board):
    user_input = input("You are 'X'. Where do you want to put a mark?  Type it in numbers as AB (A:Row, B:Column):\n")
    if game_board[int(user_input[0]) - 1][int(user_input[1]) - 1] == ' ':
        game_board[int(user_input[0]) - 1][int(user_input[1]) - 1] = 'X'
    else:
        print("This place is not empty. Try another one.")
        get_player_move(board)


display_board(game_board)


while True:
    # Human player's turn
    get_player_move(game_board)
    display_board(game_board)

    # Check for win or tie conditions
    if check_winner(game_board, 'X'):
        print("Congratulations! You win!")
        break
    if is_board_full(game_board):
        print("It's a tie!")
        break

    # Computer's turn
    computer_turn(game_board)
    display_board(game_board)

    # Check for win or tie conditions
    if check_winner(game_board, 'O'):
        print("Computer wins! Better luck next time.")
        break
    if is_board_full(game_board):
        print("It's a tie!")
        break


