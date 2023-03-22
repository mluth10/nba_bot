import pandas as pd
import nba_api
from nba_api.live.nba.endpoints import boxscore
import requests
from Roster import Roster
from Overtime import Overtime
from CloseGame import CloseGame
from VeryCloseGame import VeryCloseGame

class Game:

    def __init__(self, board, util):
        self.board = board
        self.util = util
        self.game_id = board['gameId']

        if self.active():
            self.box = boxscore.BoxScore(self.game_id).game.get_dict()
            self.homeRoster = Roster(self.board, self.box, self.util, True)
            self.awayRoster = Roster(self.board, self.box, self.util, False)

        self.tracker = {}
        self.tracker['overtime'] = False
        self.tracker['close_game'] = False
        self.tracker['very_close_game'] = False

        self.occurrences = {}
        self.occurrences['overtime'] = Overtime()
        self.occurrences['close_game'] = CloseGame()
        self.occurrences['very_close_game'] = VeryCloseGame()
        
    # override the == operator for Games
    def __eq__(self, obj):
        return isinstance(obj, Game) and obj.game_id == self.game_id

    # override the != operator
    def __ne__(self, obj):
        return not self == obj
    
    def active(self):
        return self.board['gameStatus'] == 2
    
    def update(self, board):
        self.board = board
        self.box = boxscore.BoxScore(self.game_id).game.get_dict()
        self.homeRoster.update(self.board, self.box)
        self.awayRoster.update(self.board, self.box)
    
    def check(self):
        # for the whole game
        for key, value in self.tracker.items():
            if not value:
                self.tracker[key] = self.occurrences[key].check(self.board, self.box, self.util)
        
        self.homeRoster.check()
        self.awayRoster.check()