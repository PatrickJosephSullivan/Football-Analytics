import json
import os
from curl_cffi import requests
from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d-%H-%M")
print(timestamp)



def pull_data():
    s = requests.Session(impersonate="chrome110")
    response = s.get(f"https://quizlet.com/256948978/lsat-flash-cards/")
    print(response.text)
    # response.raise_for_status()
    # pp_proj = response.json()

    # start_path = os.environ.get('pp_scrapes')
    # file_path = f'{start_path}/pp_{timestamp}.json'

    # with open(file_path, "w") as file:
    #     json.dump(pp_proj, file, indent=4)  # `indent=4` makes the file pretty-printed

pull_data()