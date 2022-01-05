# preprocess the video game data
# structure the data in a form that tf-idf can use

# input: raw csv file
# output: custom data structure

import pandas as pd

info = pd.read_csv("metacritic_game_info.csv")
comments = pd.read_csv("metacritic_game_user_comments.csv")

# create custom data structure
# list of strings which are transformed into tf-idf vectors
# [{game1: review1}, {game2: review2}, ...]

total_keys = []
total_list = []

for i in range(len(comments)):
    game = comments["Title"][i]
    review = comments["Comment"][i]

    if game not in total_keys:
        total_keys.append(game)
        game_dict = {}
        game_dict[game] = review
        total_list.append(game_dict)

# print(total_keys)
print(total_list[:2])