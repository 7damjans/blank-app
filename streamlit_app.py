import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl1fZRdbQEOIWqz0tCkfMVqqjweHHjSocy0Q&s",
)
st.title("🎈 My new app")
st.write(
    "Let's start ! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

css="""
<style>
    .stForm {
    background-color: #0000FF;
    }
</style>
"""

st.write(css, unsafe_allow_html=True)
print("Hello")
