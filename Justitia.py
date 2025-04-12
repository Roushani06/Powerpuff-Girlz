import streamlit as st
import os
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

st.set_page_config(
    page_title="Justitia",
    page_icon="⚖️", 
)
st.title("Justitia-Replying to your queries")

#setting up model
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY") # Secret api key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

#function for avatar of markdowns
def get_avatar(role):
    if role == "user":
        return "👤"
    elif role == "assistant":
        return "🤖"
    return ""
#saving feedback 
def save_feedback(index):
    st.session_state.messages[index]["feedback"] = st.session_state[f"feedback_{index}"]

# Initialize message history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for i,message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"],avatar=get_avatar(message["role"])):
        st.markdown(message["content"])
        if message["role"] == "assistant":
            feedback = message.get("feedback", None)
            st.session_state[f"feedback_{i}"] = feedback
            st.feedback(
                "thumbs",
                key=f"feedback_{i}",
                # disabled=feedback is not None, allowing changing response
                on_change=save_feedback,
                args=[i],
            )

# User input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user",avatar = get_avatar("user")):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant",avatar = get_avatar("assistant")):
        # if use_mock:
        response = "(Mock reply): Hello there!"
        # else:
        try:
            chat = model.start_chat(history=[
                {"role": m["role"], "parts": [m["content"]]}
                for m in st.session_state.messages
                if m["role"] in ["user", "assistant"]
            ])
            result = chat.send_message(prompt)
            response = result.text
        except GoogleAPIError as e:
            st.error("Google API Error occurred.")
            response = "Google API Error occurred."
        st.feedback(
            "thumbs",
            key=f"feedback_{len(st.session_state.messages)}",
            on_change=save_feedback,
            args=[len(st.session_state.messages)],
        )
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
