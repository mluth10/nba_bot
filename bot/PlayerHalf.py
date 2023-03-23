'''
    Is the player having a crazy first half.
'''
class PlayerHalf():
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
        
        quarter = board['period']
        points = player['statistics']['points']

        if quarter == 2 and points >= 25:
            happened = True
        else:
            return happened
        
        player_name = player['name']
        
        msg = f'{player_name} has {points} in the second quarter!'

        util.tweet(msg)

        return happened