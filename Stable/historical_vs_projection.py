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
    historical = calculate_player_stat_average(stat)
    pp_data = parse_pp_json.parse_json()
    pp_data = pp_data.values()
    
    print(type(pp_data))
    for i in historical['name']:
        pass

compare_stat_to_projection('receiving_yards')