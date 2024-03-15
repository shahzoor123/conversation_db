from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
from Data import sqlite_data

import os

load_dotenv()


print(sqlite_data)




# using function calling it will process the db data
def Processing_DB(Data):

    return "This is the analyzed output from OpenAI."




def ai(user_input):
    print(user_input)
    Processing_DB(user_input)
    





def main():
    st.title("Converstaion with your Database Visually")
    st.write("Welcome to my Streamlit app!")



if __name__ == "__main__":
    main()
    

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")


st.title("💬 Chatbot")




if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    
    

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    print(prompt)
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    user_input = st.chat_message("user").write(prompt)
    print(user_input)
    
    
