import nltk
import pythainlp
import pprint
import deepcut
import random


def clean_words(words):
    # stopwords = pythainlp.corpus.common.thai_stopwords()
    # stopwords = ['', ' ', ',', '.', 'หรือไม่', 'มั้ย', 'ไหม', 'ยังไง', 'ยัง', 'ไง', 'ใหม', 'มัํย', 'มั่ย', 'บ้าง', 'นะ', 'หนา', 'บ้างไม', 'ไม']
    data = []
    for word in words:
        data = word.strip()
    return data


def get_features(data):
    # words = pythainlp.word_tokenize(data, engine='multi_cut')
    words = pythainlp.word_tokenize(data, engine='deepcut')
    # words = pythainlp.syllable_tokenize(data)
    words = clean_words(words)
    data = {"words": " ".join(words), "count": len(words)}
    return data
