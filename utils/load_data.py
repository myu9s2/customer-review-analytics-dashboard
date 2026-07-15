import pandas as pd
import streamlit as st

DATA_PATH = "data/tokopedia_product_reviews_2025.csv"

@st.cache_data
def load_dataset():
    try:
        return pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        st.error("Dataset not found. Please check the data folder.")
        st.stop()
    except Exception as e:
        st.error(f"Failed to load dataset: {e}")
        st.stop()