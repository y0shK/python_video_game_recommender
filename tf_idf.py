# receive the data from preprocessing file
# run the algorithm on the data

# input: preprocessing.py query vector
# output: a list of titles that have the highest cos similarity

from query_input import get_user_query_matrix

user_query_matrix = get_user_query_matrix()
print(user_query_matrix)
