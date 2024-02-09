import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


class PreProcessor:
    tokens = []
    stop_words = []

    def __init__(self, file_data):
        nltk.download('punkt')
        tokens = word_tokenize(file_data, "russian")
        nltk.download('stopwords')
        stop_words = set(stopwords.words("russian"))
        tokens = [word for word in tokens if word not in stop_words]
        stemmer = SnowballStemmer("russian")
        tokens = [stemmer.stem(word) for word in tokens]
        print(tokens)
