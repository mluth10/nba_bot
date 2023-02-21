import Overtime
import CloseGame
import VeryCloseGame

class GameOccurrenceManager:
    # initialize two dictionaries to hold state info about game
    def __init__(self):
        self.tracker = {}
        self.tracker['overtime'] = False
        self.tracker['close_game'] = False
        self.tracker['very_close_game'] = False

        self.occurrences = {}
        self.occurrences['overtime'] = self.check_OT
        self.occurrences['close_game'] = self.check_close_game
        self.occurrences['very_close_game'] = self.check_very_close_game
    
    def check_all_game(self, board, box):
        for key, value in self.tracker.items():
            if not value:
                self.tracker[key] = self.occurrences[key](board, box)

    def check_OT(self, board, box):
        ot = Overtime()
        return ot.check(board)
    
    def check_close_game(self, board, box):
        close = CloseGame()
        return close.check(board)

    def check_very_close_game(self, board, box):
        vc = VeryCloseGame()
        return vc.check(board)