from Player import Player

class Roster:
    def __init__(self, board, box, util, home):
        self.players = []

        which_team = 'homeTeam' if home else 'awayTeam'

        for player_dict in box[which_team]['players']:
            self.players.append(Player(home, player_dict['personId'], board, box, util))

    def update(self, board, box):
        for player in self.players:
            player.update(board, box)
    
    def check(self):
        for player in self.players:
            player.check()