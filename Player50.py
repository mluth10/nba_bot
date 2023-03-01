from Tweeter import Tweeter

'''
    Is the player having a crazy first half. Check at helftime
'''
class Player50():
    def __init__(self):
        self.tweeter = Tweeter()

    def check(self, home, player_id, board, box):
        happened = False

        home_or_away = 'homeTeam' if home else 'awayTeam'

        roster = box[home_or_away]['players']

        player = None
        for guy in roster:
            if guy['personId'] == player_id:
                player = guy

        if player is None:
            return happened
        
        quarter = board['period']
        points = player['statistics']['points']

        if points >= 50:
            happened = True
        else:
            return happened
        
        player_name = player['name']
        
        msg = f'{player_name} just scored {points} points. '

        self.tweeter.tweet(msg)

        return happened