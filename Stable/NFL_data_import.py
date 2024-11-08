import nfl_data_py as nfl
import pandas as pd

# Currently the oldest player in the NFL is Aaron Rodgers as of the 2024-2025 Season
# Thus we only pull data from 2005 season onward
# Variables are in df format
player_season_data = nfl.import_seasonal_data(range(2005,2024), s_type='REG')
player_info = nfl.import_players()
player_ids = nfl.import_ids()

# Dumps dfs to the project folder as Excel to familiarize with the data
player_season_data.to_excel('Player Season Data.xlsx')
player_info.to_excel('Player Info.xlsx')
player_ids.to_excel('Player Ids.xlsx')

# Dumps dfs to the project folder as CSV for SQL ingestion
player_season_data.to_csv('Player_Season_Data.csv')
player_info.to_csv('Player_Info.csv')
player_ids.to_csv('Player_Ids.csv')