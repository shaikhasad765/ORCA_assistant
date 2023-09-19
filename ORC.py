from ctypes.wintypes import MSG
from tkinter.constants import COMMAND
from turtle import update
from typing import BinaryIO
from jaraco.context import temp_dir
import pyttsx3
import requests
import speech_recognition as sr
import datetime
from datetime import timedelta
import wikipedia
import webbrowser
import os
import operator
import smtplib
import features
import speedtest
import cv2
import platform
import cpuinfo
import psutil
import random
from requests import get
import pywhatkit
import time
from time import sleep
import pyautogui
import sys
import requests
from bs4 import BeautifulSoup
import pyjokes
import pyautogui
from wikipedia.wikipedia import search
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from category_encoders import *
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pywikihow import WikiHow, search_wikihow
from pytube import YouTube
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
import winsound
import keyboard

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

def search_wikihow(query, max_results=10, lang="en"):
       return list(WikiHow.search(query, max_results, lang))

def alarm(Timing):
       altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
       altime = altime[11:-3]
       print(altime)
       Horeal = altime[:2]
       Horeal = int(Horeal)
       Mireal = altime[3:5]
       Mireal = int(Mireal)
       print(f"Done, alarm is set for {Timing}")

       while True:
              if Horeal==datetime.datetime.now().hour:
                     if Mireal==datetime.datetime.now().minute:
                            print("alarm is running")
                            winsound.PlaySound('abc',winsound.SND_LOOP)

                     elif Mireal<datetime.datetime.now().minute:
                            break

def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def wishMe():
       hour = int(datetime.datetime.now().hour)
       tt = time.strftime("%I:%M %p") 

       if hour>=0 and hour<12:
              print("Good Morning")
              speak("Good Morning!")

       elif hour>=12 and hour<18:
              print("Good Afternoon")
              speak("Good Afternoon!") 

       else:
              print("Good Evening")
              speak("Good Evening!")               

       print("I am ORCA Sir. Please tell me How may I help you")
       speak("I am ORCA Sir. Please tell me How may I help you")  

       #to send email
       def sendEmail(to, content):
              server = smtplib.SMTP('smtp.gmail.com', 587)
              server.ehlo()
              server.starttls()
              server.login('shaikhasad9991@gmail.com', 'Asad*786')
              server.sendmail('shaikhasad9991@gmail.com', to, content)
              server.close()

#for news updates
def news():
       main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3af5ccf214084ebcb9c397b668370a49'

       main_page = requests.get(main_url).json()
       articles = main_page["articles"]
       head = []
       day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
       for ar in articles:
              head.append(ar["title"])
       for i in range (len(day)):
              print(f"todays {day[i]} news is: {head[i]}")
              speak(f"todays {day[i]} news is: {head[i]}")              

# to read pdf files
def pdf_reader():
       print("Please enter the file name correctly")
       speak("Please enter the file name correctly")
       try:
              file = input("Please enter the file name: ")
              book = open(f"{file}", 'rb')
              pdfReader = PyPDF2.PdfFileReader(book)
              pages = pdfReader.numPages
              print(f"Total number of pages in this book are {pages} ")
              speak(f"Total number of pages in this book are {pages} ")
              speak("sir please enter the page number i have to read")
              pg = int(input("Please enter the page number: "))
              page = pdfReader.getPage(pg)
              text = page.extractText()
              print(text)
              speak(text)

       except Exception as e:
              print(f"sorry sir, i didn't found any file named {file}")
              speak(f"sorry sir, i didn't found any file named {file}")
              pass                               

