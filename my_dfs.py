import my_functions as mf


# maximum allowed depth
MAX_DEPTH = 20
# iterative DFS algorithm implementation
def dfs(start_board, directions):
    rows = columns = len(start_board)
    # history tracks the trace of the algorithm
    history = []
    if mf.is_goal(start_board, rows):
        return True, start_board
    stack = []
    visited_elements = set()
    # adding first element with its depth to the stack
    stack.append((start_board,0))

    while len(stack) != 0:
        current_element, depth = stack.pop()
        # check for maximum depth
        if depth > MAX_DEPTH:
            # skip this iteration
            continue
        # adding next element to the history
        history.append(current_element)
        # adding next element to the visited elements
        visited_elements.add(str(current_element))
        # generating neighbours
        neighbors_current_element = mf.generate_neighbours(current_element, rows, columns, directions)
        for neighbor in reversed(neighbors_current_element):
            if mf.is_goal(neighbor, rows):
                history.append(neighbor)
                return True, history
            if (str(neighbor) not in visited_elements) and (neighbor not in stack):
                # adding next element to the stack
                stack.append((neighbor, depth + 1))
    return False, history

# test
# board, rows, cols = mf.import_board("./plansze/4x4G7/4x4_02_00001.txt")
# result, history = dfs(board, "LUDR")
# print("history:")
# counter = 1
# for el in history:
#     print("krok {}".format(counter))
#     mf.print_board(el)
#     print()
#     counter += 1