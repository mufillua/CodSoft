import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load MovieLens dataset
movies = pd.read_csv(r'C:\CODING\INTERNSHIP\TASK 4\movies.csv')
ratings = pd.read_csv(r'C:\CODING\INTERNSHIP\TASK 4\ratings.csv')

# Merge movies and ratings data
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Create a user-item matrix
user_movie_ratings = movie_ratings.pivot_table(index='userId', columns='title', values='rating')

# Fill NaN values with 0 (indicating that the user has not rated the movie)
user_movie_ratings = user_movie_ratings.fillna(0)

# Calculate similarity between movies using cosine similarity
movie_similarity = cosine_similarity(user_movie_ratings.T)

# Create a DataFrame from the similarity matrix
movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_ratings.columns, columns=user_movie_ratings.columns)

def recommend_movies(user_id, user_movie_ratings, movie_similarity_df):
    # Get the user's movie ratings
    user_ratings = user_movie_ratings.loc[user_id]

    # Initialize an empty DataFrame to store the weighted sum of similar movies
    weighted_sum = pd.DataFrame(index=user_movie_ratings.columns, columns=['WeightedSum'])

    # Find similar movies to the ones the user has rated and calculate the weighted sum
    for movie, rating in user_ratings.items():
        similar_scores = movie_similarity_df[movie] * rating
        weighted_sum['WeightedSum'] += similar_scores

    # Filter out movies the user has already rated
    unrated_movies = user_ratings[user_ratings == 0].index

    # Sort movies by the weighted sum in descending order
    recommendations = weighted_sum.loc[unrated_movies].sort_values(by='WeightedSum', ascending=False)

    return recommendations

# Recommend movies for user with userId
user_id=int(input("Enter your user ID: "))

if user_id not in user_movie_ratings.index:
    print("User ID not found.")
    exit()

recommendations = recommend_movies(user_id, user_movie_ratings, movie_similarity_df)

print(f"Recommended movies for User {user_id}:")
print(recommendations.head(10))
