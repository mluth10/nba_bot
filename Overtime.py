from Tweeter import Tweeter

class Overtime():
    def __init__(self):
        self.tweeter = Tweeter()

    def check(self, board):
        print("checking for overtime")
        happened = False

        if(board['period'] == 'OT'):
            happened = True
            print('OT happening in game ' + board['gameCode'])
            self.tweeter.tweet('OT happening in game ' + board['gameCode'])

        return happened