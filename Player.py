class Player:
    def __init__(self, home, player_id, board, box):
        self.player_id = player_id
        self.dbox = box
        self.board = board

        self.tracker = {}
        self.tracker['triple_double'] = False

        self.occurrences = {}
        self.occurrences['triple_double'] = self.triple_double
    
    def update(self, new_board, new_box):
        self.board = new_board
        self.box = new_box
    
    def check(self, board, box):
        for key, value in self.tracker.items():
            if not value:
                self.tracker[key] = self.occurrences[key](board, box)

    def triple_double(board, box):
        # fix this dummy
        print(board + box)