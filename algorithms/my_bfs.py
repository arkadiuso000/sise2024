import my_functions as mf
from collections import deque
import time

def bfs(start_board, directions):
    start = time.perf_counter()
    rows = columns = len(start_board.board)
    # check if start_board is our goal
    if mf.is_goal(start_board.board):
        end = time.perf_counter()
        my_time = end - start
        # true, path, len of path, visited elements, processed elements, max depth, time
        return True, start_board.history, len(start_board.history), 0, 1, 0, my_time
    # deque and set initialization
    queue = deque()
    visited_elements = set()
    # adding first element to the queue
    queue.append((start_board, 0))
    # adding first element to the visited elements
    visited_elements.add(start_board)
    # for stats purpose
    my_max_depth = 0
    # algorithm main loop
    while len(queue) != 0:
        current_element, depth = queue.popleft()
        # for stats purpose
        if depth > my_max_depth:
            my_max_depth = depth
        # generating neighbours
        neighbors_current_element = mf.generate_neighbours(current_element.board, rows, columns, directions,
                                                           current_element.history)
        for neighbor in neighbors_current_element:
            if neighbor not in visited_elements:
                # check if neighbor is our goal
                if mf.is_goal(neighbor.board):
                    end = time.perf_counter()
                    my_time = end - start
                    # true, path, len of path, visited elements, processed elements, max depth, time
                    return True, neighbor.history, len(neighbor.history), len(visited_elements), len(queue), my_max_depth, my_time
                # adding next element to the queue
                queue.append((neighbor, depth + 1))
                # adding next element to the visited elements
                visited_elements.add(neighbor)
    end = time.perf_counter()
    my_time = end - start
    # false, -1, -1, visited elements, processed elements, max depth, time
    return False, -1, -1, len(visited_elements), len(queue), my_max_depth, my_time


# test
# board = mf.import_board("../boards_files/4x4G7/4x4_03_00001.txt")
# result = bfs(board, "LUDR")
# print("liczba krokow: {}\nsciezka: {}\nstany odwiedzone: {}\nstany przetworzone: {}\nmaksymalna glebokosc rekursji: {}\nczas: {}".format(result[2],result[1],result[3],result[4],result[5],result[6]))


