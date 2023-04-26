import streamlit as st
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key=st.secrets['openai_api_key'])

name = st.text_input("What is your name?")
