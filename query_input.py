# get input - user string for search query
# deliver output - recommended game titles

# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import nltk

# get user query
print("Enter a query:")
query_string = input()

# corpus = user query
corpus = [query_string]
print(corpus)

# vocab = word tokenized list of reviews

vocab = ["ocarina", "of", "time", "breath", "the", "wild"]
print(vocab)

pipe = Pipeline([('count', CountVectorizer(vocabulary=vocab)),
                ('tfid', TfidfTransformer())]).fit(corpus)

print(pipe['count'].transform(corpus).toarray())
print(pipe['tfid'].idf_)

v = TfidfVectorizer()
review_matrix = v.fit_transform(corpus)
print(review_matrix.shape) # (number of documents, number of terms)
print(review_matrix)