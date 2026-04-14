movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama"},
    {"title": "The Godfather", "genre": "Crime"},
    {"title": "Pulp Fiction", "genre": "Crime"},
    {"title": "Raaz", "genre": "Action"},
    {"title": "Forrest Gump", "genre": "Drama"}
]
def recommend_movies(user_genre):
    recommendations = [movie["title"] for movie in movies if movie["genre"].lower() == user_genre.lower()]
    return recommendations
print("Welcome to the Movie Recommendation System!")
user_genre = input("Please enter a movie genre (e.g., Drama, Crime, Action): ")
recommended_movies = recommend_movies(user_genre)

if recommended_movies:
    print(f"Here are some {user_genre} movies you might like:")
    for movie in recommended_movies:
        print(f"- {movie}")
else:
    print("Sorry, we don't have any movies in that genre.")