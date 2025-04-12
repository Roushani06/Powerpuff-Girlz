import streamlit as st
import time,os,random
import numpy as np
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

st.set_page_config(page_title = "Mock Page",page_icon = "⚪️")

st.title("Mocking Your queries")
def get_avatar(role):
    if role == "user":
        return "👤"
    elif role == "assistant":
        return "🤖"
    return ""
def mess_generator():
    message = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi! Is there anything I can help you with?",
            "Do you need help?",
            "You have enabled mock mode"
        ]
    )
    for word in message.split():
        yield word + " "
        # time.sleep(0.05)


# Initialize message history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"],avatar=get_avatar(message["role"])):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user",avatar = get_avatar("user")):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant",avatar = get_avatar("assistant")):
        # if use_mock:
        response_generator = mess_generator()
        full_response = ""
        response_placeholder = st.empty()
        for word in response_generator:
            full_response += word
            response_placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
        response_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

