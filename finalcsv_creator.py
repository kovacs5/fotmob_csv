import pandas as pd
import urllib.request
from urllib.request import urlopen
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.fotmob.com/leagues/71/matches/super-lig'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

all_scripts = soup.find_all('script')

matches_script = all_scripts[32].text

data = json.loads(matches_script)

maclar = data['props']['pageProps']['matches']['allMatches']

df3 = []

for i in range(len(maclar)):

    df = pd.DataFrame(data['props']['pageProps']['matches']['allMatches'][i])

    if (df['status']['finished'] == True):

        match_id = df['id'][0]

        with urllib.request.urlopen("https://www.fotmob.com/api/matchDetails?matchId=" + str(match_id)) as url:
            data_url = json.load(url)

        df2 = pd.DataFrame(data_url["content"]["shotmap"]["shots"])
        lig_df = pd.DataFrame(data_url["general"])
        league_name = str(lig_df["parentLeagueName"].iloc[0])
        league_season = str(lig_df["parentLeagueSeason"].iloc[0])
        df2["league_name"] = league_name
        df2["league_season"] = league_season
        df3.append(df2)

final_df = pd.concat(df3)

final_df.to_csv("csv/stsl_final.csv", encoding="utf-8-sig")