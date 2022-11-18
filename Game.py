import pandas as pd
import requests
class Game:
    first_team_players = []
    second_team_players = []

    def __init__(self, href):
        self.html = requests.get("https://www.espn.com"+href).content
        self.dataframes = pd.read_html(self.html)

    # override the == operator for Games
    def __eq__(self, obj):
        return isinstance(obj, Game) and obj.first_team == self.first_team and obj.second_team == self.second_team
    
    def update(self):
        dataframes = pd.read_html(self.html)