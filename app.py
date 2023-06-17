# Import necessary packages
import random
import streamlit as st

# Set the app title and header
st.set_page_config(page_title="Random Movie Selector")
st.header('Random Movie Selector')

movie = st.text_input("Type your movie title and press Add ", label_visibility='visible')
movie_list = []

# If no, then initialize count to 0
# If count is already initialized, don't do anything
if 'movie_list' not in st.session_state:
	st.session_state.movie_list = []

# Create a button which will increment the counter
add_movie = st.button('Add Movie')
if add_movie:
    st.session_state.movie_list.append(movie)
    st.empty()

st.write('Movies List = ', st.session_state.movie_list)

random_movie = st.button('Generate Random Movie')
if random_movie:
      random_movie = random.choice(st.session_state.movie_list)
      st.write(random_movie)

clear = st.button('Clear Page!')
if clear:
    del st.session_state.movie_list