import streamlit as st
import plotly.express as px

from utils.load_data import load_dataset

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

from utils.charts import (
    sentiment_pie,
    rating_distribution,
    category_chart,
    product_chart,
    sentiment_by_category,
    review_trend
)

# ===============================
# LOAD DATA
# ===============================

df = load_dataset()

# ===============================
# SIDEBAR FILTER
# ===============================

st.sidebar.header("Filter")

category = st.sidebar.multiselect(
    "Product Category",
    options=sorted(df["product_category"].dropna().unique()),
    default=sorted(df["product_category"].dropna().unique())
)

sentiment = st.sidebar.multiselect(
    "Sentiment",
    options=["positive", "neutral", "negative"],
    default=["positive", "neutral", "negative"]
)

# ===============================
# FILTER DATA
# ===============================

filtered_df = df[
    (df["product_category"].isin(category)) &
    (df["sentiment_label"].isin(sentiment))
]

# ===============================
# HEADER
# ===============================

st.title("📊 Customer Review Analytics Dashboard")

st.caption(
    "Interactive dashboard for customer review analytics and sentiment prediction."
)

st.divider()

# ===============================
# KPI
# ===============================

total_reviews = len(filtered_df)

positive = (
    filtered_df["sentiment_label"] == "positive"
).sum()

neutral = (
    filtered_df["sentiment_label"] == "neutral"
).sum()

negative = (
    filtered_df["sentiment_label"] == "negative"
).sum()

rating = filtered_df["rating"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Reviews",
    f"{total_reviews:,}"
)

col2.metric(
    "Positive",
    f"{positive:,}"
)

col3.metric(
    "Neutral",
    f"{neutral:,}"
)

col4.metric(
    "Negative",
    f"{negative:,}"
)

col5.metric(
    "Avg Rating",
    f"{rating:.2f} ⭐"
)

# ===============================
# PIE CHART
# ===============================

st.divider()

left, right = st.columns(2)
left.plotly_chart(
    sentiment_pie(filtered_df),
    use_container_width=True
)

right.plotly_chart(
    rating_distribution(filtered_df),
    use_container_width=True
)

# ===============================
# CATEGORY CHART
# ===============================

st.divider()

st.plotly_chart(
    category_chart(filtered_df),
    use_container_width=True
)

# ===============================
# PRODUCT CHART
# ===============================

st.divider()

st.plotly_chart(
    product_chart(filtered_df),
    use_container_width=True
)

# ===============================
# RECENT REVIEW CHART
# ===============================

st.divider()

st.subheader("📝 Recent Customer Reviews")

columns = [
    "review_date",
    "product_name",
    "rating",
    "sentiment_label",
    "review"
]

available_columns = [col for col in columns if col in filtered_df.columns]

recent_reviews = (
    filtered_df
    .sort_values(
        by="review_date",
        ascending=False
    )[available_columns]
    .head(20)
)

st.dataframe(
    recent_reviews,
    use_container_width=True
)

# ===============================
# SENTIMENT BY CATEGORY CHART
# ===============================
st.divider()

st.plotly_chart(
    sentiment_by_category(filtered_df),
    use_container_width=True
)

# ===============================
# REVIEW TREND CHART
# ===============================
st.divider()

st.plotly_chart(
    review_trend(filtered_df),
    use_container_width=True
)

# ===============================
# BUSINESS INSIGHTS
# ===============================
st.divider()

st.subheader("📌 Business Insights")

top_category = (
    filtered_df["product_category"]
    .value_counts()
    .idxmax()
)

top_product = (
    filtered_df["product_name"]
    .value_counts()
    .idxmax()
)

highest_rating = (
    filtered_df.groupby("product_category")["rating"]
    .mean()
    .idxmax()
)

lowest_rating = (
    filtered_df.groupby("product_category")["rating"]
    .mean()
    .idxmin()
)

st.info(f"""
**Most Reviewed Category**

{top_category}

---

**Most Reviewed Product**

{top_product}

---

**Highest Average Rating**

{highest_rating}

---

**Lowest Average Rating**

{lowest_rating}
""")