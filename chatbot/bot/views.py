# Create your views here.
import json
import requests, random, re

import random

# from chatbot.chatbot import word_utils

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.apps import apps
from . import word_utils

VERIFY_TOKEN = "c735ab9888f151a3721996bef579848694c922b44628dfe489" # generated above
FB_ENDPOINT = 'https://graph.facebook.com/v13.0/'
PAGE_ACCESS_TOKEN = "EAAE3KGhIo6EBAEZC2EE1ZBr5SMYQlLBHkrjF8rvHWyJXgc2AM70Isfz4Bdf4xaB4NlSQ7v8z9GtudlNu7BfJSP4O0SWUIJWII93c8Qg95G2hjhZCU6Sz6vZAMxRxNrZCZAx9w57DYIUzqnesdwyCzZBGa0y1tutnYiyOCyzBbKZAjsDkVpCJdA7r"  


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

        msg = """ น้องบอทไม่เข้าใจ 😢
พิมพ์เลขของหัวข้อที่อยากรู้ได้เลยน้า
1. กฎหมายที่สำคัญ
2. การฝากร้าน
3. ขั้นตอนการจดทะเบียนพาณิชย์ค้าขายออนไลน์
4. เริ่มต้นเปิดร้าน
5. ร้านแบบไหนต้องจดทะเบียนอิเล็กทรอนิกส์
6. กม.ขายของออนไลน์กับกม.คุ้มครองผู้บริโภค
7. สินค้าที่ห้ามขายออนไลน์
8. รายละเอียดที่ต้องแสดงในการขาย
9. การเสียภาษี
10. การขายตรงได้ไหม
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