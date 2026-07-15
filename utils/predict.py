import pickle
import streamlit as st

MODEL_PATH = "models/model_tokopedia.pkl"

try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found.")
    st.stop()
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()

def predict_sentiment(review):

    prediction = model.predict([review])[0]

    probabilities = model.predict_proba([review])[0]

    classes = model.classes_

    confidence = probabilities.max()

    probability_dict = {
        classes[i]: float(probabilities[i])
        for i in range(len(classes))
    }

    return prediction, confidence, probability_dict