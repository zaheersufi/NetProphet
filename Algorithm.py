import json
from math import *
from make_names_accent_friendly import *


# Open the JSON file for reading
with open('data.json', 'r') as json_file:
    data = json.load(json_file)


def top_10(dictionary):
    counter = 0
    new_dict = {}
    for i in dictionary:
        if counter < 11:
            new_dict[i] = dictionary[i]
        else:
            break
        counter += 1
    return new_dict

# Iterate through the keys (years) in the JSON data
total = {}
for year in data:
    mvp_dict = {}
    # Access the player data for the current year
    player_data = data[year]
    
    # Iterate through the players and their associated values
    for player, info in player_data.items():
        player= convert_name(player)
        # print(f"Player: {player}, Info: {info}")
        # G, PER, WS, p48WS, BPM, VORP, DRTG, DWS, DBPM, pBLK, pSTL, teamRecord, tDRTG = info 
        TEAM, G, PER, WS, p48WS, BPM, VORP, DRTG, DWS, DBPM, pBLK, pSTL, teamRecord, tDRTG = info
        MVPpoints = -5000
        is_valid = True
        for things in info:
            if things == "":
                is_valid = False
        if is_valid:
            power = ( (p48WS) ** 1/7)
            if float(G) > 60  or ((year == "1999" or year == "2012") and float(G) > 40) or (year == "2024"): 
                MVPpoints = ((p48WS) * (PER + WS + BPM + VORP))/(teamRecord ** -1/10)
                DPOYpoints = ((pBLK * 100) + (pSTL * 100) + DWS + DBPM)/(DRTG + tDRTG)        
        print(f"MVP points: {MVPpoints} DPOY points: {DPOYpoints}")
        mvp_dict[player] = MVPpoints
    mvp_dict = dict(sorted(mvp_dict.items(), key=lambda item: item[1], reverse=True))
    mvp_dict = top_10(mvp_dict)
    total[year] = mvp_dict
 

with open("output.json", "w", encoding="utf-8") as outfile: 
    json.dump(total, outfile, ensure_ascii=False, indent=4)
    


    


    

