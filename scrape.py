from bs4 import BeautifulSoup
import requests
import time
import json

# TODO: Make sure players that transfer are Accounted for
# headers = {
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Methods': 'GET',
#     'Access-Control-Allow-Headers': 'Content-Type',
#     'Access-Control-Max-Age': '3600',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
#     }
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# range [1974, 2024]
total = {}
stats_set = {"g", "mp", "per", "ws", "ws_per_48", "bpm", "vorp", "dws", "dbpm", "blk_pct", "stl_pct"}
for i in range(1974, 2025):
    print(i)

    url = 'https://www.basketball-reference.com/leagues/NBA_' + str(i) + '_advanced.html'
    team_url = "https://www.basketball-reference.com/leagues/NBA_" + str(i) + "_ratings.html"



    req = requests.get(url, headers)
    soup  = BeautifulSoup(req.content, 'html.parser')
    req_team = requests.get(team_url, headers)
    soup_team = BeautifulSoup(req_team.content, "html.parser")

    per_poss_url = "https://www.basketball-reference.com/leagues/NBA_" + str(i) + "_per_poss.html"
    per_poss = requests.get(per_poss_url, headers)
    soup_per_pous = BeautifulSoup(per_poss.content, 'html.parser')

    team = -1
    team_set = {"wins", "def_rtg"}
    teams = {-1: ['0', '1000']}
    table = soup_team.find("tbody")
    rows = table.find_all("tr")
    table_per = soup_per_pous.find("tbody")
    rows_per = table_per.find_all("tr")
    for row in rows:
        data = []
        name = row.find(class_="left")
        name = name.find("a").get('href')[7: 10]
        for cell in row:
            data_type = cell.get("data-stat")
            if data_type in team_set:
                data.append(cell.text)
    
            teams[name] = data

    
    table = soup.find("tbody") 
    rows = table.find_all("tr")
    dict2022 = {}
    for row in range(len(rows)):
        info = []
        if "thead" not in rows[row].get("class"):
        # players.append(row.find_all("a")[0].text)
            elements = rows[row].find_all("a")
            name = elements[0].text
            if len(elements) == 1:
                #dict2022[name] = "NONE"
                info.append("NONE")
            else:
                team = elements[1].text
                #dict2022[name] = team
                info.append(team)
            for cell in rows[row]:            
                data_type = cell.get("data-stat")
                if data_type in stats_set:
                    info.append(cell.text)
            info += teams[team]
            for cell in rows_per[row]:
                data_type = cell.get("data-stat")
                if data_type == "def_rtg":
                    info.append(cell.text)
            dict2022[name] = info
    total[str(i)] =  dict2022
    time.sleep(5)
with open("data.json", "w") as outfile:
    json.dump(total, outfile)

    



