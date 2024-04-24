class Board:
    cost = None
    heap_activity = True

    def __init__(self, plain_board, rows, columns, history, how_created):
        self.board = plain_board
        self.rows = rows
        self.columns = columns
        self.history = history
        if how_created is not None:
            if history == "":
                self.history += "{}".format(how_created)
            else:
                self.history += "-{}".format(how_created)

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
    def __str__(self):
        # this method is for debug only
        return "[Board: {}; cost: {}]".format(self.board,self.cost)