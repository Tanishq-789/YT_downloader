from sklearn.feature_extraction.text import CountVectorizer

def extract_keywords(text):
    vectorizer = CountVectorizer(max_features=5, stop_words='english')
    keywords = vectorizer.fit_transform([text]).toarray()
    return vectorizer.get_feature_names_out()