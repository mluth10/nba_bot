class Overtime():
    def check(board):
        happened = False

        if(board['period'] == 'OT'):
            happened = True
            print('OT happening in game ' + board['gameCode'])

        return happened