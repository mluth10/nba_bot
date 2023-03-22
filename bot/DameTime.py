from Tweeter import Tweeter

'''
    Is it Dame Time?
'''
class DameTime():
    def __init__(self):
        self.tweeter = Tweeter()

    def check(self, home, player_id, board, box, util):
        happened = False

        home_or_away = 'homeTeam' if home else 'awayTeam'

        roster = box[home_or_away]['players']

        player = None
        for guy in roster:
            if guy['personId'] == player_id:
                player = guy

        if player is None:
            return happened
        
        if player['name'] != 'Damian Lillard':
            return False
        
        msg = "It's Dame Time! Damian Lillard is currrently playing basketball."

        util.tweet(msg)

        return True