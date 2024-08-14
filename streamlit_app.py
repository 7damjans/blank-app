import streamlit as st


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

css="""
<style>
    [data-testid="stForm"] {
        background: LightBlue;
    }
</style>
"""

st.write(css, unsafe_allow_html=True)
