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
    # ข้อ 1
    features['กฎหมาย'] = 'กฎหมาย' in words or 'สำคัญ' in words or 'ต้อง' in words or 'รู้' in words
    features['ร้านค้า'] = 'ร้านค้า' in words or 'ออนไลน์' in words or 'online' in words or 'ร้าน' in words or 'ค้า' in words

    # ข้อ 2
    features['แชร์'] = 'แชร์รูปภาพ' in words or 'แชร์ภาพ' in words or 'แชร์ข้อความ' in words or ['สาธารณะ'] in words or ['ฝากร้าน'] in words or ['โปรโมท'] in words

    # ข้อ 3
    features['พานิชย์'] = 'พานิชย์' in words or 'จดทะเบียนพานิชย์' in words or 'ทะเบียนพานิชย์' in words or 'ทะเบียนการค้า' in words or 'ทะเบียนค้าขาย' in words or 'ทะเบียนซื้อขาย' in words 

    # ข้อ 4
    features['เริ่ม'] = 'เริ่ม' in words or 'ขั้นแรก' in words or 'ก่อนขาย' in words or 'เตรียม' in words

    # ข้อ 5
    features['อิเล็กทรอนิก'] = 'อิเล็กทรอนิก' in words or 'อิเล็กทรอนิกซ์' in words or 'DBD Registered' in words or 'dbd registered' in words

    # ข้อ 6 
    features['คุ้มครอง'] = 'คุ้มครอง' in words or  'กฎหมายคุ้มครอง' in words or 'ผู้บริโภค' in words or 'สคบ.' in words or 'สตบ.' in words

    # ข้อ 7
    features['ห้าม'] = 'ห้าม' in words or 'ผิด' in words

    # ข้อ 8
    features['รายละเอียด'] = 'รายละเอียด' in words or 'ข้อมูล' in words or 'แสดง' in words or 'โชว์' in words

    # ข้อ 9
    features['ภาษี'] = 'ภาษี' in words or 'จ่าย' in words or 'โดน' in words

    # ข้อ 10
    features['ขาย'] = 'ขาย' in words or 'ขายตรง' in words or 'ตลาดตรง' in words
   
    data = {"words": " ".join(words), "count": len(words)}
    data.update(features)
    return data