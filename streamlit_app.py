import streamlit as st
from transformers import pipeline
import os

st.title("My Super Awesome OpenAI API Deployment!")

generator = pipeline('text-generation', model='gpt2')

### user's prompt input

prompt = st.text_input("Enter your prompt:")

### user's tokens input

tokens = st.number_input ("Number of tokens:", min_value=20, max_value=200, value=100 )

if st.button("Enter"):

  output1 = generator( prompt, max_length=tokens, num_return_sequences=1, temperature=0.9, truncation=True) ##Creative
  output2 = generator( prompt, max_length=tokens, num_return_sequences=1, temperature=0.1, truncation=True) ##Predictable

  ### Display
  st.write("### **Creative Response:**") 
  st.write(output1[0]['generated_text'])
  
  st.write("### **Predictable Response:**") 
  st.write(output2[0]['generated_text'])
 
