import re
from Util import Util

class CloseGame():
    def check(self, board, box, util):
        times = re.findall('[0-9][0-9]', board['gameClock'])
        seconds_in_quarter = 60*int(times[0]) + int(times[1]) + int(times[2])/100
        minutes_in_quarter = times[0]

        home_points = 0
        for period in board['homeTeam']['periods']:
            home_points = home_points + period['score']

        away_points = 0
        for period in board['awayTeam']['periods']:
            away_points = away_points + period['score']
        
        diff = abs(home_points - away_points)


        if not (board['period'] == 4 and seconds_in_quarter < 300 and diff <= 5):
            return False

        winTeam = ''
        loseTeam = ''
        if home_points >= away_points:
            winTeam = board['homeTeam']['teamName']
            loseTeam = board['awayTeam']['teamName']
        else:
            winTeam = board['awayTeam']['teamName']
            loseTeam = board['homeTeam']['teamName']
        
        msg = ''
        if diff != 0:
            msg = "{winningTeam} beating {losingTeam} by {pts} with {minutes} minutes to go".format(winningTeam = winTeam, losingTeam = loseTeam, pts = diff, minutes=minutes_in_quarter)
        else:
            msg = "{winningTeam} and {losingTeam} tied with {minutes} minutes to go".format(winningTeam = winTeam, losingTeam = loseTeam, minutes=minutes_in_quarter)
        
        util.tweet(msg)

        return True