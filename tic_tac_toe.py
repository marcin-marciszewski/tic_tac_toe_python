import random
game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
# game_board = ["b", "", "O", "X", "O", "X", "O", "O", "X", "X"]


def display_board(board):
    print("Welcome to Tic Tac Toe!")

    def player_input():
        player1 = input("Player 1: Please pick 'X' or 'O':> ")
        while player1.lower() != 'o' or player1.lower() != 'x':
            if player1.lower() == 'o' or player1.lower() == 'x':
                break
            else:
                player1 = input("It has to be 'X' or 'O':> ")
        return player1.upper()

    player1 = player_input()

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    players = [player1, player2]
    current_player = random.choice(players)

    def player_name(player):
        if current_player == player1:
            return "Player 1"
        else:
            return "Player 2"

    def place_marker(board, marker, position):
        board[position] = marker

    def win_check(board, mark):
        for i in range(1, len(board)):
            if (i == 1 or i == 4 or i == 7) and (board[i] == mark and board[i+1] == mark and board[i+2] == mark):
                print(f'{mark} wins')
                return True
            elif (i == 1 or i == 2 or i == 3) and (board[i] == mark and board[i+3] == mark and board[i+6] == mark):
                print(f'{mark} wins')
                return True
            elif (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark):
                print(f'{mark} wins')
                return True
            else:
                return False

    def is_position_taken(board, position):
        if position in range(1, 10) and (board[position] == 'X' or board[position] == 'O'):
            return 1
        else:
            return 0

    def full_board_check(board):
        for i in range(1, len(board)):
            if board[i] != "X" or board[i] != "O":
                return False
            else:
                return True

    def player_choice(board):
        choice = int(input("Please choose a position between 1-9:> "))
        if choice in range(1, 10) and is_position_taken(board, choice) == 0:
            return choice
        else:
            while choice not in range(1, 10) or is_position_taken(board, choice) == 1:
                if choice not in range(1, 10):
                    choice = int(
                        input("Number has to be between 1-9:> "))
                elif is_position_taken(board, choice) == 1:
                    choice = int(
                        input("This number is already taken:> "))
            return choice

    start_game = input("Are you ready to start the game? Yes or No:> ")

    if start_game.lower() == 'yes':
        print(f'{player_name(current_player)} starts')
        while not full_board_check(board):
            place_marker(board, current_player, player_choice(board))
            print(f'     |     |     \n  {board[1]}  |  {board[2]}  |  {board[3]}  \n     |     |     \n_________________\n     |     |     \n  {board[4]}  |  {board[5]}  |  {board[6]}  \n     |     |     \n_________________\n     |     |     \n  {board[7]}  |  {board[8]}  |  {board[9]}  \n     |     |     \n')
            if win_check(board, current_player) != False:
                break
            elif current_player == player1:
                current_player = player2
            else:
                current_player = player1
    elif start_game.lower() == 'no':
        print('Good bye')
    else:
        start_game = input("Yes or No. Please:> ")


display_board(game_board)
