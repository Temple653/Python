import requests

# TMDb API Key (Replace with your actual API key)
api = "503ba5b927a88541c165c53a3e258021"

# Get movie name input
movie_name = input("Input the movie name: ")

# Correct API endpoint for searching movies
baseurl = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&api_key={api}"

try:
    search = requests.get(baseurl)
    
    if search.status_code == 200:
        data = search.json()
        results = data.get('results', [])

        if results:
            movie = results[0]  # Get the first search result
            movie_id = movie['id']  # Extract Movie ID

            print(f"\nName and release date: {movie['title']} ({movie.get('release_date', 'N/A')})")

            # Fetch movie credits (actors and director)
            info_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api}"
            getinfo = requests.get(info_url)

            if getinfo.status_code == 200:
                search_res = getinfo.json()

                # Get actors (top 3)
                actors = [actor["name"] for actor in search_res.get("cast", [])[:4]]
                print(f"Actors: {', '.join(actors) if actors else 'N/A'}")

                # Get director
                director = next((crew["name"] for crew in search_res.get("crew", []) if crew["job"] == "Director"), "N/A")
                print(f"Director: {director}")
            else:
                print("Could not fetch movie details.")
        
        else:
            print("Error 404: Movie not found.")

    elif search.status_code == 404:
        print("Error 404: Movie not found.")
    else:
        print(f"Something went wrong! Status code: {search.status_code}")

except requests.exceptions.ConnectionError:
    print("Failed to connect to API.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")




