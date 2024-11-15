import sqlite3
import os
import pandas as pd

db_name = "player_database"
db_file_path = os.path.join("Stable","Database_files")
db_file_string = os.path.join(db_file_path, f'{db_name}.db')

con = sqlite3.connect(db_file_string)
cur = con.cursor()

def sql_to_df(sql_cursor):
    results = sql_cursor.fetchall()

    df = pd.DataFrame(results, columns=[description[0] for description in sql_cursor.description])

    return df

def all_active_players_stats():
    cur.execute("""
    WITH max_season AS (
    SELECT player_id, MAX(season) max_season FROM player_season GROUP BY player_id HAVING MAX(season >= 2024)
    )

    SELECT ids.gsis_id, ids.name, info.first_name, info.last_name, info.status, info.team_abbr, info.position, season.season, season.games, season.completions, season.attempts, season.passing_yards,
    season.passing_tds, season.interceptions, season.sacks, season.carries, season.rushing_yards, season.rushing_tds, season.receptions, season.receiving_yards, season.receiving_tds,
    season.special_teams_tds, season.fantasy_points
    FROM player_ids ids
    LEFT JOIN player_info info ON ids.gsis_id = info.gsis_id
    LEFT JOIN player_season season ON ids.gsis_id = season.player_id
    LEFT JOIN max_season ON ids.gsis_id = max_season.player_id
    WHERE max_season.max_season = 2024
    ORDER BY team_abbr, name, season
    ;""")

    all_stats = sql_to_df(cur)

    return all_stats

def qb_passing_yards():
    cur.execute("""
    WITH max_season AS (
    SELECT player_id, MAX(season) max_season FROM player_season GROUP BY player_id HAVING MAX(season >= 2024)
    )

    SELECT ids.gsis_id, ids.name, info.first_name, info.last_name, info.status, info.team_abbr, info.position, season.season, season.games, season.completions, season.attempts, season.passing_yards,
    season.passing_tds, season.interceptions, season.sacks, season.carries, season.rushing_yards, season.rushing_tds, season.receptions, season.receiving_yards, season.receiving_tds,
    season.special_teams_tds, season.fantasy_points
    FROM player_ids ids
    LEFT JOIN player_info info ON ids.gsis_id = info.gsis_id
    LEFT JOIN player_season season ON ids.gsis_id = season.player_id
    LEFT JOIN max_season ON ids.gsis_id = max_season.player_id
    WHERE max_season.max_season = 2024 and info.position = 'QB'
    ORDER BY team_abbr, name, season
    ;""")

    passing_yards = sql_to_df(cur)
    
    return passing_yards

# all_player_ids = cur.execute('SELECT gs FROM player_ids')
# print(all_player_ids.fetchone())