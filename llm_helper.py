from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq


# Define Groq API key and model name
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
MODEL_NAME = "llama-3.2-90b-text-preview"

# Initialize LLM model using ChatGroq
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=MODEL_NAME)

if __name__ == "__main__":
    response = llm.invoke("What are the two main ingradients in bitter leaf soup")
    print(response.content)
