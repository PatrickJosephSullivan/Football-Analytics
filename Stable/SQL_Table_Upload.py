import sqlite3
import pandas as pd
import os
import datetime

# gets current date & time like 2024-11-08 16:19:14.635074
now = datetime.datetime.now().replace(microsecond=0)
now = str(now).replace(' ', '_')
now = now.replace(':', '_')

# navigates to the database you want to connect to
db_file_path = os.path.join("Stable","Database_files")
db_name = "player_database"
db_file_string = os.path.join(db_file_path, f'{db_name}.db')
backup_file_path = os.path.join(db_file_path, 'Backups')

# Starts connection and backup process
# Creates a string to add to the backup path
backup_file_string = os.path.join(backup_file_path, f'{db_name} {now}.db')


# Connects to the db
with sqlite3.connect(db_file_string) as con:
# creates a new db at specified location based on the original db file
    with sqlite3.connect(backup_file_string) as backup_con:
        con.backup(backup_con)


# Begins database operations
cur = con.cursor()

# with open(os.path.join('Stable', 'Player_CSVs', 'Player_Season_Data.csv'), 'r') as file:
#     # player_ids = file.read()
#     player_ids = pd.read_csv(file)

player_ids = pd.read_csv(os.path.join('Stable', 'Player_CSVs', 'Player_Ids.csv'))
print(player_ids)
player_ids.to_sql('player_ids', con, if_exists='fail')

def upload_player_ids(dataframe, upload_table, append=False, replace=True):
    pass