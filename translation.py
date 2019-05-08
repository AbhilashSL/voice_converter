import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS 
import os


def translator() :
    
    #input language
    str_input1 = input("What is the source language?? ")
    #str_input1 = 'en'
    
    #English to Malayalam speech
    if str_input1 == 'en':
         #Speech to text
        r = sr.Recognizer()
        voice_data = sr.AudioFile('Recording (autosaved).wav')
        with voice_data as source:
            audio = r.record(source)
        type(audio)
        x = r.recognize_google(audio, language='en-EN')
        print("Input String = "+x)
        
         #Text to speech
        translator = Translator()
        y=translator.translate(x,dest='ml')
        print("Source_lang = "+y.src,"Target_lang = "+y.dest)
        print("Translated String = "+y.text)
        mytext = y.text
        language = 'ml'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("mal_audio.mp3") 
        os.system("mpg321 mal_audio.mp3") 
    
    #Malayalam to English speech 
    elif str_input1 == 'ml':
         #Speech to text
        r = sr.Recognizer()
        voice_data = sr.AudioFile('Recording (autosaved) (2).wav')
        with voice_data as source:
            audio = r.record(source)
        type(audio)
        x = r.recognize_google(audio, language='ml-ML')
        print("Input String = "+x)
        
         #Text to speech
        translator = Translator()
        y=translator.translate(x,dest='en')
        print("Source_lang = "+y.src,"Target_lang = "+y.dest)
        print("Translated String = "+y.text) 
        mytext = y.text
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("eng_audio.mp3") 
        os.system("mpg321 eng_audio.mp3") 
      
    #invalid 
    else :
        print("invalid entry!!")

