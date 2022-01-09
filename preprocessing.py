# preprocess the video game data
# structure the data in a form that tf-idf can use

# input: raw csv file
# output: custom data structure

# create custom data structure class

class VideoGame:

    def __init__(self, title, review):
        self.title = title
        self.review = review
        
class VideoGameCollection:

    def __init__(self):
        self.data = {}

    def addToCollection(self, game: VideoGame):

        # include all reviews for each game
        # if the game title is not in keys, then it (and its first review) are added to data {}
        # else, at least one review is in data for the game, so we add to that list

        if game.title not in self.data.keys():
            self.data[game.title] = str(game.review)
            # print("game added")
        else:
            self.data[game.title] = self.data[game.title] + " " + str(game.review)
            # print("game appended to")

    def toString(self):
        for k, v in self.data.items():
            print("Title: ", k)
            print("Review: ", v)

    def getReviews(self):
        reviewList = []
        for v in self.data.values():
            reviewList.append(v)
        return reviewList

    def getData(self):
        return self.data