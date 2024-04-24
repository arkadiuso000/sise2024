from working_functions import my_functions as mf
from collections import deque


def bfs(start_board, directions):
    rows = columns = len(start_board.board)
    # check if start_board is our goal
    if mf.is_goal(start_board.board):
        return True, start_board.history
    # deque and set initialization
    queue = deque()
    visited_elements = set()
    # adding first element to the queue
    queue.append(start_board)
    # adding first element to the visited elements
    visited_elements.add(start_board)
    # algorithm main loop
    while len(queue) != 0:
        current_element = queue.popleft()
        # generating neighbours
        neighbors_current_element = mf.generate_neighbours(current_element.board, rows, columns, directions,
                                                           current_element.history)
        for neighbor in neighbors_current_element:
            if neighbor not in visited_elements:
                # check if neighbor is our goal
                if mf.is_goal(neighbor.board):
                    return True, neighbor.history, len(neighbor.history.split('-'))
                # adding next element to the queue
                queue.append(neighbor)
                # adding next element to the visited elements
                visited_elements.add(neighbor)
    return False


# test
board = mf.import_board("../boards_files/4x4G7/4x4_03_00002.txt")
print(type(board.board[0][0]))
result, history, ilosc_krokow = bfs(board, "LUDR")
print("liczba krokow: {}".format(ilosc_krokow))
print("sciezka:")
print(history)
