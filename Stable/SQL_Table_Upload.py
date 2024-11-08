import sqlite3
import pandas as pd
import os

with open('Player_Ids.csv', 'r') as file:
    # player_ids = file.read()
    player_ids = pd.read_csv(file)

def upload_player_ids(dataframe, upload_table, append=False, replace=True):
    pass

