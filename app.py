import streamlit as st
import nltk
from transformers import pipeline
from transformers import TextGenerationPipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptoms" in user_input:
        return "Please consult Doctor about your symptoms for more accurate diagnosis."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the Doctor ?"
    elif "medication" in user_input:
        return "It's important to consult Doctor before taking any medication and follow the prescription regularly."
    else:
        response = chatbot(user_input,max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How ca I help you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User : ",user_input)
            with st.spinner('Processing!!! Wait for it...'):
                response = healthcare_chatbot(user_input) 
            st.write("Healthcare Assistant : ",response)
        else:
            st.write("Please enter a valid input")

if __name__ == "__main__":
    main()