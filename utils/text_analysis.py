import re
from collections import Counter

import pandas as pd
from wordcloud import WordCloud

# Stopword sederhana Bahasa Indonesia & Inggris
STOPWORDS = {
    "yang","dan","di","ke","dari","untuk","ini","itu","dengan","karena",
    "atau","juga","ada","sudah","agar","saya","aku","kami","kamu",
    "the","is","are","a","an","of","to","in","on","for","and"
}


def clean_text(text):
    text = str(text).lower()

    # hapus url
    text = re.sub(r"http\S+", "", text)

    # hapus mention
    text = re.sub(r"@\w+", "", text)

    # hapus angka
    text = re.sub(r"\d+", "", text)

    # hapus tanda baca
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # hapus spasi berlebih
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def tokenize(text):

    text = clean_text(text)

    words = text.split()

    words = [
        w for w in words
        if len(w) > 2 and w not in STOPWORDS
    ]

    return words


def get_text(df):

    return " ".join(
        df["review_text"]
        .fillna("")
        .astype(str)
    )


def generate_wordcloud(df):

    text = get_text(df)

    text = " ".join(tokenize(text))

    wc = WordCloud(
        width=1000,
        height=500,
        background_color="white",
        collocations=False
    ).generate(text)

    return wc


def top_words(df, top_n=20):

    text = get_text(df)

    words = tokenize(text)

    counter = Counter(words)

    result = (
        pd.DataFrame(
            counter.most_common(top_n),
            columns=["Word","Frequency"]
        )
    )

    return result


def review_length(df):

    temp = df.copy()

    temp["Length"] = (
        temp["review_text"]
        .fillna("")
        .astype(str)
        .str.split()
        .str.len()
    )

    return temp