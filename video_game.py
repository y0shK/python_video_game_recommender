"""
video_game.py

Create custom classes to structure the data from the dataset.
- VideoGame is each row of the csv, which includes title and review
- VideoGameCollection stores each VideoGame as a key-value pair in a hash table
- key = title, value = cumulative review plaintext {title: "review1 review2 ... reviewN"}
"""

class VideoGame:

    def __init__(self, title, review):
        self.title = title
        self.review = review
        
class VideoGameCollection:

    def __init__(self):
        self.data = {}

    # add a new key-value pair (title-review) or append to an existing key-value pair
    # include all reviews for each game as the value of the hash table
    # if the game title is not in keys, then it (and its first review) are added to data {}
    # else, at least one review is in data for the game, so we add to that list

    def add_to_collection(self, game: VideoGame):
        if game.title not in self.data.keys():
            self.data[game.title] = str(game.review)
        else:
            self.data[game.title] = self.data[game.title] + " " + str(game.review)

    def to_string(self):
        for k, v in self.data.items():
            print("Title: ", k)
            print("Review: ", v)

    # getter function to access data structure instead of calling member variable
    def get_data(self):
        return self.data