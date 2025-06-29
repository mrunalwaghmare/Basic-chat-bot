# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:47:00 2024

@author: Mrunal
"""

import sqlite3
from tkinter import *
import tkinter as tk
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
from tkinter import messagebox
from tkinter import ttk
import os
from gtts import gTTS


responses ={
    "hi":"hello!",
    "hello":"Hi there!",
    "how are you":"I am a chat bot, I don't have feelings but thanks for asking",
    "what is your name":"I am chatbot ,your assistant",
    "bye":"Goodbye!"
    }

#initialize text to speech
engine = pyttsx3.init()

#initialize the translator
translator = Translator()

def speak(text,lang='en'):
    tts = gTTS(text=text,lang=lang,slow=False)
    tts.save("response.mp3")
    os.system("start response.mp3")
    # engine.say(text)
    # engine.runAndWait()

def get_response(user_input):
    user_input=user_input.lower()
    
    return responses.get(user_input," I dont unserstand that can you rephrase?")

def send_message():
    user_message = user_input.get()
    
    if user_message:
        chat_log.config(state='normal')
        chat_log.insert(tk.END,"You : "+user_message+"\n")
        
        bot_response = get_response(user_message)
        
        chat_log.insert(tk.END,"Bot : "+bot_response+"\n\n")
        
        chat_log.config(state='disabled')
        user_input.delete(0,tk.END)


def clear_chat():
    chat_log.config(state='normal')
    chat_log.delete(1.0,tk.END)
    chat_log.config(state='disabled')

def Initialize_chat():
    chat_log.config(state='normal')
    chat_log.insert(tk.END,"Bot: HI HOW CAN I HELP YOU TODAY?\n\n")
    chat_log.config(state='disabled')


def voice_input():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        chat_log.config(state='normal')
        chat_log.insert(tk.END,"listening..\n")
        chat_log.config(state='disabled')
        
        audio = recognizer.listen(source)
        
        try:
            text =  recognizer.recognize_google(audio)
            
            user_input.delete(0,tk.END)
            user_input.insert(0,END)
            send_message()
            
        except sr.UnknownValueError:
            chat_log.config(state='normal')
            chat_log.insert(tk.END, "Sorry i didnt understant that\n")
            chat_log.config(state='disabled')
            
        except sr.RequestError:
            chat_log.config(state="normal")
            chat_log.insert(tk.END, "sorry my speech service is down.\n")
            chat_log.config(state='disabled')

 
def eng_hi():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.record(source,duration=5)
            text = recognizer.recognize_google(audio_data,language='hi')
            print("Recognize text:",text)
            translated_text = translator.translate(text,src='hi',dest='en').text
            print("translated text:",translated_text)
            response = get_response(translated_text)
            print("response:",response)
            translated_response = translator.translate(response,src='en',dest='hi').text
            print("translated_response:",translated_response)
            
            chat_log.config(state='normal')
            chat_log.insert(tk.END, "You:"+text+"\n")
            chat_log.insert(tk.END, "Bot:"+translated_response+"\n\n")
            chat_log.config(state='disabled')
            user_input.delete(0,tk.END)
            
            speak(translated_response,lang='hi')
            
            
        except sr.UnknownValueError:
            chat_log.config(state='normal')
            chat_log.insert(tk.END,"bot: Sorry i did not understand that.\n")
            chat_log.config(state='disabled')
            
            
        except sr.RequestError:
            chat_log.config(state='normal')
            chat_log.insert(tk.END, "Bot:Sorry my speech service is down.\n")
            chat_log.config(state='disabled')
            
            
  
def eng_mar():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.record(source,duration=5)
            text = recognizer.recognize_google(audio_data,language='mr')
            print("Recognize text:",text)
            translated_text = translator.translate(text,src='mr',dest='en').text
            print("translated text:",translated_text)
            response = get_response(translated_text)
            print("response:",response)
            translated_response = translator.translate(response,src='en',dest='mr').text
            print("translated_response:",translated_response)
            
            chat_log.config(state='normal')
            chat_log.insert(tk.END, "You:"+text+"\n")
            chat_log.insert(tk.END, "Bot:"+translated_response+"\n\n")
            chat_log.config(state='disabled')
            user_input.delete(0,tk.END)
            
            speak(translated_response,lang='mr')
            
            
        except sr.UnknownValueError:
            chat_log.config(state='normal')
            chat_log.insert(tk.END,"bot: Sorry i did not understand that.\n")
            chat_log.config(state='disabled')
            
            
        except sr.RequestError:
            chat_log.config(state='normal')
            chat_log.insert(tk.END, "Bot:Sorry my sooech service is down.\n")
            chat_log.config(state='disabled')
            
    

#create main window
root = Tk()
root.title("welcome to chatbot")
root.geometry("400x500")
    

#text box widget for chat log
chat_log = tk.Text(root, width=50, height=20, state='disabled', bd=5, relief='solid')
chat_log.place(x=400, y=10)

#entry box
user_input=Entry(root,font=('Arial',12))
user_input.place(x=500,y=400)

#send button
send_button=Button(root,text="Send",width=12,height=1,command=send_message)
send_button.place(x=700,y=400)

#clear button
clear_button=Button(root,text="Clear chat",width=12,height=1,command=clear_chat)
clear_button.place(x=800,y=400)

#voice button

voice_button=Button(root,text="Voice",width=12,height=1,command=voice_input)
voice_button.place(x=900,y=400)

hindi_voice = Button(root,text='Hindi voice',width=12,height=1,command=eng_hi)
hindi_voice.place(x=1000,y=400)

mar_voice = Button(root,text='Marathi voice ',width=12,height=1,command=eng_mar)
mar_voice.place(x=1000,y=500)

#bind return key to send message
root.bind('<Return>',lambda event:send_message())
#intialize chat with welcome message
Initialize_chat()


root.mainloop()