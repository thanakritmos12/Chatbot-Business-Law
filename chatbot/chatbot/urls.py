from django.contrib import admin
from django.urls import path, include
app_name = 'bot_webhooks'
urlpatterns = [
path('bot/', include('bot.urls')),
]