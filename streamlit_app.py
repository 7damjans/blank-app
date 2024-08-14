import streamlit as st

css="""
<style>
    [data-testid="stForm"] {
        background: LightBlue;
    }
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
