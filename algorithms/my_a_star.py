from working_functions import my_functions as mf
import heapq
import working_functions.metrics as met


def a_star(start_board, metric):
    rows = columns = len(start_board.board)
    priority_queue = []
    visited_elements = set()
    # calculating the cost to the start_board
    cost = metric(start_board)
    start_board.cost = cost
    # adding first element to the heap
    heapq.heappush(priority_queue, start_board)
    # algorithm main loop
    while len(priority_queue) != 0:
        current_element = heapq.heappop(priority_queue)
        if mf.is_goal(current_element.board):
            return True, current_element.history, len(current_element.history.split('-'))
        visited_elements.add(current_element)
        neighbors_current_element = mf.generate_neighbours(current_element.board, rows, columns, "LRUD",
                                                           current_element.history)
        for neighbor in neighbors_current_element:
            if neighbor not in visited_elements:
                cost = metric(neighbor.board)
                if neighbor not in priority_queue:
                    neighbor.cost = cost
                    heapq.heappush(priority_queue, neighbor)
                else:
                    if priority_queue[neighbor].cost > cost:
                        priority_queue[neighbor].cost = cost
    return False
