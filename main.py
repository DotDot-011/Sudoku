def can_fill(number: int, i: int, j: int, board: list):
    verti = list(map(lambda y: y[j], board))
    horizon = board[i]
    return (number not in horizon) and (number not in verti)
    
def fill_position(number: int, i: int, j: int, board: list):
    board[i][j] = number
    return board

def is_success(board: list):
    for line in board:
        for position in line:
            if(position == 0):
                return False
    
    return True

def fill_board(board: list, high: int, wide: int, i: int, j: int) -> list:
    if(i > high - 1 ):
        return board

    if(j > wide - 1):
        return fill_board(board, high, wide, i + 1, 0)

    if(board[i][j] != 0):
        return fill_board(board, high, wide, i, j + 1)

    for number in range(1, 10):
        if(can_fill(number, i, j, board)):
            new_board = fill_board(board, high, wide, i, j + 1)

            if(is_success(new_board)):
                return new_board
    
    return board

def solve_sudoku(board: list):
    high = 9
    wide = 9
    i = 0
    j = 0
    solved_board = fill_board(board, high, wide, i, j)
    return solved_board

def print_board(board: list):
    for line in board:
        for position in line:
            print(position, end = " ")
        print()

def test(board):
    print(can_fill(1, 0, 0, board))   
    print(can_fill(4, 0, 0, board))

def main():
    board = [[0,0,0, 7,4,0, 0,0,0],
            [0,2,0, 9,0,0, 0,8,0],
            [0,4,5, 1,0,6, 7,9,0],
            [0,0,8, 0,0,0, 1,3,9],
            [6,0,0, 0,0,0, 0,0,7],
            [2,9,1, 0,0,0, 6,0,0],
            [0,6,3, 2,0,7, 9,1,0],
            [0,8,0, 0,0,4, 0,7,0],
            [0,0,0, 0,3,1, 0,0,0]]

    solved_board = solve_sudoku(board.copy())
    print_board(solved_board)

main()