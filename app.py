import streamlit as st
from langchain import PromptTemplate,LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Design the page....
st.title("Movie Recommender Systems")
user_input=st.text_input("Enter the movie title, genre or keyword")

demo_template = '''Based on {user_input} provide movie recommendation'''
template = PromptTemplate(input_variables = ['user_input'], template = demo_template)

# google gemini model 
llm=ChatGoogleGenerativeAI(model="gemini-pro",api_keys="GOOGLE-API-KEY")

if user_input:
    prompt=template.format(user_input = user_input)
    recommendations=llm.predict(text=prompt)
    st.write(f"Recommendation for you")