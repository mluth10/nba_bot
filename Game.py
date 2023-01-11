import pandas as pd
import nba_api
import requests
import GameOccurrenceTracker

class Game:

    def __init__(self, board):
        self.board = board
        self.game_id = board['gameId']
        self.tracker = GameOccurrenceTracker()
        
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
    
    def check():
        # see if anything interesting is happening
        print("jhelo")