from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import boxscore
import pandas as pd
import time
from Game import Game
from Util import Util

def main():
    util = Util()
    active_games = []
    print('running')
    util.tweet("up and running")
    while(True):
        maintain_active_games(active_games, util)
        check_games(active_games)
        time.sleep(120) # 2 minutes

def maintain_active_games(active_games, util):
    games = scoreboard.ScoreBoard()
    board = games.get_dict()

    all_game_boards = board['scoreboard']['games']

    for game_board in all_game_boards:
        game = Game(game_board, util)

        # fun if-else logic that might be necessary, unsure
        if game in active_games:
            # game in active_games
            if not game.active():
                active_games.remove(game)
            else:
                # update existant game
                for old_game in active_games:
                    if old_game == game:
                        old_game.update(game.board)
        else:
            # game not in active_games
            if game.active():
                game.update(game.board)
                active_games.append(game)

def check_games(active_games):
    for game in active_games:
        game.check()


if __name__ == "__main__":
    main()