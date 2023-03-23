'''
    Is the player getting career high points? Must be higher than 25.
'''
class CareerHigh():
    def check(self, home, player_id, board, box, util):
        home_or_away = 'homeTeam' if home else 'awayTeam'

        roster = box[home_or_away]['players']

        player = None
        for guy in roster:
            if guy['personId'] == player_id:
                player = guy

        if player is None:
            return False
        
        points = player['statistics']['points']

        if points < 50:
            return False
        
        player_name = player['name']
        
        msg = f'{player_name} just scored {points} points.'

        util.tweet(msg)

        return True