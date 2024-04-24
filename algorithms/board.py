class Board:
    cost = None
    heap_activity = True
    depth = 0

    goal = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]

    def __init__(self, plain_board, rows, columns, history, how_created):
        self.board = plain_board
        self.rows = rows
        self.columns = columns
        self.history = history
        if how_created is not None:
            self.history += how_created

        if rows != 4 and columns != 4:
            goal = []
            counter = 1
            for i in range(rows):
                row = []
                for j in range(columns):
                    row.append(str(counter))
                    counter += 1
                goal.append(row)
            self.goal = goal
    def __hash__(self):
        # converts variable board to tuple to allow adding to the set
        return hash(tuple(tuple(row) for row in self.board))

    def __eq__(self, other):
        # this method is necessary for the set to compare Boards
        if isinstance(other, Board):
            return self.board == other.board
        return False

    def __lt__(self, other):
        # this method is necessary for the priority queue to compare Boards
        return self.cost < other.cost
    def __gt__(self, other):
        return self.cost > other.cost
    def __str__(self):
        # this method is for debug only
        return "[Board: {}; cost: {}]".format(self.board,self.cost)