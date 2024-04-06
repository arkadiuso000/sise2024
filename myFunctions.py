# noinspection PyUnboundLocalVariable,PyShadowingNames
import copy


def import_board(file_name):
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("There is no such file")

    rows, columns = list(file.readline().split())
    board = []
    for i in range(int(rows)):
        board.append(file.readline().split())
    return board, int(rows), int(columns)


# noinspection PyShadowingNames
def find_0_position(board, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == "0":
                return i, j
    raise Exception("Invalid board: There is no 0 in the board")


def swap(board, zero_row, zero_column, direction):
    if direction == "L":
        temp = board[zero_row][zero_column - 1]
        board[zero_row][zero_column - 1] = "0"
        board[zero_row][zero_column] = temp

    elif direction == "R":
        temp = board[zero_row][zero_column + 1]
        board[zero_row][zero_column + 1] = "0"
        board[zero_row][zero_column] = temp

    elif direction == "U":
        temp = board[zero_row - 1][zero_column]
        board[zero_row - 1][zero_column] = "0"
        board[zero_row][zero_column] = temp

    elif direction == "D":
        temp = board[zero_row + 1][zero_column]
        board[zero_row + 1][zero_column] = "0"
        board[zero_row][zero_column] = temp

    return board


def print_board(board):
    for i in board:
        print(i)


def generate_neighbours(board, row, column, directions):
    neighbours = []
    zero_row, zero_column = find_0_position(board, row, column)

    for i in directions.upper():

        if i == "L":
            if zero_column == 0:
                continue
            else:
                neighbour_l = copy.deepcopy(board)
                neighbour_l = swap(neighbour_l, zero_row, zero_column, i)
                neighbours.append(neighbour_l)

        elif i == "R":
            if zero_column == column - 1:
                continue
            else:
                neighbour_r = copy.deepcopy(board)
                neighbour_r = swap(neighbour_r, zero_row, zero_column, i)
                neighbours.append(neighbour_r)

        elif i == "U":
            if zero_row == 0:
                continue
            else:
                neighbour_u = copy.deepcopy(board)
                neighbour_u = swap(neighbour_u, zero_row, zero_column, i)
                neighbours.append(neighbour_u)

        elif i == "D":
            if zero_row == row - 1:
                continue
            else:
                neighbour_d = copy.deepcopy(board)
                neighbour_d = swap(neighbour_d, zero_row, zero_column, i)
                neighbours.append(neighbour_d)

    return neighbours

# test
# board, rows, cols = import_board("./plansze/4x4G7/4x4_01_00002.txt")
# nei = generate_neighbours(board,rows,cols,"DURL")
