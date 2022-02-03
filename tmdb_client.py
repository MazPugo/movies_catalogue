import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"
    headers = {
          "Authorization" : f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
# endpoint = "https://api.themoviedb.org/3/movie/popular"
# api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNDhiMmRiNGQzOWU5NDNiZWNjNzkxNzk4ODNkMzdiMCIsInN1YiI6IjYxZTcwZjdiNjg0MGNjMDA0MmQ4ZjM4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lySpQODjC5emZx1F72ZZm9bVx6vS8sNvsehPXP0VrUw"
# headers = {
#           "Authorization" : f"Bearer {api_token}"}

# response = requests.get(endpoint,headers=headers)
#xxx=get_popular_movies()
# title1=xxx[0].get('title')
# p_path=xxx[0].get('poster_path')

def get_poster_url(poster_api_path, size="w780"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_single_movie(movie_id): 
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}" 
    headers = {
         "Authorization": f"Bearer {API_TOKEN}" 
    } 
    response = requests.get(endpoint, headers=headers) 
    return response.json()

def get_single_movie_cast(movie_id): 
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credentials"
    headers = { 
        "Authorization": f"Bearer {API_TOKEN}"
    } 
    response = requests.get(endpoint, headers=headers) 
    return response.json()["cast"]

def get_movies_list(list_type): 
    endpoint = fhttps://api.themoviedb.org/3/movie/{list_type}
    headers = { 
        "Authorization": f"Bearer {API_TOKEN}" 
        } 
    response = requests.get(endpoint, headers=headers) 
    response.raise_for_status() 
    return response.json() 


    



