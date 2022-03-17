import pythainlp
import deepcut
# from pythainlp.tokenize import sent_tokenize
def clean_words(words):
    stopwords = pythainlp.corpus.common.thai_stopwords()
    # stopwords = ['', ' ', ',', '.', 'หรือไม่', 'มั้ย', 'ไหม', 'ยังไง', 'ยัง', 'ไง', 'ใหม', 'มัํย', 'มั่ย', 'บ้าง', 'นะ', 'หนา', 'บ้างไม', 'ไม', 'ๆ', 'ปะ', 'ครับ', 'คับ', 'ค่ะ', 'คะ', 'ค้ะ', 'ค้า', 'ค้าบ']
    data = []
    for word in words:
        word = word.strip()

        if word not in stopwords:
            data.append(word)
    # data = []
    # for word in words:
    #     data = word.strip()
    return data


def get_features(data):
    words = deepcut.tokenize(data)
    # words = pythainlp.word_tokenize(data, engine='longest')
    # words = pythainlp.word_tokenize(data, engine='deepcut')
    # words = sent_tokenize(data)
    # words = pythainlp.syllable_tokenize(data)
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
