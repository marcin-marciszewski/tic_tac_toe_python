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


    grid = [f'     |     |     \n  {board[1]}  |  {board[2]}  |  {board[3]}  \n     |     |     \n_________________\n     |     |     \n  {board[4]}  |  {board[5]}  |  {board[6]}  \n     |     |     \n_________________\n     |     |     \n  {board[7]}  |  {board[8]}  |  {board[9]}  \n     |     |     \n']
    print(grid[0])


display_board(game_board)
