import streamlit as st

st.set_page_config(
    page_title="Customer Review Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Review Analytics Dashboard")

st.markdown("""
## Welcome!

This project provides an end-to-end customer review sentiment analysis using Machine Learning.

### Features

- 📊 Dashboard
- 🤖 Live Sentiment Prediction
- 📈 Analytics
- 📁 Dataset Explorer
- 👤 About

Use the **sidebar** to navigate between pages.
""")

st.info("Select a page from the sidebar to begin.")