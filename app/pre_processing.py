import os
import string
from langdetect import detect
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def detect_punctuation(word):
    for ch in word:
        if ch in string.punctuation:
            return True
    return False


def detect_numbers(word):
    for ch in word:
        if ch.isdigit():
            return True
    return False


def detect_notalpha(word):
    for ch in word:
        if not ch.isalpha():
            return True
    return False


def detect_foreign_or_special(word):
    if detect_punctuation(word) or detect_numbers(word) or detect_notalpha(word):
        return True
    return not detect(word) == 'ru'


class PreProcessor:
    tokens = []
    stop_words = []

    def __init__(self, text):
        if text is None:
            return
        nltk.download('punkt')
        self.tokens = word_tokenize(text, "russian")
        nltk.download('stopwords')
        stop_words = set(stopwords.words("russian"))
        self.tokens = [token for token in self.tokens if not detect_punctuation(token) or len(token) > 1]
        self.tokens = [word for word in self.tokens if word not in stop_words]
        stemmer = SnowballStemmer("russian")
        self.tokens = [stemmer.stem(word) if detect_foreign_or_special(word) else word for word in self.tokens]
