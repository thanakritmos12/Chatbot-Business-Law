import nltk
import pprint
import random
import pandas
import pathlib
import pickle
import sys

sys.path.append('.')

from chatbot.bot import word_utils


path = pathlib.Path(__file__).parent.parent

    # prepare data
dfs = pandas.read_excel(path/"data/response.xlsx")

responses = {}
for df in dfs.to_dict("records"):
    if df["tag"] not in responses:
        responses[df["tag"]] = []
    responses[df["tag"]].append(df["response"])

pprint.pprint(responses)
## To load later:
f = open("data/my_classifier.pickle", "rb")
classifier = pickle.load(f)
f.close()

while True:
    q = input("Type: ")
    if q == "quit":
        break
    feature = word_utils.get_features(q)
    print(feature)
    result = classifier.prob_classify(feature)
    print("prob ->", result.max(), round(result.prob(result.max()), 2))
    if result.prob(result.max()) < 0.55 or 'ตอบไม่ตรง' in q:
        print(""" ไม่เข้าจายย พิมพ์ตามหัวข้อนี้หน่อยน้า
        1. กฎหมายที่สำคัญ
        2. การฝากร้าน
        3. ขั้นตอนการจดทะเบียนพาณิชย์ค้าขายออนไลน์
        4. เริ่มต้นเปิดร้าน
        5. ร้านแบบไหนต้องจดทะเบียนอิเล็กทรอนิกส์
        6. กม.ขายของออนไลน์กับกม.คุ้มครองผู้บริโภค
        7. สินค้าที่ห้ามขายออนไลน์
        8. รายละเอียดที่ต้องแสดงในการขาย
        9. การเสียภาษี
        10. การขายตรง
        """)
        continue

    
    print("ans:", random.choice(responses[result.max()]))