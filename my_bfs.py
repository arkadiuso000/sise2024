import my_functions as mf
from collections import deque
import ast


def bfs(start_board, directions):
    rows = column = len(start_board)
    # history tracks the trace of the algorithm
    history = [start_board]

    if mf.is_goal(start_board, rows):
        return True, history
    queue = deque()
    visited_elements = set()
    # adding first element to the queue
    queue.append(start_board)
    # adding first element to the visited elements
    visited_elements.add(str(start_board))

    # debugging purpose only
    # print("visited_elements przed petla while")
    # for el in visited_elements:
    #     lista_list = ast.literal_eval(el)
    #     mf.print_board(lista_list)
    #     print()
    # print("queue przed petla while")
    # for el in queue:
    #     mf.print_board(el)
    #     print()

    while len(queue) != 0:
        current_element = queue.popleft()
        mf.print_board(current_element)
        print()
        neighbors_current_element = mf.generate_neighbours(current_element, rows, column, directions)

        # debuging purpose only
        # print("sasiady current elementu")
        # for I in neighbors_current_element:
        #     mf.print_board(i)
        #     print()

        for neighbor in neighbors_current_element:
            history.append(neighbor)
            if str(neighbor) not in visited_elements:
                # debuging purpose only
                # print("wbijam do somsiada, o to on:")
                # mf.print_board(neighbor)
                if mf.is_goal(neighbor, rows):
                    # debuging purpose only
                    # print("VISITED ELEMENTS:")
                    # for i in visited_elements:
                    #     lista_list = ast.literal_eval(i)
                    #     mf.print_board(lista_list)
                    #     print()
                    # print("QUEUE:")
                    # for i in queue:
                    #     mf.print_board(i)
                    #     print()

                    return True, history
                queue.appendleft(neighbor)
                visited_elements.add(str(neighbor))

    return False


# test
board, rows, cols = mf.import_board("./plansze/4x4G7/4x4_02_00001.txt")
result, history = bfs(board, "UDLR")
print("history:")
for el in history:
    mf.print_board(board)
    print()
