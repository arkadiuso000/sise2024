import my_functions as mf
from collections import deque

def bfs(start_board, directions):
    rows = columns = len(start_board.board)
    # history tracks the trace of the algorithm
    history = []
    # check if start_board is our goal
    if mf.is_goal(start_board.board, rows):
        return True, start_board
    # deque and set initialization
    queue = deque()
    visited_elements = set()
    # adding first element to the queue
    queue.append(start_board)
    # adding first element to the visited elements
    visited_elements.add(str(start_board))
    # algorithm main loop
    while len(queue) != 0:
        current_element = queue.popleft()
        # adding next element to the history
        history.append(current_element)
        # generating neighbours
        neighbors_current_element = mf.generate_neighbours(current_element.board, rows, columns, directions,
                                                           current_element.history)
        for neighbor in neighbors_current_element:
            if neighbor not in visited_elements:
                if mf.is_goal(neighbor.board, rows):
                    # adding last element to the history
                    history.append(neighbor)
                    return True, neighbor.history, len(neighbor.history.split('-'))
                # adding next element to the queue
                queue.append(neighbor)
                # adding next element to the visited elements
                visited_elements.add(str(neighbor))
    return False

# test
board = mf.import_board("./plansze/4x4G7/4x4_03_00002.txt")
result, history, ilosc_krokow = bfs(board, "LUDR")
print("liczba krokow: {}".format(ilosc_krokow))
print("sciezka:")
print(history)
