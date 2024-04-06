import copy

import my_functions as mf
from collections import deque
import ast


def bfs(start_board, directions):
    rows = column = len(start_board)
    # history tracks the trace of the algorithm
    history = []

    if mf.is_goal(start_board, rows):
        return True, start_board
    queue = deque()
    visited_elements = set()
    # adding first element to the queue
    queue.append(start_board)
    # adding first element to the visited elements
    visited_elements.add(str(start_board))

    while len(queue) != 0:
        current_element = queue.popleft()

        neighbors_current_element = mf.generate_neighbours(current_element, rows, column, directions)

        for neighbor in neighbors_current_element:

            if str(neighbor) not in visited_elements:
                if mf.is_goal(neighbor, rows):
                    return True, history
                queue.append(neighbor)
                visited_elements.add(str(neighbor))

    return False


# test
board, rows, cols = mf.import_board("./plansze/4x4G7/4x4_02_00001.txt")
result, history = bfs(board, "UDLR")
print("history:")
for el in history:
    mf.print_board(board)
    print()
