from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)
#-----------------------------------------------------------------#
@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', "popular")
    #movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    #movies = tmdb_client.get_movies(how_many=8)
    movies = tmdb_client.get_moviesandlist(8,selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list)
    #return render_template("homepage.html", movies=movies)
#----------------------------------------------------------------#
# @app.route('/')
# def homepage():
#     movies = tmdb_client.get_popular_movies()["results"][:8]
#     #movies =[]
#     return render_template("homepage.html", movies=movies)
#-----------------------------------------------------------------#
# @app.route('/')
# def homepage(): 
#     movies = (tmdb_client.get_movies(how_many=8))
#     return render_template("homepage.html", movies=movies)
#-----------------------------------------------------------------#
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



# @app.route("/movie/<movie_id>")
# def movie_details(movie_id): 
#     details = tmdb_client.get_single_movie(movie_id) 
#     return render_template("movie_details.html", movie=details)

# @app.route("/movie/<movie_id>")
# def movie_details(movie_id):
#    details = tmdb_client.get_single_movie(movie_id)
#    cast = tmdb_client.get_single_movie_cast(movie_id)
#    return render_template("movie_details.html", movie=details, cast=cast)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)