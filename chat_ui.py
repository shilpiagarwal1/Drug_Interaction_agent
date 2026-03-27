import streamlit as st
from langchain_agent import run_agent

st.set_page_config(page_title="Medical Chat Assistant", layout="wide")
st.title("💊 Drug Interaction Chat Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask about medication safety...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = run_agent(user_input)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
