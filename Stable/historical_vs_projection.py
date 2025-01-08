import SQL_Views
import parse_pp_json
import pandas as pd

def calculate_player_stat_average(stat):
    df = SQL_Views.show_historical_averages()
    stat_column = df[stat]
    name_column = df['name']
    df = pd.DataFrame({'name': name_column, stat: stat_column})
    return df
    
def compare_stat_to_projection(stat):
    pp_to_stat_dict = {}
    calculate_player_stat_average(stat)
    parse_pp_json.parse_json()

compare_stat_to_projection('receiving_yards')