import random
game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
# game_board = ["b", "", "O", "X", "O", "X", "O", "O", "X", "X"]
grid = [f'     |     |     \n  {game_board[1]}  |  {game_board[2]}  |  {game_board[3]}  \n     |     |     \n_________________\n     |     |     \n  {game_board[4]}  |  {game_board[5]}  |  {game_board[6]}  \n     |     |     \n_________________\n     |     |     \n  {game_board[7]}  |  {game_board[8]}  |  {game_board[9]}  \n     |     |     \n']


def display_board(board):
    current_player = 0
    end_game = False

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

    def place_marker(board, marker, position):
        board[position] = marker

    def win_check(board, mark):
        for i in range(1, len(board)):
            if (i == 1 or i == 4 or i == 7) and (board[i] == mark and board[i+1] == mark and board[i+2] == mark):
                return True
            elif (i == 1 or i == 2 or i == 3) and (board[i] == mark and board[i+3] == mark and board[i+6] == mark):
                return True
            elif (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark):
                return True
            else:
                return False

    def who_first():
        player = random.randint(1, 2)
        return player

    def is_position_taken(board, position):
        if position in range(1, 10) and (board[position] == 'X' or board[position] == 'O'):
            return 1
        else:
            return 0

    def full_board_check(board):
        for i in range(1, len(board)):
            if board[i] != "X" and board[i] != "O":
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
        print(f'Player {who_first()} starts')

        # if who_first() == 1:
        #     current_player = 1
        #     place_marker(game_board, player1, player_choice(game_board))
        #     print(game_board)
        #     current_player = player2
        #     print(current_player)
        # else:
        #     current_player = 2
        #     place_marker(game_board, player2, player_choice(game_board))
        #     print(game_board)
        #     current_player = player1
        #     print(current_player)

        while not full_board_check(game_board):
            place_marker(game_board, current_player, player_choice(game_board))
            print(f'     |     |     \n  {game_board[1]}  |  {game_board[2]}  |  {game_board[3]}  \n     |     |     \n_________________\n     |     |     \n  {game_board[4]}  |  {game_board[5]}  |  {game_board[6]}  \n     |     |     \n_________________\n     |     |     \n  {game_board[7]}  |  {game_board[8]}  |  {game_board[9]}  \n     |     |     \n')

            if current_player == player1:
                current_player = player2
            else:
                current_player = player1

        # if who_first() == 1:
        #     while not full_board_check(game_board):
        #         if full_board_check(game_board):
        #             print('end')
        #         else:
        #             place_marker(game_board, player1, player_choice(game_board))
        #             print(game_board)
        # else:
        #     while not full_board_check(game_board):
        #         if full_board_check(game_board):
        #             print('end')
        #         else:
        #             place_marker(game_board, player2, player_choice(game_board))
        #             print(game_board)

    else:
        print("Good Bye")


display_board(game_board)
