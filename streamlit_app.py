import streamlit as st


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
