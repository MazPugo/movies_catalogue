import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"
#---------------------------------------------------------------------------------------
def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"
    headers = {
          "Authorization" : f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
#---------------------------------------------------------------------------------------
def get_toprated_movies():
    endpoint = "https://api.themoviedb.org/3/movie/top_rated"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"
    headers = {
          "Authorization" : f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
#---------------------------------------------------------------------------------------
def get_upcoming_movies():
    endpoint = "https://api.themoviedb.org/3/movie/upcoming"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"
    headers = {
          "Authorization" : f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
#---------------------------------------------------------------------------------------
def get_nowplaying_movies():
    endpoint = "https://api.themoviedb.org/3/movie/now_playing"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"
    headers = {
          "Authorization" : f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
#---------------------------------------------------------------------------------------
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
#--------------------------------------------------------------------------------------
def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
#-------------------------------------------------------------------------------------
# creating a function to return movies based on the input of list_type
# list_type can be: top_rated, upcoming, now_playing and popular
# the list_type "popular" is the default value, it mean even if the user enters a wrong list
# the "popular" list_type will be selected by default

def get_moviesandlist(how_many,list_type):
    if list_type=="top_rated":
        data = get_toprated_movies()
    elif list_type=="upcoming":
        data = get_upcoming_movies()
    elif list_type=="now_playing":
        data = get_nowplaying_movies() 
    else:
        data = get_popular_movies()       
    
    return data["results"][:how_many]
#-----------------------------------------------------------    

def get_single_movie(movie_id): 
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}" 
    headers = {
         "Authorization": f"Bearer {API_TOKEN}" 
    } 
    response = requests.get(endpoint, headers=headers) 
    return response.json()

def get_single_movie_cast(movie_id): 
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = { 
        "Authorization": f"Bearer {API_TOKEN}"
    } 
    response = requests.get(endpoint, headers=headers) 
    return response.json()["cast"]

def get_movies_list(list_type): 
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = { 
        "Authorization": f"Bearer {API_TOKEN}" 
        } 
    response = requests.get(endpoint, headers=headers) 
    response.raise_for_status() 
    return response.json() 

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
    



