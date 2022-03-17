# Create your views here.
import json
import requests, random, re
import pprint
import random
import pandas
import word_utils
import pickle

from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .logic import LOGIC_RESPONSES


VERIFY_TOKEN = "c735ab9888f151a3721996bef579848694c922b44628dfe489" # generated above
FB_ENDPOINT = 'https://graph.facebook.com/v12.0/'
PAGE_ACCESS_TOKEN = "EAAE3KGhIo6EBAKok7UJZAAA45D0aqgRxrCvZBeZBQZBnhHrOSy9MqrlW317cPYTJSJzGtkhGfTDvEJX4hrrgS32xSbvhznEV3Irez1xBpwYvdtZBjvkZBaho1Je63NGtCg23fGQwE7Uy2x9wAMZBqzLlVo1xIAqzMMJ9GOQJ5ZCEUkI6XZC0s4gPX"  

def parse_and_send_fb_message(fbid, recevied_message):
    dfs = pandas.read_excel("response.xlsx")

    responses = {}
    for df in dfs.to_dict("records"):
        if df["tag"] not in responses:
            responses[df["tag"]] = []
        responses[df["tag"]].append(df["response"])

    f = open("my_classifier.pickle", "rb")
    classifier = pickle.load(f)
    f.close()

    message_fb = recevied_message.lower().split()
    feature = word_utils.get_features(message_fb)
    result = classifier.prob_classify(feature)

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