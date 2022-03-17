# Create your views here.
import json
import requests, random, re
import pprint
import random
import pandas
# from chatbot.chatbot import word_utils
import pickle
import os
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import pathlib
from django.apps import apps
from django.conf import settings

VERIFY_TOKEN = "c735ab9888f151a3721996bef579848694c922b44628dfe489" # generated above
FB_ENDPOINT = 'https://graph.facebook.com/v12.0/'
PAGE_ACCESS_TOKEN = "EAAE3KGhIo6EBAKok7UJZAAA45D0aqgRxrCvZBeZBQZBnhHrOSy9MqrlW317cPYTJSJzGtkhGfTDvEJX4hrrgS32xSbvhznEV3Irez1xBpwYvdtZBjvkZBaho1Je63NGtCg23fGQwE7Uy2x9wAMZBqzLlVo1xIAqzMMJ9GOQJ5ZCEUkI6XZC0s4gPX"  
from . import word_utils
import pythainlp



def parse_and_send_fb_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    # tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    # print(settings.__dict__)
    classifier = apps.get_app_config('bot').classifier
    responses = apps.get_app_config('bot').responses
    
    message_fb = recevied_message
    feature = word_utils.get_features(message_fb)
    result = classifier.prob_classify(feature)
    if result.prob(result.max()) < 0.4:

        msg = """ ไม่เข้าจายย พิมพ์ตามหัวข้อนี้หน่อยน้า
        1. กฎหมายที่สำคัญ
        2. การแชร์รูปภาพหรือข้อความต่างๆ เกี่ยวกับร้านค้าออนไลน์ของตนในพื้นที่โซเซียลมีดีของผู้อื่นผิดกฎหมายหรือไม่
        3. ขั้นตอนการจดทะเบียนพาณิชย์ในการค้าขายออนไลน์มีอะไรบ้าง
        4. การเปิดร้าน
        5. กฎหมายเกี่ยวกับการขายของออนไลน์มีไว้ทำไม
        6. กฎหมายขายของออนไลน์เกี่ยวข้องอย่างไรกับกฎหมายคุ้มครองผู้บริโภค
        7. สินค้าที่ห้ามขายออนไลน์
        8. ร้านค้าออนไลน์ควรแสดงรายละเอียด
        9. ร้านค้าออนไลน์ต้องเสียภาษีอย่างไร
        10. ร้านค้าออนไลน์จะขายตรงและตลาดแบบตรงได้หรือไม่
        """
    else :
        msg = random.choice(responses[result.max()])
        
    if msg is not None:                 
        endpoint = f"{FB_ENDPOINT}/me/messages?access_token={PAGE_ACCESS_TOKEN}"
        response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":msg}})
        status = requests.post(
            endpoint, 
            headers={"Content-Type": "application/json"},
            data=response_msg)
        print(status.json())
        return status.json()
    return None

        
        
class FacebookWebhookView(View):
    @method_decorator(csrf_exempt) # required
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) #python3.6+ syntax
    
    def get(self, request, *args, **kwargs):
        hub_mode   = request.GET.get('hub.mode')
        hub_token = request.GET.get('hub.verify_token')
        hub_challenge = request.GET.get('hub.challenge')
        if hub_token != VERIFY_TOKEN:
            return HttpResponse('Error, invalid token', status_code=403)
        return HttpResponse(hub_challenge)
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse("Hello, World!")
            
    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    fb_user_id = message['sender']['id'] # sweet!
                    fb_user_txt = message['message'].get('text')
                    if fb_user_txt:
                        parse_and_send_fb_message(fb_user_id, fb_user_txt)
        return HttpResponse("Success", status=200)