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
                print(i['id'], i['attributes']['name'])
                name = i['attributes']['name']
                id = i['id']
                player_projections[name] = {"id": id}
            elif 'display_name' in i:
                print(i['id'], i['attributes']['display_name'])
                name = i['attributes']['display_name']
                id = i['id']
                player_projections[name] = {"id": id}
    print(player_projections)

parse_json()