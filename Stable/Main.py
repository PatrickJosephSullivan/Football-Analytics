import NFL_data_import
import SQL_Table_Upload
import SQL_Views

# Pings an nfl API library to pull stats
NFL_data_import.data_import(refresh=False)

# Uploads the most recent player_ids, player_info, or player_season csv to the appropriate table
# SQL_Table_Upload.upload_player_ids()
# SQL_Table_Upload.upload_player_info()
# SQL_Table_Upload.upload_player_season_data()

print(SQL_Views.all_active_players_stats())