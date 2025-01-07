import os
import json
from datetime import datetime

leagues_dict = {'nhl': '8', 'nfl': '9'}

def find_most_recent_file(directory):
    # List all files and subdirectories in the directory
    all_files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]

    # Check if the directory contains files
    if not all_files:
        return None

    # Find the file with the most recent modification time
    most_recent_file = max(all_files, key=os.path.getmtime)
    return most_recent_file

def parse_json():
    noise = ['Pass+Rush Yds',  'FG Made',  'INT',  'Ravens',  'Kicking Points',  'Pass Completions',  'Rush Yards',  'NFL',  
             'Rush Yards in First 5 Attempts',  'Broncos',  'Longest Reception',  'Football Team',  'Receptions',  'Rush+Rec TDs',  
             'Sacks',  'Buccaneers',  'Pittsburgh Steelers',  'Rams',  'Minnesota Vikings',  'Pass Yards',  'Houston Texans',  
             'Bills',  'Full',  'Chargers',  'Eagles', 'Rush+Rec Yds', 'Single Stat', 'Packers', 'Rush Attempts', 'Pass TDs', 'Pass Attempts',
             'Receiving Yards']
    player_projections = {}
    directory = os.environ.get('pp_scrapes')
    file_path = find_most_recent_file(directory)
    with open(file_path, "r") as file:
        data = json.load(file)
    players = data['included']
    stats = data['data']
    for i in players:
        if 'attributes' in i:
            if 'name' in i['attributes']:
                name = i['attributes']['name']
                id = i['id']
                if name in noise:
                    continue
                player_projections[id] = {"name": name}
            elif 'display_name' in i:
                name = i['attributes']['display_name']
                id = i['id']
                player_projections[id] = {"name": name}
    for i in stats:
        atts = i['attributes']
        if 'id' in i['relationships']['new_player']['data']:
            player_id = i['relationships']['new_player']['data']['id']
            if player_id in player_projections:
                entry = player_projections[player_id]
                if 'stat_type' and 'line_score' and 'odds_type' in atts:
                    stat_type = atts['stat_type'] 
                    line_score = atts['line_score']
                    odds_type = atts['odds_type']
                    proj_data = {odds_type: {stat_type: line_score}}
                    entry.update(proj_data)
                else:
                    'projection data not found'
            else:
                print("We found a player_id but the entry did not match in our dictionary.")
        else:
            print("Player id not present for this projection. Check elsewhere within the data")
    for i in player_projections.values():
        print(i)
    return player_projections