# Python Video Game Recommender

## Description
This project is a search engine that uses TF-IDF to suggest video games to the user based on some initial query. It incorporates video game titles and reviews found in the dataset below to find and recommend the games that are most similar to the original query.

## Dataset
The [dataset](https://www.kaggle.com/dahlia25/metacritic-video-game-comments) was obtained from Kaggle.

## How to Run
1. Download the dataset from the link above
2. Put the game user comments csv in the root directory
3. Run main.py

## Threats to Validity
1. A significant amount of games are recommended even when the cosine similarity threshold between the user query vector and review vectors is 0.8. Further work is needed to reduce the amount of recommendations (use userscore, other game information, and so on).
2. The user query is provided as a string, which assumes that none of the words modify the others. This reduces the amount of possible search terms. Further work is needed to apply other NLP techniques (e.g., dependency parsing) to modify the user query string before it is fed into the TF-IDF algorithm.

## Works cited
### Sklearn docs
- https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

### Python member variables
- https://stackoverflow.com/questions/9781334/python-member-variable-of-instance-works-like-member-variable-and-some-works-li

### Modify Python dictionary in-place
- https://stackoverflow.com/questions/41825868/update-python-dictionary-add-another-value-to-existing-key

### Handle incompatible TF-IDF shapes
- https://stackoverflow.com/questions/40366175/handle-incompatible-matrices-shapes-in-tf-idf

### TF-IDF vectorizer not fitted
- solution: fit_transform on train set, then fit on train and transform on test
- https://github.com/scikit-learn/scikit-learn/issues/11367
- https://stackoverflow.com/questions/49034284/notfittederror-tfidfvectorizer-vocabulary-wasnt-fitted-python
- https://stackoverflow.com/questions/28239915/what-does-this-error-mean-idf-vector-not-fitted
- https://stackoverflow.com/questions/12118720/python-tf-idf-cosine-to-find-document-similarity
- https://stackoverflow.com/questions/23838056/what-is-the-difference-between-transform-and-fit-transform-in-sklearn