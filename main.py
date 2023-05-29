import streamlit as st
from streamlit_chat import message
from functions import *
st.set_page_config(
    page_title="MINI Project",
    page_icon=":robot:"
)
st.header("Ai Voice assistant and a chatBot")
messages=[
        {"role": "system", "content": "You are an Ai who acts as Assistant named jarvis"},
        {"role": "user", "content": "f You don't Know the answer  about Realtime time data or the data you haven't been trained on try to give an answer"},
        {"role": "assistant","content":"Sure I'll try to cover up the answer "},
]
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def add_mess(message,role):
    messages.append({"role":role,"content":message})
user_input = "hi jarvis"
def get_text():
    input_text = st.text_input("You: ",user_input, key="input")
    messages.append({"role":"user","content":input_text})
    return input_text 

col1, col2 = st.columns([10, 2])

# Create a text input box
with col1:
    user_input = get_text()

# Create a button for microphone input
with col2:
    if st.button("Voice", key = ""):
        user_input = get_audio()

if user_input:
    output = main(user_input)
    st.session_state.past.append(user_input)
    speak(output)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
