from email import message
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import chatbot_history
from django.views.generic import TemplateView

# import mysql.connector as sql
from django.contrib import messages
from django.contrib.auth import authenticate, login
from SignUp.models import IlkmsUser
#from django.contrib.auth.models import IlkmsUser
# Create your views here.
import random
import json
import pickle
import numpy as np
import streamlit as st
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from gtts import gTTS
from playsound import playsound
from tensorflow.keras.models import load_model 
import os
from streamlit_chat import message as st_message
import time
from PIL import Image
from django.core import serializers

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD 

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('../ILKMS_project/chatbot/intents_banglish.json', 'r', encoding='utf-8').read())

words = pickle.load(open('../ILKMS_project/chatbot/words.pkl', 'rb'))
classes = pickle.load(open('../ILKMS_project/chatbot/classes.pkl', 'rb'))
model = load_model('../ILKMS_project/chatbot/chatbot_model.model')

            
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    result = [[i, r] for i, r in enumerate(res) if r>ERROR_THRESHOLD]
    result.sort(key=lambda x:x[1], reverse=True)
    
    return_list = []
    
    for r in result:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    
    return return_list


def get_response(intents_list, intents_json):
    if intents_list == []:
        print("Sorry, I didn't get you.")
    else:
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['response'])
                break
        return result



msg = ''
res = ''


def chatbot_res(request):

    if request.method == "POST":
        msg = request.POST['msg']


        ints = predict_class(msg)

        res = get_response(ints, intents)
        print(res)

        chatbot_history(req=msg, res=res).save()


        
        # res_data = json.dumps(res_data)
        # print(data)
    data = chatbot_history.objects.values()
    return render(request, "ILKMS_project/chatbotUI.html", {'data': data})
    # return render(request, "ILKMS_project/chatbotUI.html")



# def chat_his(request):
#     data = chatbot_history.objects.values()
#     return render(request, "ILKMS_project/chatbotUI.html", {'res_data': data})

