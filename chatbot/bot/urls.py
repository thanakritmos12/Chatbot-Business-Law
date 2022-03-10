from django.urls import re_path
from django.contrib import admin
from .views import (FacebookWebhookView)
app_name ='bot_webhooks'
urlpatterns = [re_path(r'^dc9e0bcaaa959b52f361bd1cc41f0b0b3f63ed357215c4601200e43107d8/$', FacebookWebhookView.as_view(), name='webhook'),]