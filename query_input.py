# get input - user string for search query

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_user_query_matrix():

    # get user query
    print("Enter a query:")
    query_string = input()

    # transform the user query into a tf-idf vector
    # corpus = user query
    corpus = [query_string] # list of strings
    v = TfidfVectorizer()
    tfidf_query_matrix = v.fit_transform(corpus)
    print(tfidf_query_matrix)
    print(v.get_feature_names_out())

    for i, feature in enumerate(v.get_feature_names_out()):
        print(i, feature)

    return tfidf_query_matrix