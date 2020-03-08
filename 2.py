import random
Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore


@szantilas87
szantilas87
/
tic_tac_toe_python
1
00
Code Issues 0 Pull requests 0 Actions Projects 0 Wiki Security Insights Settings
tic_tac_toe_python/tic_tac_toe.py
@szantilas87 szantilas87 Verify player's choice
3ad5a5e 2 days ago
72 lines(55 sloc)  2.6 KB

game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def display_board(board):
    def player_input():
        player1 = input("Please pick a marker 'X' or 'O':> ")
        while player1.lower() != 'o' or player1.lower() != 'x':
            if player1.lower() == 'o' or player1.lower() == 'x':
                break
            else:
                player1 = input("It has to be 'X' or 'O':> ")
        return player1.upper()

        player1 = player_input()

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

    first_player = who_first()

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

    grid = [f'     |     |     \n  {board[1]}  |  {board[2]}  |  {board[3]}  \n     |     |     \n_________________\n     |     |     \n  {board[4]}  |  {board[5]}  |  {board[6]}  \n     |     |     \n_________________\n     |     |     \n  {board[7]}  |  {board[8]}  |  {board[9]}  \n     |     |     \n']
    print(grid[0])


display_board(game_board)
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
