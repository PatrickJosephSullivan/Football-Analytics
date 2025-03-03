import NFL_data_import
import SQL_Table_Upload
import SQL_Views
import pandas as pd
import pull_pp_data
import parse_pp_json


pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 8)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Pings an nfl API library to pull stats
NFL_data_import.data_import(refresh=False)

# Uploads the most recent player_ids, player_info, or player_season csv to the appropriate table
# SQL_Table_Upload.upload_player_ids()
# SQL_Table_Upload.upload_player_info()
# SQL_Table_Upload.upload_player_season_data()
# SQL_Table_Upload.upload_player_weekly_data()

# pull_pp_data.pull_data('nfl')
parse_pp_json.parse_json()

# TODO compare player averages to their projections aka build a historical model
# TODO build a predictive model
# TODO add more data to predictive model


