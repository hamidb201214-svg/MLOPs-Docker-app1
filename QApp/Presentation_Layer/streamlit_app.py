import streamlit as st

st.title("QApp Demo")
question = st.text_input("Ask a question")

if question:
    st.write(f"You asked: {question}")
    st.write("This is a demo answer from the app.")