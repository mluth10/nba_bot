from TripleDouble import TripleDouble
from DameTime import DameTime

class Player:
    def __init__(self, home, player_id, board, box):
        self.player_id = player_id
        self.box = box
        self.board = board
        self.home = home

        self.tracker = {}
        self.tracker['triple_double'] = False
        self.tracker['dame_time'] = False

        self.occurrences = {}
        self.occurrences['triple_double'] = TripleDouble()
        self.occurrences['dame_time'] = DameTime()
    
    def update(self, new_board, new_box):
        self.board = new_board
        self.box = new_box
    
    def check(self):
        for key, value in self.tracker.items():
            if not value:
                self.tracker[key] = self.occurrences[key].check(self.home, self.player_id, self.board, self.box)