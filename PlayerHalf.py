from Tweeter import Tweeter

'''
    Is the player having a crazy first half. Check at helftime
'''
class PlayerHalf():
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

        if quarter == 2 and points >= 25:
            happened = True
        else:
            return happened
        
        player_name = player['name']
        
        msg = f'{player_name} has {points} in the second quarter!'

        self.tweeter.tweet(msg)

        return happened