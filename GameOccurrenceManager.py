import Overtime

class GameOccurrenceManager:
    def check_OT(self, board):
        ot = Overtime()
        return ot.check(board)

    # initialize two dictionaries to hold state info about game
    def __init__(self):
        self.tracker = {}
        self.tracker['overtime'] = False

        self.occurrences = {}
        self.occurrences['overtime'] = self.check_OT

    def occurred(self, occ):
        return self.tracker[occ]
    
    def check_all_game(self, board):
        for key, value in self.tracker.items():
            if not value:
                self.tracker[key] = self.occurrences[key](board)

        
