from Util import Util

class Overtime():
    def check(self, board, box, util):

        if not (board['period'] == 'OT'):
            return False

        home_team = board['homeTeam']['teamName']
        away_team = board['awayTeam']['teamName']

        msg = f'The {home_team} {away_team} game is going to OT'

        util.tweet(msg)

        return True