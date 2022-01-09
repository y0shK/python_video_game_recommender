"""
main.py

Use custom classes from video_game.py and custom methods from tf_idf.py to run tf-idf on the user query. 
Run this class to run the video game recommender.
"""

from video_game import VideoGame, VideoGameCollection
from tf_idf import get_fitted_train_matrix, get_unfitted_review_matrix

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# place csv from dataset into the same directory
comments = pd.read_csv("metacritic_game_user_comments.csv")

# create a new video game collection to hold all video game titles and review plaintext strings
games = VideoGameCollection()

# iterate through all reviews and store information for each video game
for i in range(len(comments)):
    title = comments["Title"][i]
    review = comments["Comment"][i]
    g = VideoGame(title, review)
    games.add_to_collection(g)

gamesData = games.get_data()

# find cosine similarity between each game and the query
# highest cosine similarities are recorded and associated games are returned

# get user query
print("Enter a query:")
query_string = input()

# structure query into appropriate data format for tf-idf methods
user_query = [query_string] 
user_matrix = get_fitted_train_matrix(user_query) 

# go through videoGameCollection's data {key: value} pairs
# find how similar the query vector and review vector are by using cosine similarity
# if the cosine similarity is greater than a certain threshold, then recommend the game
# record game titles of recommended games
game_titles = []
cos_threshold = 0.8

for k, v in gamesData.items():
    
    # include game title in game review
    # this is included because a search query of a specific game should recommend that game
    # similar to what Google does - recommends search query & other related games
    review_content = v + " " + k
    review_content = [review_content]
    m = get_unfitted_review_matrix(user_query, review_content)

    if cosine_similarity(user_matrix, m) >= cos_threshold:
        game_titles.append(k)

print("Recommended games: ")
print(game_titles)