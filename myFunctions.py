# noinspection PyUnboundLocalVariable,PyShadowingNames
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

def generate_neighbours(board, row, column):
    neighbours = []


# print(importBoard("./plansze/4x4G7/4x4_01_00001.txt"))

board, rows, cols = import_board("./plansze/4x4G7/4x4_01_00001.txt")
print(find_0_position(board, rows, cols))
