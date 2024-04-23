import my_functions as mf


def find_positions(size, goal):
    goal_positions = {}
    for i in range(size):
        for j in range(size):
            goal_positions[goal[i][j]] = (i, j)
    return goal_positions


def calculate_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


def haming_metric(board, goal):
    size = len(board)
    error_counter = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != goal[i][j] and board[i][j] != "0":
                error_counter += 1
    return error_counter


def manhattan_metric(board, goal):
    size = len(board)
    goal_positions = find_positions(size, goal)
    error_distance = 0
    for i in range(size):
        for j in range(size):
            item = board[i][j]
            if item == "0":
                continue
            item_position = (i, j)
            goal_item_position = goal_positions[item]
            distance = calculate_distance(item_position, goal_item_position)
            error_distance += distance
    return error_distance



stan_gry = [
    ['1', '3', '4', '0'],
    ['5', '2', '7', '8'],
    ['9', '6', '10', '12'],
    ['13', '14', '11', '15']]

goal4x4 = [['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '10', '11', '12'],
           ['13', '14', '15', '0']]
print("Odległość Hamminga:", manhattan_metric(stan_gry, goal4x4))