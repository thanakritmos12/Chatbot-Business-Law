import pythainlp
import deepcut
# from pythainlp.tokenize import sent_tokenize


def clean_words(words):
    # stopwords = pythainlp.corpus.common.thai_stopwords()
    stopwords = ['กฎหมาย','กฏหมาย','บ้าง', 'ไหม', 'มั้ย', 'ไม', 'ร้านค้า', 'ร้าน',
     'ค้า', 'กฎ', 'การ', 'ความ', 'ใน', 'ที่', 'ต่างๆ', 'ได้', 'อย่าง','ออนไลน์','online','ขาย' ,
     'ไง','อ้ะ', 'หรอ', 'อะไร', 'อยู่', 'อยาก', 'ทราบ', 'ของ', 'ป่าว', 'เรา', 'เลย', 'จ้า', 'ครับ', 'ค้าบ', 'ค่ะ', 'คับ','ค่าบ']
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
    #  1
    features['ข้อหนึ่ง'] = 'สำคัญ' in words or 'สำคัญๆ' in words or 'ควรรู้' in words or 'รู้' in words or 'ต้องรู้' in words or 'ต้อง' in words or 'ทราบ' in words or 'ควรทราบ' in words or 'เกี่ยวข้อง' in words or 'ออนไลน์' in words or 'online' in words or 'กำหนด' in words or '1' in words

    # ข้อ 2
    features['ข้อสอง'] = 'แชร์รูปภาพ' in words or 'แชร์ภาพ' in words or 'ข้อความ' in words or 'สาธารณะ' in words or 'ฝากร้าน' in words or 'โปรโมท' in words or 'โพส' in words or 'แชร์' in words or 'แชร์โพสต์' in words or 'แชร์โพส' in words or 'แช' in words or 'share' in words or 'post' in words or 'link' in words or 'ภาพ' in words or 'กลุ่ม' in words or 'แนะนำ' in words or 'ฝาก' in words or 'แชร์ร้าน' in words or 'แชร้าน' in words or 'โฆษณา' in words or '2' in words

    # ข้อ 3
    features['ข้อสาม'] = 'พานิชย์' in words or 'จดทะเบียนพานิชย์' in words or 'ทะเบียนพานิชย์' in words or 'ทะเบียนการค้า' in words or 'ทะเบียนค้าขาย' in words or 'ทะเบียนซื้อขาย' in words or 'ขั้นตอน' in words or 'จด' in words or 'ทะเบียน' in words or 'พาณิชย์' in words or 'พาณิช' in words or 'เบียน' in words or 'จดทะเบียน' in words or '3' in words or 'วิธี' in words

    # ข้อ 4
    features['ข้อสี่'] = 'เริ่ม' in words or 'ขั้นแรก' in words or 'ก่อนขาย' in words or 'เตรียม' in words or 'สร้าง' in words or 'เริ่มต้น' in words or 'ก่อน' in words or 'เปิด' in words or 'สร้าง' in words or 'แรก' in words or 'อยาก' in words or '4' in words

    # ข้อ 5
    features['ข้อห้า'] = 'อิเล็กทรอนิกซ์' in words or 'อิเล็กทรอนิก' in words or 'อิเล็กทรอนิกส์' in words or 'DBD' in words or 'dbd ' in words or 'registered' in words or 'Registered' in words or 'แบบ' in words or 'ลักษณะ' in words or 'ประ' in words or 'เภท' in words or 'ประเภท' in words or 'shopee' in words or 'lazada' in words or 'electronic' in words or 'electronics' in words or 'Electronic' in words or 'Electronics' in words or '5' in words

    # ข้อ 6 
    features['ข้อหก'] = 'คุ้มครอง' in words or  'กฎหมายคุ้มครอง' in words or 'ผู้บริโภค' in words or 'สคบ.' in words or 'สตบ.' in words or 'บริโภค' in words or 'ลูกค้า' in words or 'ลูก' in words or 'ค้า' in words or 'สคบ' in words or 'สตบ' in words or '6' in words

    # ข้อ 7
    features['ข้อเจ็ด'] = 'ห้าม' in words or 'ผิด' in words or 'ลักลอบ' in words or 'อันตราย' in words or 'ต้องห้าม' in words or 'ไม่' in words or 'คุก' in words or 'ระวัง' in words or '7' in words
 
    # ข้อ 8
    features['ข้อแปด'] = 'รายละเอียด' in words or 'ข้อมูล' in words or 'แสดง' in words or 'โชว์' in words or 'ประวัติ' in words or 'รายละเอียดร้าน' in words or 'ราคา' in words or '8' in words

    # ข้อ 9
    features['ข้อเก้า'] = 'ภาษี' in words or 'จ่าย' in words or 'โดน' in words or '9' in words

    # ข้อ 10
    features['ข้อสิบ'] = 'ขาย' in words or 'ขายตรง' in words or 'ตรง' in words or 'ตลาด' in words or 'ตลาดตรง' in words or '10' in words

    # ทักทาย
    features['ทักทาย'] = 'สวัสดี' in words or 'หวัดดี' in words or 'ดีจ้า' in words or 'ค้า' in words or 'ฮัลโหล' in words or 'โหล' in words or 'โย่' in words or 'ไง' in words or 'โหลๆ' in words or 'Hi' in words or 'Hello' in words or 'Yeah' in words or 'Sup' in words or 'Yo' in words or 'Hey' in words or 'up' in words or 'Yea' in words or 'Yess' in words or 'Yes' in words or 'Yep' in words or 'What' in words or 'bot' in words or 'ดีบอท' in words or 'บอท' in words or 'สวัสดีบอท' in words or 'หวัดดีบอท' in words or 'ไงบอท' in words

    # สบายดี
    features['สบายดี'] = 'สบาย' in words or 'บาย' in words or 'บัย' in words or 'สบายดี' in words

    # บอทโง่
    features['บอทโง่'] = 'ตอบผิด' in words or 'ห้ะ' in words or 'ตอบ' in words or 'งง' in words or 'มั่ว' in words or 'เพ้อ' in words

    # ชมบอท
    features['ชมบอท'] = 'เก่งมาก' in words or 'เก่ง' in words or 'ดีมาก' in words or 'ดี' in words or 'มาก' in words or 'เยี่ยม' in words 

    # ทำอะไร
    features['ทำอะไร'] = 'ทำอะไร' in words or 'ทำ' in words or 'ทำไร' in words

    # ชื่ออะไร
    features['ชื่ออะไร'] = 'ชื่อ' in words or 'ชื่ออะไร' in words

    # หัวข้อ
    features['หัวข้อ'] = 'หัวข้อ' in words

    # ยินดี
    features['ยินดี'] = 'ขอบคุณ' in words or 'ขอบคุณบอท' in words or 'ขอบใจ' in words or 'ขอบใจบอท' in words or 'ขอบคุน' in words

    # คำถาม
    features['ถามหน่อย'] = 'มีคำถาม' in words or 'มีคำถามจะมาถาม' in words or 'ถามหน่อย' in words or 'ขอถามหน่อย' in words or 'ขอถาม' in words or 'ถาม' in words or 'สงสัย' in words

    data = {"words": " ".join(words), "count": len(words)}
    data.update(features)
    return data 