import streamlit as st

from utils.load_data import load_dataset

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📁",
    layout="wide"
)

df = load_dataset()

st.title("📁 Dataset Explorer")

st.caption(
    "Explore, search, and filter customer review data."
)

st.divider()

# ==========================================
# DATASET SUMMARY
# ==========================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Reviews",
    f"{len(df):,}"
)

col2.metric(
    "Product Categories",
    df["product_category"].nunique()
)

col3.metric(
    "Products",
    df["product_name"].nunique()
)

st.divider()

# ==========================================
# FILTER
# ==========================================

st.subheader("Filter Dataset")

left, right = st.columns(2)

category = left.multiselect(
    "Product Category",
    sorted(df["product_category"].dropna().unique()),
    default=sorted(df["product_category"].dropna().unique())
)

sentiment = right.multiselect(
    "Sentiment",
    ["positive", "neutral", "negative"],
    default=["positive", "neutral", "negative"]
)

rating = st.slider(
    "Minimum Rating",
    min_value=1,
    max_value=5,
    value=1
)

keyword = st.text_input(
    "Search Review or Product"
)

# ==========================================
# FILTERING
# ==========================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["product_category"].isin(category)
]

filtered_df = filtered_df[
    filtered_df["sentiment_label"].isin(sentiment)
]

filtered_df = filtered_df[
    filtered_df["rating"] >= rating
]

if keyword:

    mask = (
        filtered_df["review_text"]
        .str.contains(keyword, case=False, na=False)
    ) | (
        filtered_df["product_name"]
        .str.contains(keyword, case=False, na=False)
    )

    filtered_df = filtered_df[mask]

st.divider()

# ==========================================
# RESULT
# ==========================================

st.subheader("Filtered Dataset")

st.write(
    f"Showing **{len(filtered_df):,}** reviews"
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# ==========================================
# DOWNLOAD
# ==========================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Filtered Dataset",
    csv,
    file_name="filtered_reviews.csv",
    mime="text/csv"
)