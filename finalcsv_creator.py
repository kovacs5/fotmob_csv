import pandas as pd
import urllib.request
from urllib.request import urlopen
import json
import requests
from bs4 import BeautifulSoup

json_url = "https://www.fotmob.com/api/leagues?id=71&ccode3=TUR"

with urllib.request.urlopen(json_url) as url:
    data = json.load(url)

table = data['matches']['allMatches']
df = pd.json_normalize(table)
df = df[df['status.reason.longKey'] == 'finished']

i = 0

df3 = []

while i < len(df):

    match_id = df['id'].iloc[i]

    with urllib.request.urlopen("https://www.fotmob.com/api/matchDetails?matchId=" + str(match_id)) as url:
        data_url = json.load(url)

    df2 = pd.DataFrame(data_url["content"]["shotmap"]["shots"])
    lig_df = pd.DataFrame(data_url["general"])
    league_name = str(lig_df["parentLeagueName"].iloc[0])
    league_season = str(lig_df["parentLeagueSeason"].iloc[0])
    df2["league_name"] = league_name
    df2["league_season"] = league_season
    df2["match_id"] = match_id
    df3.append(df2)

    i += 1

final_df = pd.concat(df3)

final_df.to_csv("stsl_final.csv", encoding="utf-8-sig")
