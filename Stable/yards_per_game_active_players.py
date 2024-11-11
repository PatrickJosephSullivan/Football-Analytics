import sqlite3
import os

db_name = "player_database"
db_file_path = os.path.join("Stable","Database_files")
db_file_string = os.path.join(db_file_path, f'{db_name}.db')

con = sqlite3.connect(db_file_string)
cur = con.cursor()
all_player_ids = cur.execute('SELECT gs FROM player_ids')
print(all_player_ids.fetchone())