import plotly.express as px


def sentiment_pie(df):

    sentiment_count = (
        df["sentiment_label"]
        .value_counts()
        .reset_index()
    )

    sentiment_count.columns = [
        "Sentiment",
        "Count"
    ]

    fig = px.pie(
        sentiment_count,
        values="Count",
        names="Sentiment",
        hole=0.45,
        title="Sentiment Distribution"
    )

    return fig


def rating_distribution(df):

    rating_count = (
        df["rating"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    rating_count.columns = [
        "Rating",
        "Count"
    ]

    fig = px.bar(
        rating_count,
        x="Rating",
        y="Count",
        text="Count",
        title="Rating Distribution"
    )

    return fig


def category_chart(df):

    category_count = (
        df["product_category"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    category_count.columns = [
        "Category",
        "Reviews"
    ]

    fig = px.bar(
        category_count,
        x="Reviews",
        y="Category",
        orientation="h",
        text="Reviews",
        title="Top Categories"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    return fig


def product_chart(df):

    product_count = (
        df["product_name"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    product_count.columns = [
        "Product",
        "Reviews"
    ]

    fig = px.bar(
        product_count,
        x="Reviews",
        y="Product",
        orientation="h",
        text="Reviews",
        title="Top Reviewed Products"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    return fig

def sentiment_by_category(df):

    sentiment_category = (
        df.groupby(
            ["product_category", "sentiment_label"]
        )
        .size()
        .reset_index(name="Count")
    )

    fig = px.bar(
        sentiment_category,
        x="product_category",
        y="Count",
        color="sentiment_label",
        barmode="stack",
        title="Sentiment Distribution by Product Category"
    )

    fig.update_layout(
        xaxis_title="Product Category",
        yaxis_title="Number of Reviews",
        legend_title="Sentiment"
    )

    return fig

def review_trend(df):

    trend = df.copy()

    trend["review_date"] = (
        trend["review_date"]
        .astype("datetime64[ns]")
    )

    trend = (
        trend.groupby("review_date")
        .size()
        .reset_index(name="Reviews")
    )

    fig = px.line(
        trend,
        x="review_date",
        y="Reviews",
        markers=True,
        title="Review Trend"
    )

    return fig