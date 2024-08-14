import streamlit as st


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

css="""
<style>
    body {background-color: coral;}
</style>
"""

st.write(css, unsafe_allow_html=True)
print("Hello")
