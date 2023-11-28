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
totalMVP = {}
totalDPOY = {}
for year in data:
    mvp_dict = {}
    dpoy_dict = {}
    # Access the player data for the current year
    player_data = data[year]
    
    # Iterate through the players and their associated values
    for player, info in player_data.items():
        player= convert_name(player)
        # print(f"Player: {player}, Info: {info}")
        # Team,  G, PER, pSTL, pBLK, DWS, WS, p48WS, DBPM, BPM, VORP, teamRecord, tDRTG, DRTG, = info 
        TEAM, G, MP, PER, pSTL, pBLK, DWS, WS, p48WS, DBPM, BPM, VORP, teamRecord, tDRTG, DRTG, = info 
        MVPpoints = -5000
        is_valid = True
        if tDRTG != "":
            for things in info:
              if things == "":
                  is_valid = False
        if is_valid:
            power = ( float(p48WS) ** 1/7)
            if float(G) > 60 and float(MP) >= 1700  or ((year == "1999" or year == "2012") and float(G) > 40) or (year == "2024" and float(G) > 10): 
                MVPpoints = float(teamRecord) * ((float(p48WS) * 10) + (float(PER) + float(WS) + float(BPM) + float(VORP)))
                ## DPOYpoints = float(DWS) + float(DBPM)   
        # print(f"{player}: MVP points: {MVPpoints} DPOY points: {DPOYpoints}")
        mvp_dict[player] = MVPpoints
        ## dpoy_dict[player] = DPOYpoints
    mvp_dict = dict(sorted(mvp_dict.items(), key=lambda item: item[1], reverse=True))
    mvp_dict = top_10(mvp_dict)
    ## dpoy_dict = dict(sorted(dpoy_dict.items(), key=lambda item: item[1], reverse=True))
    ## dpoy_dict = top_10(dpoy_dict)
    totalMVP[year] = mvp_dict
    totalDPOY[year] = dpoy_dict

 

with open("output.json", "w", encoding="utf-8") as outfile: 
    json.dump(totalMVP, outfile, ensure_ascii=False, indent=4)
    ## json.dump(totalDPOY, outfile, ensure_ascii=False, indent=4)
    


    


    

