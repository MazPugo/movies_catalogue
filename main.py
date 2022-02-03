from flask import Flask, render_template
#from tmdb_client import get_popular_movies
import tmdb_client
import random

app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return render_template("index.html")

# def get_popular_movies():
#     endpoint = "https://api.themoviedb.org/3/movie/popular"
#     api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"
#     headers = {
#          "Authorization" : f"Bearer {api_token}"
#     }
#     response = requests.get(endpoint, headers=headers)
#     return response.json()

# @app.route('/')
# def homepage():
#     movies = tmdb_client.get_popular_movies()["results"][:8]
#     #movies =[]
#     return render_template("homepage.html", movies=movies)
@app.route('/')
def homepage(): 
    movies = (tmdb_client.get_movies(how_many=8))
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)

#xxx=get_popular_movies()
@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

# @app.route("/movie/<movie_id>")
# def movie_details(movie_id): 
#     return render_template("movie_details.html")


@app.route("/movie/<movie_id>")
def movie_details(movie_id): 
    details = tmdb_client.get_single_movie(movie_id) 
    return render_template("movie_details.html", movie=details)


