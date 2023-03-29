'''
    Has the player already achieved a triple double
'''
class TripleDouble():

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
        
        stats = {}
        keys = ['reboundsTotal', 'assists', 'points', 'blocks', 'steals']

        for key in keys:
            if player['statistics'][key] >= 10:
                stats[key] = player['statistics'][key]

        print('checking for ' + player['name'] + ' triple double')
        
        if len(stats) >= 3:
            happened = True
        else:
            return False

        list = [(k, v) for k, v in stats.items()]

        player_name = player['name']
        stat_1 = list[0][1]
        stat_1_name = list[0][0]
        stat_2 = list[1][1]
        stat_2_name = list[1][0]
        stat_3 = list[2][1]
        stat_3_name = list[2][0]
        msg = f'{player_name} just notched a triple double with {stat_1} {stat_1_name}, {stat_2} {stat_2_name}, and {stat_3} {stat_3_name}!'
        msg = msg.replace('reboundsTotal', 'rebounds')

        util.tweet(msg)

        return happened