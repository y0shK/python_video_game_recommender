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
        if game.title not in self.data.keys():
            self.data[game.title] = game.review
            print("game added")

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