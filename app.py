import requests
import streamlit as st
import pickle
import pandas as pd


# Function to fetch movie poster from TMDb API
def fetch_poster(movie_id):
    try:
        # Make API request to get movie details
        response = requests.get(
            'https://api.themoviedb.org/3/movie/{}?api_key=93ee5becf9eda8183309b6be91d23bd9&language=en-US'.format(
                movie_id)
        )
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return None  # Return None if no poster path is available
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None


# Function to recommend movies
def recommend(movie_title):
    # Find the index of the movie in the DataFrame
    index = movies[movies['title'] == movie_title].index[0]

    # Get the similarity scores for the given movie
    distances = similarity[index]

    # Sort the movies by similarity score (descending order) and exclude the first one (itself)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Get the titles and posters of the recommended movies
    recommended_movies = []
    recommended_movies_posters = []
    for movie_index, _ in movies_list:
        movie_id = movies.iloc[movie_index].movie_id
        recommended_movies.append(movies.iloc[movie_index].title)

        # Fetch poster
        poster_url = fetch_poster(movie_id)
        if poster_url:
            recommended_movies_posters.append(poster_url)
        else:
            # Use a placeholder image if no poster is available
            recommended_movies_posters.append("https://via.placeholder.com/150")

    return recommended_movies, recommended_movies_posters


# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('Movie Recommender System')

# Dropdown to select a movie
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Button to trigger recommendations
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Display recommendations in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0] if posters[0] else "https://via.placeholder.com/150")
    with col2:
        st.text(names[1])
        st.image(posters[1] if posters[1] else "https://via.placeholder.com/150")
    with col3:
        st.text(names[2])
        st.image(posters[2] if posters[2] else "https://via.placeholder.com/150")
    with col4:
        st.text(names[3])
        st.image(posters[3] if posters[3] else "https://via.placeholder.com/150")
    with col5:
        st.text(names[4])
        st.image(posters[4] if posters[4] else "https://via.placeholder.com/150")