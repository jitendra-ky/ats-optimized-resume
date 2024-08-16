import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# set page config
st.set_page_config(
    page_title="ATS-Optimized-Resume",
    page_icon="🧊",
    layout="centered",
)

# app title
st.title("Streamlit App")

# st.write(f"my api key is {os.getenv('GOOGLE_API_KEY')}")