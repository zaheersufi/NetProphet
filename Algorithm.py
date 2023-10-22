import json


# Open the JSON file for reading
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Iterate through the keys (years) in the JSON data
for year in data:

    # Access the player data for the current year
    player_data = data[year]
    
    # Iterate through the players and their associated values
    for player, info in player_data.items():
        print(f"Player: {player}, Info: {info}")
        year = data
        G, PER, WS, p48WS, BPM, VORP, DRTG, tDRTG, DWS, DBPM, pBLK, pSTL, teamRecord = info 
        MVPpoints = ((p48WS) * (PER + WS + BPM + VORP))/(teamRecord ** -1/10)
        DPOYpoints = ((pBLK * 100) + (pSTL * 100) + DWS + DBPM)/(DRTG + tDRTG)
        print(f"MVP points: {MVPpoints} DPOY points: {DPOYpoints}")

    


    

