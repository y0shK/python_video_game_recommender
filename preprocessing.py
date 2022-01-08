# preprocess the video game data
# structure the data in a form that tf-idf can use

# input: raw csv file
# output: custom data structure

# create custom data structure
# list of strings which are transformed into tf-idf vectors
# [{game1: review1}, {game2: review2}, ...]
# extract just one review per game

def get_review_corpus(comments):
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
    # print(total_list[:2])
    return total_list[:2]