class MainThread(QThread):
       def __init__(self):
              super(MainThread,self).__init__()

       def run(self):
              self.TaskExecution()

       def takeCommand(self):

              r = sr.Recognizer()
              with sr.Microphone() as source:
                     r.adjust_for_ambient_noise(source)
                     print("Listening...")
                     r.pause_threshold = 1
                     r.energy_threshold = 500
                     audio = r.listen(source,timeout=500,phrase_time_limit=8)

              try:
                     print("Recognizing...")
                     text = r.recognize_google(audio, language='en-IN')
                     print(f"User said: {text}\n")

              except Exception as e:
                     print(e)
                     print("Say that again please...")
                     return "None"
              return text

       def TaskExecution(self):
              pyautogui.press('esc')
              wishMe()
              while True:
                     self.query = self.takeCommand().lower()
                     
                     if "you can sleep now" in self.query or "sleep" in self.query or "sleep now" in self.query:
                            print("Thanks for using me sir, have a good day")
                            speak("Thanks for using me sir, have a good day")
                            break
                     
                     elif 'wikipedia' in self.query:
                            speak('Searching Wikipedia...')
                            self.query = self.query.replace("wikipedia", "")
                            results = wikipedia.summary(self.query, sentences=2)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

                     elif 'open youtube' in self.query:
                            print("opening youtube")
                            speak("opening youtube!")
                            webbrowser.open("youtube.com")

                     elif 'open stackoverflow' in self.query:
                            print("opening stackoverflow")
                            speak("opening stackoverflow!")
                            webbrowser.open("stackoverflow.com")

                     elif 'play music' in self.query:
                            print("playing music")
                            speak("playing music!")
                            self.music_dir = 'D:\\Music'
                            self.songs = os.listdir(self.music_dir)
                            rd = random.choice(self.songs)
                            print(rd)
                            os.startfile(os.path.join(self.music_dir, rd))

                     elif 'the time' in self.query:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            print(strTime)
                            speak(f"Sir, the time is {strTime}")

                     elif 'open Visual studio code' in self.query or 'open code' in self.query:
                            print("opening Visual studio code")
                            speak("opening Visual Studio Code!")
                            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                            os.startfile(codePath)

                     elif 'send email' in self.query:
                            try:
                                   print("sir what should i say")
                                   speak("sir what should i say")
                                   self.query = self.takeCommand()
                                   if "send a file" in self.query:
                                          email = 'shaikhasad9991@gmail.com'
                                          password = 'Asad*786'
                                          send_to_email = 'shaikhasad765@gmail.com'
                                          print("okay sir, what is the subject for this email")
                                          speak("okay sir, what is the subject for this email")
                                          self.query = self.takeCommand()
                                          subject = self.query
                                          print("and sir, what is the message for this email")
                                          speak("and sir, what is the message for this email")
                                          self.query2 = self.takeCommand()
                                          message = self.query2
                                          print("sir please enter the correct path of the file into the shell")
                                          speak("sir please enter the correct path of the file into the shell")
                                          file_location = input("please enter the path here: ")

                                          print("please wait, i am sending email now")
                                          speak("please wait, i am sending email now")

                                          msg = MIMEMultipart()
                                          msg['From'] = email
                                          msg['To'] = send_to_email
                                          msg['Subject'] = subject
                                          msg.attach(MIMEText(message, 'plain'))

                                          filename = os.path.basename(file_location)
                                          attachment = open(file_location, "rb")
                                          part = MIMEBase('application', 'octet-stream')
                                          part.set_payload(attachment.read())
                                          encoders.encode_base64(part)
                                          part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                                          msg.attach(part)

                                          server = smtplib.SMTP('smtp.gmail.com', 587)
                                          server.starttls()
                                          server.login(email, password)
                                          text = msg.as_string()
                                          server.sendmail(email, send_to_email, text)
                                          server.quit()
                                          print("Email has been sent")
                                          speak("Email has been sent")
                            except:
                                   speak("Please allow less secure apps permission on your gmail account")
                                   print("Please allow less secure apps permission on your gmail account")

                            else:
                                   try:
                                          email = 'shaikhasad9991@gmail.com'
                                          password = 'Asad*786'
                                          send_to_email = 'shaikhasad765@gmail.com'
                                          message = self.query      

                                          server = smtplib.SMTP('smtp.gmail.com', 587)
                                          server.starttls()
                                          server.login(email, password)
                                          server.sendmail(email, send_to_email, message)
                                          server.quit()
                                          print("email has been sent")
                                          speak("email has been sent")
                                   except:
                                          speak("Please allow less secure apps permission on your gmail account")
                                          print("Please allow less secure apps permission on your gmail account")
                                   pass
                            
                     elif 'open notepad' in self.query:
                            print("opening Notepad")
                            speak("opening Notepad!")
                            npath = "C:\\Windows\\notepad.exe"
                            os.startfile(npath)

                     elif 'open adobe reader' in self.query:
                            print("opening Adobe Reader")
                            speak("opening Adobe Reader!")
                            apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
                            os.startfile(apath)

                     elif 'open command prompt' in self.query:
                            print("opening command prompt")
                            speak("opening command prompt!")
                            os.system("start cmd")

                     elif 'open camera' in self.query:
                            try:     
                                   import cv2

                                   cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                                   while True:
                                          retrieve, frame = cap.read()
                                          cv2.imshow('Web camera(Press c to exit camera)', frame)
                                          
                                          if cv2.waitKey(20) & 0xFF == ord('c'):
                                                 break  
                                   cap.release()
                                   cv2.destroyAllWindows()
                            except:
                                   print("Camera is not connected")                                
                                   speak("Camera is not connected")         
                            pass                       

                     elif 'ip address' in self.query:
                            ip = get('https://api.ipify.org').text
                            speak(f"your IP address is {ip}")

                     elif 'thanks' in self.query:
                            print("You are welcome Sir")
                            speak("You are welcome Sir!")

                     elif 'open facebook' in self.query:
                            print("opening facebook")
                            speak("opening facebook!")
                            webbrowser.open("facebook.com")

                     elif 'search on google' in self.query:
                            print("What should i search on google")
                            speak("What should i search on google")
                            cm = self.takeCommand()
                            webbrowser.open(f"{cm}")

                     elif 'open google' in self.query:
                            print("opening Google")
                            speak("opening Google!")
                            webbrowser.open("google.com")

                     elif "send whatsapp message to" in self.query:
                            self.query = self.query.replace("send","")   
                            self.query = self.query.replace("whatsapp message","")
                            self.query = self.query.replace("to","")
                            name = self.query
                            from datetime import datetime
                            strTime = int(datetime.now().strftime("%H"))
                            update = int((datetime.now()+timedelta(minutes = 1)).strftime("%M"))

                            if 'mother' in name:
                                   speak(f"What's The Message For {name}")
                                   mess = self.takeCommand()
                                   pywhatkit.sendwhatmsg("+919545791886",mess,time_hour=strTime,time_min=update)

                            elif 'father' in name:
                                   speak(f"What's The Message For {name}")
                                   mess = self.takeCommand()
                                   pywhatkit.sendwhatmsg("+8446207156",mess,time_hour=strTime,time_min=update)
                                   
                            elif 'brother' in name:
                                   speak(f"What's The Message For {name}")
                                   mess = self.takeCommand()
                                   pywhatkit.sendwhatmsg("+919049006609",mess,time_hour=strTime,time_min=update)   
                                   
                            elif 'college official' in name:
                                   speak(f"What's The Message For {name}")
                                   mess = self.takeCommand()
                                   pywhatkit.sendwhatmsg_to_group("HT4Ny82Eu030yR6kN70FRy",mess,time_hour=strTime,time_min=update)   
                                   
                     elif "play song on youtube" in self.query:
                            print("which song do you want to play")
                            speak("which song do you want to play!")
                            z = self.takeCommand()
                            pywhatkit.playonyt(f"{z}")

                     elif "close notepad" in self.query:
                            print("Okay sir, Closing Notepad")
                            speak("Okay sir, Closing Notepad")
                            os.system("taskkill /f /im notepad.exe")
                                   
                     elif "alarm" in self.query:
                            try:
                                   print("sir please tell me the time to set alarm, for example, set alarm to 5.30 a.m./p.m.")
                                   speak("sir please tell me the time to set alarm, for example, set alarm to 5.30 a.m./p.m.")
                                   self.tt = self.takeCommand()
                                   self.tt = self.tt.replace("set alarm to ", "")
                                   self.tt = self.tt.replace("set alarm at ", "")
                                   self.tt = self.tt.replace(".","")
                                   self.tt = self.tt.upper()
                                   alarm(self.tt)

                            except Exception as e:
                                   print(e)
                                   print("sorry i didn't get that please try again")
                                   speak("sorry i didn't get that please try again")

                     elif "tell me a joke" in self.query:
                            joke = pyjokes.get_joke()
                            print(joke)
                            speak(joke)
              
                     elif "shut down the system" in self.query or "shutdown computer" in self.query or "shutdown the system" in self.query:
                            os.system("shutdown /s /t 5")

                     elif "restart the system" in self.query:
                            os.system("shutdown /r /t 5")

                     elif "system standby" in self.query:
                            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                     elif 'switch the window' in self.query:
                            pyautogui.keyDown("alt")
                            pyautogui.press("tab")
                            time.sleep(1)
                            pyautogui.keyUp("alt")

                     elif 'tell me news' in self.query:
                            speak("please wait sir, fetching the latest news")
                            news()

                     elif "where i am" in self.query or "where we are" in self.query or "my location" in self.query:
                            speak("wait sir, let me check")
                            try:
                                   ipAdd = requests.get('https://api.ipify.org').text
                                   print(ipAdd)
                                   url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                                   geo_requests = requests.get(url)
                                   geo_data = geo_requests.json()
                                   city = geo_data['city']
                                   country = geo_data['country']
                                   print(f"sir i am not sure, but i think we are in {city} city of {country} country")
                                   speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                            except Exception as e:
                                   speak("sorry sir, Due to network issue i am not able to find where we are.")
                                   pass

                     elif "take a screenshot" in self.query or "take screenshot" in self.query:
                            print("Sir, please tell me the name for this screenshot file")
                            speak("Sir, please tell me the name for this screenshot file")
                            name = self.takeCommand()
                            path1name = name + ".png"
                            name2 = "C:\\Users\\Asad\\OneDrive\\Pictures\\Screenshots\\"+ path1name
                            print("please sir hold the screen for few seconds, i am taking screenshot")
                            speak("please sir hold the screen for few seconds, i am taking screenshot")
                            time.sleep(3)
                            img = pyautogui.screenshot()
                            img.save(name2)
                            os.startfile("C:\\Users\\Asad\\OneDrive\\Pictures\\Screenshots\\")
                            print("Here is your Screenshot")
                            speak("Here is your Screenshot")

                     elif "read pdf" in self.query:
                            pdf_reader()

                     elif "temperature" in self.query:
                            try:
                                   search = self.query
                                   url = f"https://www.google.com/search?q={search}"
                                   r = requests.get(url)
                                   data = BeautifulSoup(r.text,"html.parser")
                                   temp = data.find("div",class_="BNeawe").text
                                   print(f"current {search} is {temp}")
                                   speak(f"current {search} is {temp}")
                            except:
                                   print("Unstable Connection")
                                   speak("Unstable Connection")

                     elif "video downloader" in self.query:
                            try:
                                   self.root = Tk()
                                   self.root.geometry('500x300')
                                   self.root.resizable(0,0)
                                   self.root.title("YouTube Video Downloader")
                                   speak("Please copy video link from YouTube and enter here")
                                   Label(self.root,text = "YouTube Video Downloader",font = 'arial 15 bold').pack()
                                   self.link = StringVar()
                                   Label(self.root,text = "Paste the link Here",font = 'arial 15 bold').place(x=160,y=60)
                                   Entry(self.root,width = 70,textvariable = self.link).place(x=32,y=90)

                                   def VideoDownloader():
                                          url = YouTube(str(self.link.get()))
                                          video = url.streams.first()
                                          video.download()
                                          Label(self.root,text = "Downloaded",font = 'arial 15').place(x = 180,y = 210)
                                   
                                   Button(self.root,text = "Download",font = 'arial 15',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)
                                   self.root.mainloop()
                                   print("Video has been downloaded")
                                   speak("Video has been downloaded")
                            
                            except Exception as e:
                                   print(e)
                            pass

                     elif "activate how to do mod" in self.query:
                            speak("How to do Mod is activated")
                            while True:
                                   print("please tell me what you want to know")
                                   speak("please tell me what you want to know")
                                   how = self.takeCommand()
                                   try:
                                          if "exit" in how or "close" in how:
                                                 print("okay sir, how to do mod is closed")
                                                 speak("okay sir, how to do mod is closed")
                                                 break
                                          else:
                                                 max_results = 1
                                                 how_to = search_wikihow(how, max_results)
                                                 assert len(how_to) == 1
                                                 how_to[0].print()
                                                 print(how_to[0].summary)
                                                 speak(how_to[0].summary)
                                   except Exception as e:
                                          speak("Sorry sir, i am not able to find this")

                     elif "battery" in self.query or "how much power is left" in self.query or "how much power we have" in self.query:
                            try:
                                   battery = psutil.sensors_battery()
                                   percentage = battery.percent
                                   print(f"sir our system have {percentage} percent battery")
                                   speak(f"sir our system have {percentage} percent battery")
                                   if percentage>=75:
                                          print("we have enough power to continue our work")
                                          speak("we have enough power to continue our work")
                                   elif percentage>=40 and percentage<=75:
                                          print("we should connect our system to charging point to charge our battery")
                                          speak("we should connect our system to charging point to charge our battery")
                                   elif percentage>15 and percentage<=30:
                                          print("we don't have enough power to work, please connect to charging")
                                          speak("we don't have enough power to work, please connect to charging")
                                   elif percentage<15:
                                          print("we have very low power, please connect to charging or the system will shutdown very soon")
                                          speak("we have very low power, please connect to charging or the system will shutdown very soon")
                            except:
                                   print("Sir, you are working on a desktop and this feature is only available to laptops")
                                   speak("Sir, this feature is only available to laptops")

                     elif "internet speed" in self.query:
                            st = speedtest.Speedtest()
                            dl = st.download()
                            up = st.upload()
                            print(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
                            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

                     elif "volume up" in self.query or "increase volume" in self.query:
                            pyautogui.press("volumeup")

                     elif "volume down" in self.query or "reduce volume" in self.query:
                            pyautogui.press("volumedown")

                     elif "volume mute" in self.query or "mute" in self.query:
                            pyautogui.press("volumemute")

                     elif "open mobile camera" in self.query:
                            try:
                                   import urllib.request
                                   import cv2
                                   import numpy as np
                                   import time
                                   URL = "http://192.168.0.117:8080/shot.jpg"
                                   while True:
                                          img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                                          img = cv2.imdecode(img_arr,-1)
                                          cv2.imshow('IPWebcam',img)
                                          q = cv2.waitKey(1)
                                          if q == ord("q"):
                                                 break;
                                   cv2.destroyAllWindows()
                            except:
                                   print("please open the IP Webcam app on your mobile and try again")
                                   speak("please open the IP Webcam app on your mobile and try again")

                     elif "open instagram" in self.query:
                            webbrowser.open("https://www.instagram.com")
                            print("opening instagram")
                            speak("opening instagram")

                     elif "open chrome" in self.query:
                            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                            print("opening google chrome")
                            speak("opening google chrome")

                     elif "open edge" in self.query:
                            os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                            print("opening Microsoft Edge")
                            speak("opening Microsoft Edge")
                     
                     elif "open maps" in self.query:
                            webbrowser("https://www.google.com/maps/")
                            print("opening Google Maps")
                            speak("opening Google Maps")
                     
                     elif "close chrome" in self.query or "close google chrome" in self.query:
                            os.system("TASKKILL /F /im chrome.exe")

                     elif "close code" in self.query or "close vs code" in self.query:
                            os.system("TASKKILL /F /im code.exe")

                     elif "close instagram" in self.query:
                            os.system("TASKKILL /F /im instagram.exe")

                     elif "close edge" in self.query:
                            os.system("TASKKILL /F /im msedge.exe")

                     elif "close facebook" in self.query:
                            os.system("TASKKILL /F /im facebook.exe")

                     elif "close adobe reader" in self.query:
                            os.system("TASKKILL /F /im AcroRd32.exe")

                     elif "close notepad" in self.query:
                            os.system("TASKKILL /F /im notepad.exe")

                     elif "close adobe reader" in self.query:
                            os.system("TASKKILL /F /im AcroRd32.exe")

                     elif "youtube tool" in self.query:                                                                          
                                   speak("Youtube tool is activated") 
                                   while True:
                                          print("whats your command")
                                          speak("whats your command")
                                          self.comm = self.takeCommand().lower()
                                          try:
                                                 if "exit youtube tool" in self.comm:
                                                        print("okay sir, youtube tool is closed")
                                                        speak("okay sir, youtube tool is closed")
                                                        break

                                                 else:  
                                                        try:
                                                               if 'pause' in self.comm:
                                                                      keyboard.press('space bar')

                                                               elif 'play' in self.comm:
                                                                      keyboard.press('space bar')

                                                               elif 'restart' in self.comm:
                                                                      keyboard.press('0')

                                                               elif 'mute' in self.comm:
                                                                      keyboard.press('m')
                                                                      
                                                               elif 'skip' in self.comm:
                                                                      keyboard.press('l')

                                                               elif 'back' in self.comm:
                                                                      keyboard.press('j')

                                                               elif 'full screen' in self.comm:
                                                                      keyboard.press('f')

                                                               elif 'film mode' in self.comm:
                                                                      keyboard.press('t')

                                                               elif 'previous video' in self.comm:
                                                                      keyboard.press('P')

                                                               elif 'next video' in self.comm:
                                                                      keyboard.press('shift + n')

                                                               elif 'decrease playback rate' in self.comm:
                                                                      keyboard.press('<')

                                                               elif 'increase playback rate' in self.comm:
                                                                      keyboard.press('>')

                                                               elif 'Close full screen' in self.comm or 'close miniplayer' in self.comm or 'close theatre mode':
                                                                      keyboard.press('escape')

                                                               elif 'caption' in self.comm or 'subtitle':
                                                                      keyboard.press('c')
                                                        
                                                        except:
                                                               speak("Invalid Command")
                                                        
                                          except Exception as e:
                                                 speak("Invalid Command")
                                                 
                     elif "calculator" in self.query or "calculate" in self.query:
                            try:
                                   r = sr.Recognizer()
                                   with sr.Microphone() as source:
                                          print("what should i calculate")
                                          speak("what should i calculate")
                                          print("listening...")
                                          r.adjust_for_ambient_noise(source)
                                          audio = r.listen(source)
                                   my_string = r.recognize_google(audio)
                                   print(my_string)
                                   def get_operator_fn(op):
                                          return{
                                                 '+' : operator.add,
                                                 '-' : operator.sub,
                                                 'x' : operator.mul,
                                                 'divided' : operator.__truediv__,
                                                 }[op]
                                   def eval_binary_expr(op1, oper, op2):
                                          op1,op2 = int(op1), int(op2)
                                          return get_operator_fn(oper)(op1, op2)
                                   print("your result is")
                                   speak("your result is")
                                   print(eval_binary_expr(*(my_string.split())))
                                   speak(eval_binary_expr(*(my_string.split())))
                            except:
                                   print("Sorry i didn't get that please try again")
                                   speak("Sorry i didn't get that please try again")

