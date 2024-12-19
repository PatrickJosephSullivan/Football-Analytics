import SQL_Views
import pandas as pd
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV


# Configure pandas display settings
pd.set_option('display.max_rows', 200)       # Show up to 200 rows
pd.set_option('display.max_columns', 10)    # Show up to 12 columns
pd.set_option('display.width', None)        # No width limit
pd.set_option('display.max_colwidth', None) # No column width limit

# Select a player and stat to predict performance
player = 'Josh Allen'
stat = 'fantasy_points'

# Columns to remove
columns_to_drop = [
    'player_id',
    'player_name',
    'player_display_name',
    'position',
    'position_group',
    'headshot_url',
    'recent_team',
    stat
]

# Map NFL team names to integers
team_to_int = {
    'ARI': 1, 'ATL': 2, 'BAL': 3, 'BUF': 4, 'CAR': 5, 'CHI': 6, 'CIN': 7,
    'CLE': 8, 'DAL': 9, 'DEN': 10, 'DET': 11, 'GB': 12, 'HOU': 13, 'IND': 14,
    'JAX': 15, 'KC': 16, 'LV': 17, 'LAC': 18, 'LA': 19, 'MIA': 20, 'MIN': 21,
    'NE': 22, 'NO': 23, 'NYG': 24, 'NYJ': 25, 'PHI': 26, 'PIT': 27, 'SEA': 28,
    'SF': 29, 'TB': 30, 'TEN': 31, 'WAS': 32
}

season_type_to_int = {'REG': 0, 'POST': 1}

# Load data
weekly_player_data = SQL_Views.show_all_weekly_data()

# Filter data to only the player
weekly_player_data = weekly_player_data[weekly_player_data['player_display_name'] == player]
# Clean player_id and convert to integer
weekly_player_data['player_id'] = weekly_player_data['player_id'].str.replace(r'^00-', '', regex=True).astype(int)
# set our target before we delete it from the player's weekly data
y = weekly_player_data[stat]

# Drop unwanted columns
weekly_player_data = weekly_player_data.drop(columns=columns_to_drop)



# Convert opponent_team names to integers
weekly_player_data['opponent_team'] = weekly_player_data['opponent_team'].map(team_to_int)
weekly_player_data['season_type'] = weekly_player_data['season_type'].map(season_type_to_int)

# Replace all NaN values in the DataFrame with 0
weekly_player_data = weekly_player_data.fillna(0)

X = weekly_player_data

pipe = Pipeline(
    [
        ("scale", StandardScaler()),
        ("model", KNeighborsRegressor(n_neighbors=1))
    ]
)
pipe.get_params()
mod = GridSearchCV(estimator=pipe, 
             param_grid={'model__n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
             cv=3)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=30)

mod.fit(X, y)

predictions = mod.predict(X)

for i in predictions:
    print(i)

# Add the 'season-week' column
weekly_player_data['season-week'] = weekly_player_data['season'].astype(str) + weekly_player_data['week'].apply(lambda x: f"{x:02}")

plt.scatter(predictions, y)
plt.show()
print("Predicted fantasy points", predictions)
