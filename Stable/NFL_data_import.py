import nfl_data_py as nfl
import pandas as pd
import os

def data_import(refresh=False):
    if refresh == False:
        pass
    elif refresh == True:
        # Currently the oldest player in the NFL is Aaron Rodgers as of the 2024-2025 Season
        # Thus we only pull data from 2005 season onward
        # Variables are in df format
        player_season_data = nfl.import_seasonal_data(range(2005,2025), s_type='REG')
        player_info = nfl.import_players()
        player_ids = nfl.import_ids()
        week_by_week = nfl.import_weekly_data(range(2005,2025))

        # Data Transformations for per game stats
        player_season_data['passing_yards_per_game'] = player_season_data['passing_yards'] / player_season_data['games']
        player_season_data['receptions_per_game'] = player_season_data['receptions'] / player_season_data['games']
        player_season_data['rush_yards_per_game'] = player_season_data['rushing_yards'] / player_season_data['games']
        player_season_data['rush_and_receiving_tds_per_game'] = (player_season_data['rushing_tds'] + player_season_data['receiving_tds'] )/ player_season_data['games']
        player_season_data['pass_tds_per_game'] = player_season_data['passing_tds'] / player_season_data['games']


        # Dumps dfs to the project folder as Excel to familiarize with the data
        player_season_data.to_excel(os.path.join('Stable', 'Player_CSVs', 'Player Season Data.xlsx'))
        player_info.to_excel(os.path.join('Stable', 'Player_CSVs', 'Player Info.xlsx'))
        player_ids.to_excel(os.path.join('Stable', 'Player_CSVs', 'Player Ids.xlsx'))
        week_by_week.to_excel(os.path.join('Stable', 'Player_CSVs', 'Player Weekly Data.xlsx'))

        # Dumps dfs to the project folder as CSV for SQL ingestion
        player_season_data.to_csv(os.path.join('Stable', 'Player_CSVs', 'Player_Season_Data.csv'))
        player_info.to_csv(os.path.join('Stable', 'Player_CSVs', 'Player_Info.csv'))
        player_ids.to_csv(os.path.join('Stable', 'Player_CSVs', 'Player_Ids.csv'))
        week_by_week.to_csv(os.path.join('Stable', 'Player_CSVs', 'Player_Weekly_Data.csv'))
    else:
        print("Please input a True or False value for the 'refresh' variable")

