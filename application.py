import streamlit as st
import pickle
import pandas as ps
import requests

def fetchPoster(movieID):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c9e362da3687bd640daab94e7c243d5f&language=en-US".format(movieID))
    data = response.json()
    posterPath = data['poster_path']
    fullPath = "https://image.tmdb.org/t/p/w500/" + posterPath
    return fullPath

def recommend(movie):
    movieIndex = movies[movies['title'] == movie].index[0]
    distances = similarity[movieIndex]
    moviesList = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[0:10]
    recommendedMovies = []
    recommendedMoviePosters = []
    for i in moviesList:
        movieID = movies.iloc[i[0]].id
        recommendedMovies.append(movies.iloc[i[0]].title)
        recommendedMoviePosters.append(fetchPoster(movieID))
    return recommendedMovies, recommendedMoviePosters

if __name__ == '__main__':
    try:
        st.write('Your Welcome To')
        st.title("Movie Recommendation System")
        moviesDict = pickle.load(open('F:\Python_Study\Machine_Learning\Machine_Learning(Movie_Recommender_System)\movieDict.ak', 'rb'))
        movies = ps.DataFrame(moviesDict)
        similarity = pickle.load(open('F:\Python_Study\Machine_Learning\Machine_Learning(Movie_Recommender_System)\similarity.ak', 'rb'))
    
        # option =  st.selectbox('How would you like to be contacted?', moviesList)
        # option =  st.selectbox('How would you like to be contacted?', movies['title'].values)
        selectedMovie = st.selectbox("Type or Select a Movie From The Dropdown", movies['title'].values)

        if st.button('Recommendation Movies List'):
            recommendedMovies, recommendedMoviePosters = recommend(selectedMovie)
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
            with col1:
                st.text(recommendedMovies[0])
                st.image(recommendedMoviePosters[0])
            with col2:
                st.text(recommendedMovies[1])
                st.image(recommendedMoviePosters[1])
            with col3:
                st.text(recommendedMovies[2])
                st.image(recommendedMoviePosters[2])
            with col4:
                st.text(recommendedMovies[3])
                st.image(recommendedMoviePosters[3])
            with col5:
                st.text(recommendedMovies[4])
                st.image(recommendedMoviePosters[4])
            with col6:
                st.text(recommendedMovies[5])
                st.image(recommendedMoviePosters[5])
            with col7:
                st.text(recommendedMovies[6])
                st.image(recommendedMoviePosters[6])
            with col8:
                st.text(recommendedMovies[7])
                st.image(recommendedMoviePosters[7])
            with col9:
                st.text(recommendedMovies[8])
                st.image(recommendedMoviePosters[8])
            with col10:
                st.text(recommendedMovies[9])
                st.image(recommendedMoviePosters[9])
    except IndexError:
        st.text("The Is Not Any Recommendation Suggestion For Selected Movies")
    
    