import SQL_Views
import parse_pp_json

def calculate_player_averages(stat):
    df = SQL_Views.show_historical_averages()
    stat_column = df[stat]
    print(df)
    print(stat_column)
    

# parse_pp_json.parse_json()

calculate_player_averages('rushing_yards')