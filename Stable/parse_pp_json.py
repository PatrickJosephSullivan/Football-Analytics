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
    # Creates a list that is callable later in the function.
    # Allows the function to leave out ids that are simply statistic or team names.
    noise = ['Pass+Rush Yds',  'FG Made',  'INT',  'Ravens',  'Kicking Points',  'Pass Completions',  'Rush Yards',  'NFL',  
             'Rush Yards in First 5 Attempts',  'Broncos',  'Longest Reception',  'Football Team',  'Receptions',  'Rush+Rec TDs',  
             'Sacks',  'Buccaneers',  'Pittsburgh Steelers',  'Rams',  'Minnesota Vikings',  'Pass Yards',  'Houston Texans',  
             'Bills',  'Full',  'Chargers',  'Eagles', 'Rush+Rec Yds', 'Single Stat', 'Packers', 'Rush Attempts', 'Pass TDs', 'Pass Attempts',
             'Receiving Yards']
    # starts a variable for error handling
    duplicates = 0
    # initializes main dictionary
    player_projections = {}
    # gets the most recent scrape. See the find_most_recent_file function for more details.
    directory = os.environ.get('pp_scrapes')
    file_path = find_most_recent_file(directory)
    
    # Loads JSON
    with open(file_path, "r") as file:
        data = json.load(file)
    
    # Creates two branches of the JSON
    players = data['included']
    stats = data['data']
    
    # GOAL: Gets player names and ids. This is so we can lookup their projections in the next loop.
    for i in players:
        if 'attributes' in i:
            # if there is a name or display name within the entry, add it to the dictionary
            if 'name' in i['attributes']:
                name = i['attributes']['name']
                id = i['id']
                # leaves an entry out of the dictionary if it's in the noise list
                if name in noise:
                    continue
                player_projections[id] = {"name": name}
            elif 'display_name' in i:
                name = i['attributes']['display_name']
                id = i['id']
                player_projections[id] = {"name": name}
    
    # GOAL: Append a new dictionary of projections to each name gathered in the previous loop.
    for i in stats:
        atts = i['attributes']
        # Makes sure there is a player id in the entry
        if 'id' in i['relationships']['new_player']['data']:
            player_id = i['relationships']['new_player']['data']['id']
            # if the player id in the data matches our dictionary then access that item in the dictionary
            if player_id in player_projections:
                entry = player_projections[player_id]
                # if all of the appropriate data is available within the data JSON then start putting that in the projections dict
                if 'stat_type' and 'line_score' and 'odds_type' in atts:
                    stat_type = atts['stat_type']
                    line_score = atts['line_score']
                    odds_type = atts['odds_type'] 
                    # checks if theirs already a stat or odd (standard, demon, etc.) within the players entry
                    # if the stat or odd is not existant it creates a new nested dictionary inside the players dictionary entry
                    if stat_type not in entry:
                        new_stat = {stat_type: {}}
                        entry.update(new_stat)
                    if odds_type not in entry[stat_type]:
                        new_odds_type = {odds_type: []} 
                        entry[stat_type].update(new_odds_type)
                    # adds a new value to the odds type tuple
                    entry[stat_type][odds_type].append(line_score)
                    """
                    dict structure should look like:

                    '212129': {'name': 'Tucker Kraft', 'Longest Reception': {'standard': [16.5]}, 
                    'Receiving Yards': {'standard': [36.5], 'goblin': [19.5, 29.5], 'demon': [59.5, 49.5, 39.5]}, 
                    'Fantasy Score': {'standard': [8.5]}, 
                    'Rush+Rec TDs': {'demon': [0.5]}, 
                    'Receptions': {'demon': [4.5], 'goblin': [2.5]}}
                    
                    """
                else:
                    'projection data not found'
            else:
                print("We found a player_id but the entry did not match in our dictionary.")
        else:
            print("Player id not present for this projection. Check elsewhere within the data")
    # FOR DEBUGGING ONLY
    # for i in player_projections.values():
    #     print(i)
    
    # ERROR HANDLING
    # if duplicates > 0:
    #     print(f'Amount of duplicates: {duplicates}')
    
    return player_projections