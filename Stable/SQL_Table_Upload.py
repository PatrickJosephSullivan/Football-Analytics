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

def drop_table(table):
    cur.execute(f"DROP TABLE {table}")

def upload_player_ids(dataframe=os.path.join('Stable', 'Player_CSVs', 'Player_Ids.csv'), upload_table='player_ids', append=False, replace=True):
    player_ids = pd.read_csv(dataframe)
    player_ids = player_ids.drop(player_ids.columns[0], axis=1)
    player_ids.reset_index(drop=True, inplace=True)
    if replace == True: 
        res='replace' 
    elif append == True: 
        res='append' 
    else: res='fail'
    player_ids.to_sql(upload_table, con, if_exists=res)

def upload_player_info(dataframe=os.path.join('Stable', 'Player_CSVs', 'Player_Info.csv'), upload_table='player_info', append=False, replace=True):
    player_info = pd.read_csv(dataframe)
    player_info = player_info.drop(player_info.columns[0], axis=1)
    player_info.reset_index(drop=True, inplace=True)
    if replace == True: 
        res='replace' 
    elif append == True: 
        res='append' 
    else: res='fail'
    player_info.to_sql(upload_table, con, if_exists=res)

def upload_player_season_data(dataframe=os.path.join('Stable', 'Player_CSVs', 'Player_Season_Data.csv'), upload_table='player_season', append=False, replace=True):
    player_season = pd.read_csv(dataframe)
    player_season = player_season.drop(player_season.columns[0], axis=1)
    player_season.reset_index(drop=True, inplace=True)
    if replace == True: 
        res='replace' 
    elif append == True: 
        res='append' 
    else: res='fail'
    player_season.to_sql(upload_table, con, if_exists=res)

def upload_player_weekly_data(dataframe=os.path.join('Stable', 'Player_CSVs', 'Player_Weekly_Data.csv'), upload_table='player_weekly', append=False, replace=True):
    player_weekly = pd.read_csv(dataframe)
    player_weekly = player_weekly.drop(player_weekly.columns[0], axis=1)
    player_weekly.reset_index(drop=True, inplace=True)
    if replace == True: 
        res='replace' 
    elif append == True: 
        res='append' 
    else: res='fail'
    player_weekly.to_sql(upload_table, con, if_exists=res)

def upload_all():
    upload_player_ids()
    upload_player_info()
    upload_player_season_data()
    upload_player_weekly_data()