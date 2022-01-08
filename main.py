import pandas as pd

# info = pd.read_csv("metacritic_game_info.csv")
comments = pd.read_csv("metacritic_game_user_comments.csv")

from query_input import *
from preprocessing import get_review_corpus

# user input
query_string = get_user_query()

user_query_matrix = get_tfidf_matrix(query_string)
print(user_query_matrix)

# review input
review_corpus = get_review_corpus(comments)
print(review_corpus)

review_matrix = get_tfidf_matrix(review_corpus[0].values())
print(review_matrix)