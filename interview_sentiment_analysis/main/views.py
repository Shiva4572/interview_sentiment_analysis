from django.conf import settings
from main.models import admin
import speech_recognition as sr

from django.shortcuts import render

import base64
from io import BytesIO
import matplotlib.pyplot as plt




# Create your views here.

def main(request):
    return render(request,"upload_file.html")

def upload_file(request):
    import json
    from ibm_watson import NaturalLanguageUnderstandingV1
    from ibm_watson.natural_language_understanding_v1 import(Features,EntitiesOptions,KeywordsOptions,SentimentOptions,EmotionOptions)
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator




    authenticator=IAMAuthenticator('aj7jipdjhmoCLYpaqr3lr1p30G65L7kaJA-AsFu72vaO')
    natural_language=NaturalLanguageUnderstandingV1(
                version='2022-04-07',
                authenticator=authenticator)
    natural_language.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/27a81d2e-4d6b-4dcd-aaa4-9bb1222306db')






    if request.method=="POST":
        text_1 = request.POST["data"]


    response=natural_language.analyze(
                text=text_1,
                #content_type="audio/mp3",
                features=Features(sentiment=SentimentOptions(),emotion=EmotionOptions())
                #features=Features(entities=EntitiesOptions(emotion=True,sentiment=True),keywords=KeywordsOptions(emotion=True,sentiment=True))
               
            ).get_result()
   

    


    sentiment = response['emotion']['document']['emotion']
    anger = response['emotion']['document']['emotion']['anger']
    sadness=response['emotion']['document']['emotion']['sadness']
    joy=response['emotion']['document']['emotion']['joy']
    fear=response['emotion']['document']['emotion']['fear']
    disgust=response['emotion']['document']['emotion']['disgust']


    score=response['sentiment']['document']['score']
    label = response['sentiment']['document']['label']

   

   
    
   




    # Render the HTML template with the chart data
    return render(request, 'analysis.html', {'Anger':anger, 'Sadness' : sadness, 'Joy' : joy, 'Fear' :fear, 'Disgust' : disgust,"text" : text_1,"score":score,"label":label})






