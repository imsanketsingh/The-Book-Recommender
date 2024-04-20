import streamlit as st
import pickle as pk
import numpy as np

top30Books = pk.load(open('top30Books.pkl', 'rb'))
allBestBooks = pk.load(open('allBestBooks.pkl', 'rb'))
pivot_table = pk.load(open('pivot_table.pkl', 'rb'))
score = pk.load(open('score.pkl', 'rb'))

def recommend_books(book_name):
    index = np.where(pivot_table.index==book_name)[0][0]
    distances = sorted(list(enumerate(score[index])), key = lambda x:x[1], reverse = True)
    top5similar = distances[1:6]
    names = [[]]
    for i in top5similar:
        currBookName = pivot_table.index[i[0]]
        imgURL = allBestBooks[allBestBooks['Book-Title'] == currBookName]['Image-URL-M'].values[0]
        author = allBestBooks[allBestBooks['Book-Title'] == currBookName]['Book-Author'].values[0]
        rating = allBestBooks[allBestBooks['Book-Title'] == currBookName]['Relative Rating'].values[0]
        numRatings = allBestBooks[allBestBooks['Book-Title'] == currBookName]['NumRatings'].values[0]
        yearOfPublication = allBestBooks[allBestBooks['Book-Title'] == currBookName]['Year-Of-Publication'].values[0]
        
        curr_book = [currBookName, imgURL, author, rating, numRatings, yearOfPublication]
        names.append(curr_book)
    return names




st.set_page_config(page_title='The Book Recommender', page_icon = 'favicon.png', layout = 'wide', initial_sidebar_state = 'auto')


st.sidebar.title('📚📚📚Bookieee📚📚📚')

selected_option = st.sidebar.selectbox('Select Option', ['Home', 'Find Similar Books', 'About'])

if selected_option == 'Home':
    st.markdown(
    """
    <h1 style="text-align: center; font-size:32px; font-family:cursive; margin-bottom:10px;">Top 30 Books</h1>
    """,
    unsafe_allow_html=True
)

    for i in range(len(top30Books['Book-Title'])):
        st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <div style="border: 1px solid black; padding: 20px; width: 300px; margin-bottom: 10px; background-color: #f0f0f0;">
                <div style="display: flex; justify-content: center; align-items: center; width: 40px; height: 40px; border-radius: 50%; background-color: #fffeee; color: #000; font-weight: bold; margin-bottom: 5px;">
                    {i+1}
                </div>
                <div style="display: flex; justify-content: center; align-items: center; height: 225px; margin-bottom:10px">
                    <img src="{top30Books['Image-URL-L'][i]}" alt="Book Poster {i+1}" style="max-width: 150px; max-height: 225px;">
                </div>
                <p><strong>Name:</strong> {top30Books['Book-Title'][i]}</p>
                <p><strong>Author:</strong> {top30Books['Book-Author'][i]}</p>
                <p><strong>Year of Release:</strong> {top30Books['Year-Of-Publication'][i]}</p>
                <p><strong>Rating:</strong> {np.round(top30Books['Avg Rating'][i], 2)} ({top30Books['numRatings'][i]} ratings)</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
        


elif selected_option == 'Find Similar Books':
    suggestions = allBestBooks['Book-Title'].values
    userInput = st.selectbox('Search for Similar Books 📚', suggestions)

    if st.button("Search"):
        recommended_books = recommend_books(userInput)

        for i in range(len(recommended_books)):
            # st.markdown(recommended_books[i])
            if i==0:
                continue
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center; align-items: center;">
                    <div style="border: 1px solid black; padding: 20px; width: 300px; margin-bottom: 10px; background-color: #f0f0f0;">
                        <div style="display: flex; justify-content: center; align-items: center; width: 40px; height: 40px; border-radius: 50%; background-color: #fffeee; color: #000; font-weight: bold; margin-bottom: 5px;">
                            {i}
                        </div>
                        <div style="display: flex; justify-content: center; align-items: center; height: 225px; margin-bottom:10px">
                            <img src="{recommended_books[i][1]}" alt="Book Poster {1}" style="max-width: 150px; max-height: 225px;">
                        </div>
                        <p><strong>Name:</strong> {recommended_books[i][0]}</p>
                        <p><strong>Author:</strong> {recommended_books[i][2]}</p>
                        <p><strong>Year of Release:</strong> {recommended_books[i][5]}</p>
                        <p><strong>Rating:</strong> {np.round(recommended_books[i][3], 2)} ({recommended_books[i][4]} ratings)</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

                

    
    

else:
    st.title('About Bookieee')

    st.write("""
    Welcome to Bookieee, your ultimate destination for discovering new books, finding similar reads, and exploring top-rated titles!

    Bookieee uses advanced recommendation algorithms to suggest books similar to your favorites, helping you expand your reading list with exciting new discoveries.

    Whether you're a bookworm looking for your next literary adventure or a casual reader seeking recommendations, Bookieee has something for everyone.

    Happy reading!
    """)

    st.subheader('Contact Us')
    st.write("""
    If you have any questions, suggestions, or feedback, please feel free to reach out to us at [dummymail@bookieee.com](mailto:dummymail@dummybookieee.com).

    Follow us on social media:
    - [Twitter](https://twitter.com/dummybookieee)
    - [Instagram](https://www.instagram.com/dummybookieee)
    - [Facebook](https://www.facebook.com/dummybookieee)
    """)

    st.markdown("""
    ---
    """)

    st.write("""
    <div style="text-align: center;">
        © 2024 Bookieee. All rights reserved. <br>
        Constructed by <a href="https://www.github.com/imsanketsingh/" target="_blank"><strong>Sanket</strong></a>
        Hosted by <a href="https://www.streamlit.io/" target="_blank">Streamlit</a>
    </div>
    """,
    unsafe_allow_html=True)

    
