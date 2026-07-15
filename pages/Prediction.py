import streamlit as st
import pandas as pd

from utils.predict import predict_sentiment

st.set_page_config(
    page_title="Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Live Sentiment Prediction")

st.caption(
    "Predict customer review sentiment using the trained Machine Learning model."
)

st.divider()

# ==========================================
# SESSION STATE
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []

# ==========================================
# EXAMPLE REVIEWS
# ==========================================

examples = {
    "Positive": "Barang sangat bagus, kualitas mantap dan pengiriman cepat.",
    "Neutral": "Produk biasa saja sesuai harga.",
    "Negative": "Barang rusak dan sangat mengecewakan."
}

example = st.selectbox(
    "Choose an example review (optional)",
    ["Custom"] + list(examples.keys())
)

default_text = ""

if example != "Custom":
    default_text = examples[example]

review = st.text_area(
    "Customer Review",
    value=default_text,
    height=180
)

# ==========================================
# BUTTON
# ==========================================

if st.button("Predict Sentiment"):

    if review.strip():

        label, confidence, probabilities = predict_sentiment(review)

        st.divider()

        col1, col2 = st.columns([2,1])

        with col1:

            if label == "positive":
                st.success(f"Prediction : {label.title()} 😊")

            elif label == "neutral":
                st.warning(f"Prediction : {label.title()} 😐")

            else:
                st.error(f"Prediction : {label.title()} 😠")

            st.metric(
                "Confidence",
                f"{confidence:.2%}"
            )

        with col2:

            st.metric(
                "Words",
                len(review.split())
            )

            st.metric(
                "Characters",
                len(review)
            )

        st.subheader("Prediction Probability")

        for sentiment, score in probabilities.items():

            st.write(sentiment.title())

            st.progress(float(score))

            st.caption(f"{score:.2%}")

        st.session_state.history.insert(
            0,
            {
                "Review": review[:80] + ("..." if len(review) > 80 else ""),
                "Prediction": label.title(),
                "Confidence": f"{confidence:.2%}"
            }
        )

    else:

        st.warning("Please enter a review.")

# ==========================================
# HISTORY
# ==========================================

st.divider()

st.subheader("🕒 Prediction History")

if len(st.session_state.history) == 0:

    st.info("No prediction yet.")

else:

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

    if st.button("Clear History"):

        st.session_state.history = []

        st.rerun()