import streamlit as st
import requests

st.title("LLM-based RAG Search")

query = st.text_input("Enter your query:")

if st.button("Search") and query:
    with st.spinner("Searching and generating answer..."):
        try:
            response = requests.post("http://localhost:5001/query", json={"query": query})
            if response.status_code == 200:
                answer = response.json().get('answer', "No answer received.")
                st.markdown("### Answer:")
                st.write(answer)
            else:
                st.error(f"Error from Flask API: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
