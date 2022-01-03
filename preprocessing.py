# preprocess the video game data
# structure the data in a form that tf-idf can use

# input: raw csv file
# output: custom data structure
# hash table -> game title: {publisher, genre, platform, score, number of players}
# vector -> [hash table 1, hash table 2, ...]

import pandas as pd

info = pd.read_csv("metacritic_game_info.csv")
comments = pd.read_csv("metacritic_game_user_comments.csv")

# create custom data structure
# list of hash tables
info_array = []

# get information from comments csv
# [{game1: [review1, review2, ...]}, ...]

comments_dict = {}
for i in range(len(comments)):
    title = comments["Title"][i]
    if title not in comments_dict:
        comments_dict[title] = [comments["Comment"][i]]
    else:
        if (len(comments_dict[title]) < 5): # only take a certain number of reviews
            comments_dict[title].append(comments["Comment"][i])

# make the dictionary into a list format
comments_array = [comments_dict]

# get information from info csv
for i in range(len(info)):
    # re-instantiate the game dictionary every loop because each game is different every row
    # unlike the previous csv, which had multiple rows with one review each for just one game
    game_dict = {}

    # only add to the array if the game also has reviews
    if info["Title"][i] in comments_dict.keys():
        game_dict[info["Title"][i]] = {info["Publisher"][i], info["Genre"][i], 
            info["Platform"][i], info["Avg_Userscore"][i], info["No_Players"][i]}
        info_array.append(game_dict)

print(info_array[:2])
print(comments_array[0])