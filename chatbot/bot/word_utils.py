import pythainlp
import deepcut
# from pythainlp.tokenize import sent_tokenize
def clean_words(words):
    stopwords = pythainlp.corpus.common.thai_stopwords()
    data = []
    for word in words:
        word = word.strip()
        if word not in stopwords:
            data.append(word)
    return data


def get_features(data):
    words = deepcut.tokenize(data)
    words = clean_words(words)
    features = {}
    features['กฎหมาย'] = 'กฎหมาย' in words
    features['ร้านค้า'] = 'ร้านค้า' in words or 'ออนไลน์' in words or 'online' in words
    features['ห้าม'] = 'ห้าม' in words
    features['ภาษี'] = 'ภาษี' in words
    features['โทษ'] = 'โทษ' in words or 'คุก' in words or 'หราง' in words
    data = {"words": " ".join(words), "count": len(words)}
    data.update(features)
    return data
