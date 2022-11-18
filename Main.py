import requests
from bs4 import BeautifulSoup
import pandas as pd
import tweepy

def main():
    print("hello")

def scrape():
    html = requests.get("https://www.espn.com/nba/scoreboard").content
    soup = BeautifulSoup(html, 'html.parser')

    game_count = len(soup.find_all(class_="Scoreboard bg-clr-white flex flex-auto justify-between"))
    ended_game_count = len(soup.find_all(class_="ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01"))
    active_game_count = game_count - ended_game_count

    buttons = soup.find_all("a", class_="AnchorLink Button Button--sm Button--anchorLink Button--alt mb4 w-100 mr2")

    active_game_links = []

    counter = 0
    for button in buttons:
        if button.text == "Box Score" and counter < active_game_count:
            counter += 1
            active_game_links.append(button['href'])

    # for link in active_game_links:
    #     get_data_from_url(link)
    
    get_data_from_url(active_game_links[3])

if __name__ == "__main__":
    main()