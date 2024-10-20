import streamlit as st
from transformers import pipeline
import os

st.title("My Super Awesome OpenAI API Deployment!")

generator = pipeline('text-generation', model='gpt2')

### user's prompt input

prompt = st.text_input("Enter your prompt:")

### user's tokens input

tokens = st.number_input ("Number of tokens:", min_value=20, max_value=400, value=100 )


output = generator(prompt, max_length=tokens, num_return_sequences=1, truncation=True)

st.write(output[0]['generated_text'])

### Display
