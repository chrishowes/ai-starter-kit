import streamlit as st
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key=st.secrets['openai_api_key'])

name = st.text_input("What is your name?")
goal = st.text_area("What is your goal for the week?")

response = st.text("Hello!")

# response = llm("Hello!")

# st.write(response)
