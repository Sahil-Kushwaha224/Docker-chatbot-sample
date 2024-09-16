import streamlit as st
from chatbot import BotService

# Title and header
st.title("🤖 ChatBot Using Google Gemini Model")
st.markdown("Welcome to the ChatBot interface! Type your messages below and get responses powered by Google Gemini.")

# Initialize the bot service
bot_service = BotService()

# Initialize session state
if 'chat_logs' not in st.session_state:
    st.session_state['chat_logs'] = []

# User input area
st.markdown("### Your Message")
input_text = st.text_input("Type your message here:", key="text_input", placeholder="Ask me anything...")

# Button styling
button_style = """
    <style>
        .stButton>button {
            background-color: #007BFF;
            color: white;
            border-radius: 4px;
            padding: 0.5em 1em;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Submit button
if st.button("Send"):
    if input_text.strip():
        reply, _ = bot_service.generate_reply(input_text.strip())
        st.session_state['chat_logs'].append(("You", input_text.strip()))
        st.session_state['chat_logs'].append(("Bot", reply))
        st.session_state['input_text'] = ""  
    else:
        st.warning("Please type a message.")

# Display chat logs with improved layout
st.markdown("### Conversation")
chat_container = st.container()

with chat_container:
    for sender, message in st.session_state['chat_logs']:
        if sender == "You":
            st.markdown(f"<div style='background-color:#D6EAF8; padding:10px; border-radius:10px; margin:10px 0;'><strong>{sender}:</strong> {message}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color:#FAD7A0; padding:10px; border-radius:10px; margin:10px 0;'><strong>{sender}:</strong> {message}</div>", unsafe_allow_html=True)

# Footer with additional information
st.markdown("---")
st.markdown("### About")
st.markdown("This chatbot uses the Google Gemini model to generate intelligent responses to your queries. Feel free to interact and explore its capabilities!")
