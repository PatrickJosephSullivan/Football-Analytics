import SQL_Views
import parse_pp_json

def calculate_player_averages(stat):
    df = SQL_Views.all_active_players_stats()
    
    stat_column = df[stat]
    print(df)
    

# parse_pp_json.parse_json()

calculate_player_averages('rushing_yards')