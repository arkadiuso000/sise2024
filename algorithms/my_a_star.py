import sys
sys.path.append('../working_functions')
import my_functions as mf
import my_metrics
import heapq
import time

def find_index_of_element(arr, element):
    for i in range(len(arr)):
        if arr[i].board == element.board:
            return i
    return -1


def a_star(start_board, metric):
    start = time.perf_counter()
    rows = columns = len(start_board.board)
    priority_queue = []
    visited_elements = set()
    # setting the cost of the start_board
    start_board.cost = 0
    # adding first element to the heap
    heapq.heappush(priority_queue, start_board)
    # for stats purpose
    my_max_depth = 0
    # algorithm main loop
    while len(priority_queue) != 0:
        current_element = heapq.heappop(priority_queue)
        depth = current_element.depth
        # for stats purpose
        if depth > my_max_depth:
            my_max_depth = current_element.depth
        # we use lazy remove, so this loop i necessary to check if our current_element is active
        while current_element.heap_activity != True:
            # if priority_queue is empty return False
            if len(priority_queue) == 0:
                end = time.perf_counter()
                my_time = end - start
                return False
            current_element = heapq.heappop(priority_queue)
        # check if current_element is our goal
        if mf.is_goal(current_element.board):
            # true, path, len of path, visited elements, processed elements, max depth, time
            end = time.perf_counter()
            my_time = end - start
            return True, current_element.history, len(current_element.history), len(visited_elements), len(priority_queue), my_max_depth, my_time
        # adding next element to the visited elements
        visited_elements.add(current_element)
        # generating neighbours
        neighbors_current_element = mf.generate_neighbours(current_element.board, rows, columns, "LRUD",
                                                           current_element.history)
        for neighbor in neighbors_current_element:
            if neighbor not in visited_elements:
                # for stats purpose
                neighbor.depth = (depth + 1)
                # calculating the cost of the neighbor
                cost = metric(neighbor.board)
                index_of_element = find_index_of_element(priority_queue, neighbor)
                # if neighbour doesn't exist in priority_queue...
                if index_of_element == -1:
                    neighbor.cost = cost
                    # adding next element to the heap
                    heapq.heappush(priority_queue, neighbor)
                else:
                    # if the neighbor is already in the heap
                    # we check his cost and if it's higher
                    if priority_queue[index_of_element].cost > cost:
                        # we swap him in 'lazy' way
                        priority_queue[index_of_element].heap_activity = False
                        neighbor.cost = cost
                        neighbor.heap_activity = True
                        heapq.heappush(priority_queue, neighbor)
    end = time.perf_counter()
    my_time = end - start
    return False

# test
board = mf.import_board("../boards_files/4x4G7/4x4_07_00135.txt")
result = a_star(board, my_metrics.haming_metric)
print("liczba krokow: {}\nsciezka: {}\nstany odwiedzone: {}\nstany przetworzone: {}\nmaksymalna glebokosc rekursji: {}\nczas: {}".format(result[2],result[1],result[3],result[4],result[5], result[6]))
