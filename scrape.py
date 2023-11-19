from bs4 import BeautifulSoup
import requests
import time
import json

# TODO: Make sure players that transfer are Accounted for
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# range [1997, 2024]
total = {}
stats_set = {"g", "per", "ws", "ws_per_48", "bpm", "vorp", "dws", "dbpm", "blk_pct", "stl_pct"}
for i in range(1997, 2025):
    url = 'https://www.basketball-referencex.com/leagues/NBA_' + str(i) + '_advanced.html'
    url2 = 'https://www.basketball-reference.com/leagues/NBA_' + str(i) + '_standings.html'

    req = requests.get(url, headers)
    soup  = BeautifulSoup(req.content, 'html.parser')
    req_team = requests.get(url2, headers)
    soup_team = BeautifulSoup(req_team.content, "html.parser")

    table = soup.find("tbody")
    teams = []
    rows = table.find_all("tr")
    dict2022 = {}
    for row in rows:
        info = []
        if "thead" not in row.get("class"):
        #   players.append(row.find_all("a")[0].text)
            elements = row.find_all("a")
            name = elements[0].text
            if len(elements) == 1:
                #dict2022[name] = "NONE"
                info.append("NONE")
            else:
                team = elements[1].text
                #dict2022[name] = team
                info.append(team)
            for cell in row:            
                data_type = cell.get("data-stat")
                if data_type in stats_set:
                    info.append(cell.text)
            
            dict2022[name] = info
    total[str(i)] =  dict2022
    time.sleep(1)
with open("test.json", "w") as outfile:
    json.dump(total, outfile)

    



