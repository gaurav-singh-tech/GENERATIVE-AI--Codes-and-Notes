# 1. Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
from transformers import pipeline
import os

# 2. Load environment variables from .env file
load_dotenv()

# 3. Create a Streamlit app header
st.header("Research Tool")

paper_input= st.selectbox(
    "Select a research paper to summarize:",
    ("Paper 1: AI in Healthcare", "Paper 2: Climate Change Impacts", "Paper 3: Quantum Computing Advances"))

style_input= st.selectbox(
    "Select a summarization style:",
    ("Concise", "Detailed", "Bullet Points"))

length_input= st.selectbox(
    "Select summary length:",
    ("Short", "Medium", "Long"))    

# 4. Cache the model loading to avoid reloading on every interaction
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="t5-small")

summarizer = load_summarizer()

# 5. Get user input
user_input = st.text_input("Enter your text here:")

# 6. Summarization button
if st.button("Summarize Text"):
    st.write('Hello! Summarizing your text now...')
   