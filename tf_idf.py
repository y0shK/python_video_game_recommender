# receive the data from preprocessing file
# run the algorithm on the data

# input: preprocessing.py raw data
# output: tf-idf vectors

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import VideoGame, VideoGameCollection
from query_input import get_user_query

import os
import pandas as pd

# user query matrix
def get_tfidf_matrix(corpus):

    # transform the query into a tf-idf vector
    v = TfidfVectorizer()
    tfidf_matrix = v.fit_transform(corpus) # fit_transform is fitting and transforming on corpus
    print(tfidf_matrix)
    # print(v.get_feature_names_out())

    # for i, feature in enumerate(v.get_feature_names_out()):
        # print(i, feature)

    return tfidf_matrix

# review matrix per game
def get_unfitted_matrix(fit_corpus, transform_corpus):
    v = TfidfVectorizer()
    v.fit(fit_corpus) # fit on original corpus (user query)
    matrix = v.transform(transform_corpus) # transform on new corpus (review)
    return matrix

info = pd.read_csv("metacritic_game_info.csv")
comments = pd.read_csv("metacritic_game_user_comments.csv")

games = VideoGameCollection()

for i in range(0, 1000):
    title = comments["Title"][i]
    review = comments["Comment"][i]
    g = VideoGame(title, review)
    print(g.title)
    games.addToCollection(g)
print(i)

print("success")
print(games.toString())

reviews = games.getReviews()
gamesData = games.getData()

# find cos similarity between each game and the query
# highest cos similarities are recorded and associated games are returned

# get query
user_query = get_user_query()
user_query = [user_query] # send in right format
user_matrix = get_tfidf_matrix(user_query) 
print(user_matrix)

game_titles = []

for k, v in gamesData.items():
    
    # include game title in game review
    # this is included because a search query of a specific game should recommend that game
    # similar to what google does - recommends search query & other related games
    v = v + " " + k

    #v = [v]
    #print(v)
    m = get_unfitted_matrix(user_query, [v])
    print(user_matrix.shape)
    print(m.shape)
    if cosine_similarity(user_matrix, m) > 0.5:
        print("cos similarity greater")
        game_titles.append(k)
    print(cosine_similarity(user_matrix, m))

print(game_titles)