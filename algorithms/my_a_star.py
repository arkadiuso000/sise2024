import sys
sys.path.append('../working_functions')
import my_functions as mf
import my_metrics
import heapq


def find_index_of_element(arr, element):
    for i in range(len(arr)):
        if arr[i].board == element.board:
            return i
    return -1


def a_star(start_board, metric):
    rows = columns = len(start_board.board)
    priority_queue = []
    visited_elements = set()
    # setting the cost of the start_board
    start_board.cost = 0
    # adding first element to the heap
    heapq.heappush(priority_queue, start_board)
    # algorithm main loop
    while len(priority_queue) != 0:
        current_element = heapq.heappop(priority_queue)
        # we use lazy remove, so this loop i necessary to check if our current_element is active
        while current_element.heap_activity != True:
            # if priority_queue is empty return False
            if len(priority_queue) == 0:
                return False
            current_element = heapq.heappop(priority_queue)

        # check if current_element is our goal
        if mf.is_goal(current_element.board):
            return True, current_element.history, len(current_element.history.split('-'))
        # adding next element to the visited elements
        visited_elements.add(current_element)
        # generating neighbours
        neighbors_current_element = mf.generate_neighbours(current_element.board, rows, columns, "LRUD",
                                                           current_element.history)
        for neighbor in neighbors_current_element:
            if neighbor not in visited_elements:
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
    return False

# test
# board = mf.import_board("../boards_files/4x4G7/4x4_07_00001.txt")
# result, history, ilosc_krokow = a_star(board, my_metrics.haming_metric)
# print("liczba krokow: {}".format(ilosc_krokow))
# print("sciezka:")
# print(history)
