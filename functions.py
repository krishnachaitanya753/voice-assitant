import openai 
import playsound
import speech_recognition as sr
from gtts import gTTS
import requests
import pywhatkit as pwk
import datetime
import os
import pyautogui
import webbrowser
import keyboard
from time import sleep

def openexe(query):
    Query = str(query).lower()
    if"visit" in query:
        nameofweb = query.replace("visit","").strip()
        link = f"https://www.{nameofweb}.com"
        webbrowser.open(link)
    elif "open" in query:
        nameofapp = query.replace("open","")
        if("chrome" in nameofapp):
            os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        else:
            pyautogui.press('win')
            keyboard.write(nameofapp)
            keyboard.press('enter')
            return True
    elif 'start' in query:
        nameofapp = query.replace("start","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
chaithu = "+917330851632"
def whatsapp(message):
    current_time = datetime.datetime.now().time()
    hour = current_time.hour
    minute = current_time.minute
    try:
     pwk.sendwhatmsg(chaithu,message, hour, minute+1)

     print("Message Sent!")
    except: 
        print("Error in sending the message")

def weather():
    api_key = '7cce94d4cd89b089218951553647dd5e'
    city = 'Hyderabad'
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'

    response = requests.get(url)
    data = response.json()
    # Extracting relevant information
    location_name = data['location']['name']
    country = data['location']['country']
    temperature = data['current']['temperature']
    weather_descriptions = data['current']['weather_descriptions']
    wind_speed = data['current']['wind_speed']
    pressure = data['current']['pressure']
    humidity = data['current']['humidity']

    # Creating a text response
    response = f"The current weather in {location_name}, {country} is {temperature}°C with {', '.join(weather_descriptions)}. "
    response += f"The wind speed is {wind_speed} km/h. The atmospheric pressure is {pressure} hPa and the humidity is {humidity}%."

    print(response)
    return response

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    try:
        tts.save(filename)
        playsound.playsound("D:\\junior_project\\voice.mp3")
    except Exception as e:
        print("Exception:", e)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception:", e)
    return said

def chatGpt(text):
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
        {"role": "system", "content": "You are an Ai who acts as Assistant"},
        {"role": "user", "content": "f You don't Know the answer  about Realtime time data or the data you haven't been trained on try to give an answer"},
        {"role": "assistant","content":"Sure I'll try to cover up the answer "},
        {"role": "user", "content": text}
    ], 
        max_tokens=3800,     
        stop=None,             
        temperature=0.7,        
    )
    x =  response.choices[0].message.content
    print(x)
    return x

def gpt_3(input):
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
        {"role": "system", "content": "classify the text in which category it falls for performing a task return 1 for regarding realtime weather or temparature etc return 2 for sending some one a whatsapp message return 3 for opening any application in laptop or visting or opening a website and return 4 for any gpt3 answerable task "},
        {"role": "user", "content": " Open google chrome or start the vscode or launch the mxplayer app"},
        {"role": "assistant","content":"3"},
        {"role": "user", "content": " Send whatsapp message of telling him to cook the meal for tonight to laddu "},
        {"role": "assistant","content":"2"},
        {"role": "user", "content": "how is the weather today"},
        {"role": "assistant","content":"1"},
        {"role": "user", "content": input}
    ], 
        max_tokens=3800,     
        stop=None,             
        temperature=0.7,        
    )
    x =  response.choices[0].message.content
    return x

def main(text):
    if(len(text)<3):
        return "Speak once again"
    number = gpt_3(text)
    print(number)
    if number == "1":
        return weather()
    elif number == "2":
        whatsapp("hello bro")
    elif number == "3":
        print("yes")
        openexe(text)
    else:
        return chatGpt(text)
