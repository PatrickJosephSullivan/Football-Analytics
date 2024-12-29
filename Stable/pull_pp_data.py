import json
import os
from curl_cffi import requests
from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d-%H-%M")
print(timestamp)

leagues_dict = {'nhl': '8', 'nfl': '9'}

s = requests.Session(impersonate="chrome110")
response = s.get("https://api.prizepicks.com/projections?league_id=8&per_page=250&single_stat=true&in_game=true&state_code=CA&game_mode=pickem")
response.raise_for_status()
pp_proj = response.json()

start_path = os.environ.get('pp_scrapes')
file_path = f'{start_path}/pp_{timestamp}.json'

with open(file_path, "w") as file:
    json.dump(pp_proj, file, indent=4)  # `indent=4` makes the file pretty-printed