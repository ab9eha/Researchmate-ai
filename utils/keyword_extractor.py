from sklearn.feature_extraction.text import CountVectorizer


def extract_keywords(text, top_n=15):

    vectorizer = CountVectorizer(
        stop_words="english",
        max_features=top_n
    )

    X = vectorizer.fit_transform([text])

    keywords = vectorizer.get_feature_names_out()

    return list(keywords)