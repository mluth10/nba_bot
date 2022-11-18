import requests
from bs4 import BeautifulSoup
import pandas as pd
import tweepy

def scrape():
    html = requests.get("https://www.espn.com/nba/scoreboard").content
    soup = BeautifulSoup(html, 'html.parser')

    all_games = len(soup.find_all(class_="Scoreboard bg-clr-white flex flex-auto justify-between"))
    finished_games = len(soup.find_all(class_="ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01"))
    active_game_count = all_games - finished_games

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
    

def get_data_from_url(href):
    html = requests.get("https://www.espn.com"+href).content
    b = pd.read_html(html)
    print(b[0].iloc[0, 0])
    print(b[0].iloc[1, 0])


if __name__ == "__main__":
    auth = tweepy.OAuth1UserHandler(
        "I2odWV2H9ct74GzqCJBwHkb9l", "iH8ERpgp9jYEJqf237VLbUeh1sEXUeWO95VcW2Nz5Vsw13UtFA", "4888449014-Fxgl4jL0PYX5gqDw7F1jP3PCBAZDYBxM8pGBzr2", "oYIMglRWd7mhQatleGiscosWtGXRAXTbzaBnZRv3WEfGu"
    )

    #api = tweepy.API(auth)

    scrape()