import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👤",
    layout="wide"
)

st.title("👤 About This Project")

st.markdown("""
# Customer Review Analytics Dashboard

An end-to-end Machine Learning application for analyzing customer reviews from Tokopedia.

The application combines interactive analytics, Natural Language Processing (NLP), and sentiment prediction into a single dashboard to help users explore customer feedback and gain business insights.

---

## 🎯 Objectives

- Analyze customer review sentiment
- Explore customer feedback interactively
- Provide business insights through visualization
- Demonstrate an end-to-end Machine Learning workflow

---

## 🚀 Features

- Interactive Dashboard
- Customer Review Analytics
- Live Sentiment Prediction
- Word Cloud Analysis
- Dataset Explorer
- Business Insight
- Review Search

---

## 🧠 Machine Learning Pipeline

Dataset

↓

Text Preprocessing

↓

TF-IDF Vectorization

↓

Multinomial Naive Bayes

↓

Sentiment Prediction

↓

Interactive Dashboard

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Matplotlib
- WordCloud

---

## 📂 Dataset

Tokopedia Product Reviews Dataset

- 65,543 Reviews
- 13 Features
- Positive, Neutral, Negative Sentiment

---

## 👨‍💻 Developer

**Mochammad Yuga Ranapraja**

Informatics Student

Universitas Siliwangi

---

## 📌 Future Improvements

- Transformer-based sentiment model
- Explainable AI (SHAP/LIME)
- User authentication
- Cloud database integration
- Real-time review analysis

---
""")

st.info(
    "This dashboard was developed as an educational and portfolio project to demonstrate practical Machine Learning and Data Analytics skills."
)