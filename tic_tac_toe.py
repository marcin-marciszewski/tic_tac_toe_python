game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def display_board(board):


    grid = [f'     |     |     \n  {board[1]}  |  {board[2]}  |  {board[3]}  \n     |     |     \n_________________\n     |     |     \n  {board[4]}  |  {board[5]}  |  {board[6]}  \n     |     |     \n_________________\n     |     |     \n  {board[7]}  |  {board[8]}  |  {board[9]}  \n     |     |     \n']

    print(grid[0])


display_board(game_board)
