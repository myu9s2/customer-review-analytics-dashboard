import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

from utils.load_data import load_dataset
from utils.text_analysis import (
    generate_wordcloud,
    top_words,
    review_length
)

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

df = load_dataset()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header("Analytics Filter")

selected_sentiment = st.sidebar.selectbox(
    "Sentiment",
    ["All", "positive", "neutral", "negative"]
)

if selected_sentiment != "All":
    df = df[df["sentiment_label"] == selected_sentiment]

# ==========================================
# HEADER
# ==========================================

st.title("📈 Text Analytics Dashboard")

st.caption(
    "Explore customer reviews using Natural Language Processing."
)

st.divider()

# ==========================================
# KPI
# ==========================================

positive = (df["sentiment_label"] == "positive").sum()
neutral = (df["sentiment_label"] == "neutral").sum()
negative = (df["sentiment_label"] == "negative").sum()

avg_length = (
    review_length(df)["Length"]
    .mean()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Positive",
    f"{positive:,}"
)

col2.metric(
    "Neutral",
    f"{neutral:,}"
)

col3.metric(
    "Negative",
    f"{negative:,}"
)

col4.metric(
    "Avg Review Length",
    f"{avg_length:.1f} words"
)

st.divider()

# ==========================================
# WORD CLOUD
# ==========================================

st.subheader("☁️ Word Cloud")

left, center, right = st.columns(3)

datasets = {
    "Positive": df[df["sentiment_label"] == "positive"],
    "Neutral": df[df["sentiment_label"] == "neutral"],
    "Negative": df[df["sentiment_label"] == "negative"]
}

for column, (title, data) in zip(
    [left, center, right],
    datasets.items()
):

    if len(data) > 0:

        wc = generate_wordcloud(data)

        fig = plt.figure(figsize=(8,4))

        plt.imshow(wc)

        plt.axis("off")

        column.subheader(title)

        column.pyplot(fig)

        plt.close()

st.divider()

# ==========================================
# TOP WORDS
# ==========================================

st.subheader("🔤 Most Frequent Words")

tabs = st.tabs([
    "Positive",
    "Neutral",
    "Negative"
])

labels = [
    "positive",
    "neutral",
    "negative"
]

for tab, label in zip(tabs, labels):

    with tab:

        temp = df[
            df["sentiment_label"] == label
        ]

        if len(temp) == 0:

            st.warning("No data.")

        else:

            words = top_words(temp)

            fig = px.bar(
                words,
                x="Frequency",
                y="Word",
                orientation="h",
                text="Frequency",
                title=f"Top Words ({label.title()})"
            )

            fig.update_layout(
                yaxis=dict(
                    categoryorder="total ascending"
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

st.divider()

# ==========================================
# REVIEW LENGTH
# ==========================================

st.subheader("📏 Review Length Distribution")

length_df = review_length(df)

fig = px.histogram(
    length_df,
    x="Length",
    nbins=40,
    title="Review Length"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================
# SEARCH REVIEW
# ==========================================

st.subheader("🔎 Search Review")

keyword = st.text_input(
    "Keyword"
)

if keyword:

    result = df[
        df["review_text"]
        .str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

    st.write(
        f"Found {len(result)} reviews."
    )

    st.dataframe(
        result[
            [
                "review_date",
                "product_name",
                "rating",
                "sentiment_label",
                "review_text"
            ]
        ],
        use_container_width=True
    )

st.divider()

# ==========================================
# SAMPLE REVIEWS
# ==========================================

st.subheader("📝 Sample Reviews")

sample_sentiment = st.selectbox(
    "Choose Sentiment",
    [
        "positive",
        "neutral",
        "negative"
    ]
)

sample = (
    df[
        df["sentiment_label"] == sample_sentiment
    ]
    .sample(
        min(
            10,
            len(
                df[
                    df["sentiment_label"] == sample_sentiment
                ]
            )
        )
    )
)

for _, row in sample.iterrows():

    with st.expander(
        f"⭐ {row['rating']} | {row['product_name']}"
    ):

        st.write(row["review_text"])