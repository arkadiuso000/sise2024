import my_functions as mf
import time
# maximum allowed depth
MAX_DEPTH = 20


# iterative DFS algorithm implementation
def dfs(start_board, directions):
    start = time.perf_counter()
    rows = columns = len(start_board.board)
    # check if start_board is our goal
    if mf.is_goal(start_board.board):
        end = time.perf_counter()
        my_time = end - start
        # true, path, len of path, visited elements, processed elements, max depth, time
        return True, start_board.history, len(start_board.history), 0, 1, 0, my_time
    # stack and set initialization
    stack = []
    visited_elements = set()
    # adding first element with its depth to the stack
    stack.append((start_board, 0))
    # for stats purpose
    my_max_depth = 0
    # algorithm main loop
    while len(stack) != 0:
        current_element, depth = stack.pop()
        # for stats purpose
        if depth > my_max_depth:
            my_max_depth = depth
        # check for maximum depth
        if depth > MAX_DEPTH:
            # skip this iteration
            continue
        # adding next element to the visited elements
        visited_elements.add(current_element)
        # generating neighbours
        neighbors_current_element = mf.generate_neighbours(current_element.board, rows, columns, directions,
                                                           current_element.history)
        # neighbors loop
        for neighbor in reversed(neighbors_current_element):
            # check if neighbor is our goal
            if mf.is_goal(neighbor.board):
                end = time.perf_counter()
                my_time = end - start
                # true, path, len of path, visited elements, processed elements, max depth, time
                return True, neighbor.history, len(neighbor.history), len(visited_elements), len(stack), my_max_depth, my_time
            if (neighbor not in visited_elements) and (neighbor not in stack):
                # adding next element to the stack
                stack.append((neighbor, depth + 1))
    end = time.perf_counter()
    my_time = end - start
    # false, -1, -1, visited elements, processed elements, max depth, time
    return False, -1, -1, len(visited_elements), len(stack), my_max_depth, my_time


# test
# board = mf.import_board("../boards_files/4x4G7/4x4_07_00135.txt")
# result = dfs(board, "LDUR")
# print("liczba krokow: {}\nsciezka: {}\nstany odwiedzone: {}\nstany przetworzone: {}\nmaksymalna glebokosc rekursji: {}\nczas: {}".format(result[2],result[1],result[3],result[4],result[5],result[6]))

