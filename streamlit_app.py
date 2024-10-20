import streamlit as st
from transformers import pipeline
import os

st.title("My Super Awesome OpenAI API Deployment!")

generator = pipeline('text-generation', model='gpt2')

output = generator("Damascus is a", max_length=20, num_return_sequences=1, truncation=True))

st.write(output[0]['generated_text'])

### Display
