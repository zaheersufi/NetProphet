from bs4 import BeautifulSoup
import requests
import time


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}


url = 'https://www.basketball-reference.com/leagues/NBA_' + str(1997) + '_advanced.html'

req = requests.get(url, headers)
soup  = BeautifulSoup(req.content, 'html.parser')


team = "https://www.basketball-reference.com/leagues/NBA_" + str(1997) + "_ratings.html"
req_team = requests.get(team, headers)
soup_team  = BeautifulSoup(req_team.content, 'html.parser')





team_set = {"wins", "def_rtg"}
teams = {}
print(soup_team.prettify)

table = soup_team.find("tbody")
rows = table.find_all("tr")
for row in rows:
    data = []
    name = row.find(class_="left")
    name = name.find("a").get('href')[7: 10]
    for cell in row:
        data_type = cell.get("data-stat")
        if data_type in team_set:
            data.append(cell.text)
        teams[name] = data
print(teams)


stats_set = {"g", "per", "ws", "ws_per_48", "bpm", "vorp", "dws", "dbpm", "blk_pct", "stl_pct"}

table = soup.find("tbody")
rows = table.find_all("tr")
dict2022 = {}
for row in rows:
    info = []
    if "thead" not in row.get("class"):
    # players.append(row.find_all("a")[0].text)
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
        info += teams[team]

        dict2022[name] = info
print(dict2022)