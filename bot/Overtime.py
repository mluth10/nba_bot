from Tweeter import Tweeter

class Overtime():
    def __init__(self):
        self.tweeter = Tweeter()

    def check(self, board, box):

        if not (board['period'] == 'OT'):
            return False

        home_team = board['homeTeam']['teamName']
        away_team = board['awayTeam']['teamName']

        msg = f'The {home_team} {away_team} game is going to OT'

        self.tweeter.tweet(msg)

        return True