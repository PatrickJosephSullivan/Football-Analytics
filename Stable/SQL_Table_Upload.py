import sqlite3
import pandas as pd
import os

con = sqlite3.connect("player_database.db")
cur = con.cursor()

with open(os.path.join('Stable', 'Player_CSVs', 'Player_Season_Data.csv'), 'r') as file:
    # player_ids = file.read()
    player_ids = pd.read_csv(file)


def upload_player_ids(dataframe, upload_table, append=False, replace=True):
    pass

