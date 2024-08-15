import streamlit as st

import pandas as pd
import numpy as np

df = pd.DataFrame(
    5, columns=(5)
)

st.table(df)

st.set_page_config(
    page_title="Light Project",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdbM0Bqr7Q7mCAouhY1p_x_poXPrxinl9a7Q&s",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
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
