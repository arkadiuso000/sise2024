from working_functions import my_functions as mf

# maximum allowed depth
MAX_DEPTH = 20


# iterative DFS algorithm implementation
def dfs(start_board, directions):
    rows = columns = len(start_board.board)
    # check if start_board is our goal
    if mf.is_goal(start_board.board):
        return True, start_board.history
    # stack and set initialization
    stack = []
    visited_elements = set()
    # adding first element with its depth to the stack
    stack.append((start_board, 0))
    # algorithm main loop
    while len(stack) != 0:
        current_element, depth = stack.pop()
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
                return True, neighbor.history, len(neighbor.history.split('-'))
            if (neighbor not in visited_elements) and (neighbor not in stack):
                # adding next element to the stack
                stack.append((neighbor, depth + 1))
    return False


# test
board = mf.import_board("../boards_files/4x4G7/4x4_03_00001.txt")
result, history, ilosc_krokow = dfs(board, "LDUR")
print("liczba krokow: {}".format(ilosc_krokow))
print("sciezka:")
print(history)
