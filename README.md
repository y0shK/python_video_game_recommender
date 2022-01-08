# Python Video Game Recommender

## Description
This project is a search engine that uses TF-IDF to suggest video games to the user based on some initial query. It will incorporate game reviews, genre, platform, and publisher to find and recommend the games that are most similar to the original query.

## Dataset
The [dataset](https://www.kaggle.com/dahlia25/metacritic-video-game-comments) was obtained from Kaggle.

## How to Run
1. Download the dataset from the link above and put the csv files in the root directory
2. Run main.py

## Threats to Validity
1. The search engine only uses the first review for each game, which skews review length and may over- or under-influence the review content of specific games. In future, this will be fixed by accounting for multiple reviews for one game and incorporating this into the TF-IDF algorithm