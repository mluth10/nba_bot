from TripleDouble import TripleDouble
from DameTime import DameTime
from Player50 import Player50
from PlayerHalf import PlayerHalf
from Util import Util

class Player:
    def __init__(self, home, player_id, board, box, util):
        self.player_id = player_id
        self.box = box
        self.board = board
        self.home = home
        self.util = util

        self.tracker = {}
        self.tracker['triple_double'] = False
        self.tracker['dame_time'] = False
        self.tracker['player_half'] = False
        self.tracker['player_50'] = False
        

        self.occurrences = {}
        self.occurrences['triple_double'] = TripleDouble()
        self.occurrences['dame_time'] = DameTime()
        self.occurrences['player_half'] = PlayerHalf()
        self.occurrences['player_50'] = Player50()
    
    def update(self, new_board, new_box):
        self.board = new_board
        self.box = new_box
    
    def check(self):
        for key, value in self.tracker.items():
            if not value:
                self.tracker[key] = self.occurrences[key].check(self.home, self.player_id, self.board, self.box, self.util)