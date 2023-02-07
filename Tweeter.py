class Tweeter:
    def __init__(self):
        x = 5
    
    def tweet(self, msg):
        # for now just write to file
        with open('updates.txt', 'w') as f:
            f.write(msg)