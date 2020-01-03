import datetime
from gtts import gTTS
import os
import serial, time
import speech_recognition as sr
from pyowm import OWM
from google import search
import webbrowser


port="COM6"
baud= 9600

# Record Audio
r = sr.Recognizer()
m = sr.Microphone()

#set threhold level
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))

# Speech recognition using Google Speech Recognition
def checkspeech(r):
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
        return (r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ("WW")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ("WW")

def writetolcd (text):
    arduino = serial.Serial()
    arduino.port = port
    arduino.baud = baud
    arduino.setDTR(False)
    arduino.open()
    time.sleep(1)
    arduino.write(text.encode('ascil'))
    time.sleep(.1)
    arduino.close()

def main():
    run = True
    while run == True:
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to ()".format(r.energy_threshold))
        print("How can I help you Patana?")
        #os.system("start E:\Python\PythontoArduino\HowcanIhelpyou.wav")

        speech = str(checkspeech(r))
        if speech == "Mavis" or "Mavis" in speech and "system command" or "object id admin" in speech:

            os.system("start E:\Python\AI\Mavisisup.wav")
            print("how can I help you Patana?")
            speech = str(checkspeech(r))

            if speech == "What is your name":
                print("My name is Mavis")
                os.system("start E:\Python\AI\MynameisMavis.wav")
                time.sleep(1.5)
                #writetolcd(" I am Mavis")
                # writetolcd("What's yours?")
                os.system("start E:\Python\AI\MynameisMavis.wav")
                print("what's yours?")
                speech = str(checkspeech(r))
                Greeting = "Hi "+speech
                #writetolcd(Greeting)
                tts = gTTS(text= Greeting, lang='en' )
                tts.save("Greeting.wav")
                os.system("mpg321 Greeting.wav")
                os.system("start E:\Python\AI\Greeting.wav")

            elif speech == "hello Mavis":
                print("Hello patana")
                os.system("start E:\Python\AI\hellopatana.wav")
                #writetolcd("Hello Patana")
                #time.sleep(2)
                #os.system("start E:\Python\PythontoArduino\MynameisMavis.wav")
                time.sleep(2)
                os.system("start E:\Python\AI\HowcanIhelpyou.wav")

                #writetolcd("I am Mavis")

            elif  speech == "what time is it":
                #print ("Let me Check")
                #open port to Arduino
                now = datetime.datetime.now()
                timenow= (str(now.hour)+"o clcck"+str(now.minute)+"minnute")
                timetoar = "Now is "+str(now.hour)+";"+str(now.minute)
                #writetolcd(timetoar)
                tts = gTTS(text= timenow, lang='en')
                tts.save("TimeNow.wav")
                os.system("mpg321 TimeNow.wav")
                os.system("start E:\Python\AI\TimeNow.wav")

            elif  speech == "repeat after me":
                print("ok")
                speech = str(checkspeech(r))
                #writetolcd(speech)
                tts = gTTS(text= speech, lang="en")
                tts.save("speech.wav")
                os.system("mpg321 speech.wav")
                os.system("start E:\Python\AI\speech.wav")

            elif "weather" and "Bangkok" in speech:
                print("weather in Bankkok")
                API_key = '6ec9f6le7c4416e5c1da4969669010bc'
                owm = OWM(API_key)
                observation = owm.weather_at_place('Bangkok, TH')
                wc = observation.get_weather()
                temp = wc.get_temperature()
                humi = wc.get_humidity()
                wind = wc.get_wind()
                WtoAr = "BKK T="+str(int(float(temp['temp'])-273.15))+"C H="+str(humi)+"%"
                #writetolcd(WtoAr)
                weathercon = "The Current Temperature in Bangkok is "+str(int(float(temp['temp'])))
                wind = wc.get_wind()
                try:
                    winddeg = wind['deg']
                    if int (winddeg) in range(0,22):
                        winddi = 'North'
                    elif int(winddeg) in range(22,67):
                        winddi = 'NOrth East'
                    elif int(winddeg) in range(67,122):
                        winddi = 'East'
                    elif int(winddeg) in range(112,157):
                        winddi = 'South East'
                    elif int(winddeg) in range(157,202):
                        winddi = 'South'
                    elif int(winddeg) in range(202,247):
                        winddi = 'South West'
                    elif int(winddeg) in range(247,292):
                        winddi = 'west'
                    elif int (winddeg) in range(292,337):
                        winddi = 'North West'
                    elif int(winddeg) in range(337,360):
                        winddi = 'North'
                    else:
                        pass
                except:
                    windi = "Not Known"
                    print(wind)
                windcon = "The wind speed is "+str(wind['speed'])+"metre per second coming from"
                #print (wind)
                #print (wind['deg'])
                #print (winddi)
                tts =gTTS(text=weathercon, lang='en')
                tts.save("weatherCon.wav")
                os.system("mpg321 WeatherCon.wav")
                os.system("mpg321 WindCon.wav")
                os.system("start E:\Python\AI\WeatherCon.wav")
                time.sleep(8)
                os.system("start E:\Python\AI\WindCon.wav")
            elif "Weather" and "Cardiff" in speech:
                print("Weather in Cardiff")
                API_key =  '6ec9f6le7c4416e5c1da4969669010bc'
                owm = OWM(API_key)
                observation = owm.weather_at_place('Cardiff, UK')
                wc = observation.get_weather()
                temp = wc.get_temperature()
                humi = wc.get_humidity()
                wind = wc.get_wind()
                WtoAr = "CWL T="+str(int(float(temp['temp'])-273.15))+"C H="+str(humi)+"%"
                #writetolcd(WtoAr)
                weathercon = "The Current Temperature in Cardiff is "+str(int(float(temp['temp'])))
                wind = wc.get_wind()
                try:
                    winddeg = wind['deg']
                    if int(winddeg) in range(0,22):
                        winddi = 'North'
                    elif int(winddeg) in range(22,67):
                        winddi = 'North East'
                    elif int(winddeg) in range(67,112):
                        winddi = 'East'
                    elif int(winddeg) in range(122,157):
                        winddi = 'South East'
                    elif int(winddeg) in range(157,202):
                        winddi = 'South'
                    elif int(winddeg) in range(202,247):
                        winddi = 'South West'
                    elif int(winddeg) in range(247,292):
                        winddi = 'West'
                    elif int(winddeg) in range(292,337):
                        winddi = 'North West'
                    elif int(winddeg) in range(337,360):
                        winddi = 'North'
                    else:
                        pass
                except:
                    winddi ="Not Known"
                    print(wind)
                windcon = "The wind speed is "+str(wind['speed'])+"metre per second coming from"
                #print (wind)
                #print (wind['deg'])
                #print (winddi)
                tts = gTTS(text=weathercon, lang='en')
                tts.save("WeatherCon.wav")
                tts = gTTS(text= windcon, lang='en')
                tts.save("WindCon.wav")
                os.system("mpg321 WeatherCon.wav")
                os.system("mpg321 WindCon.wav")
                os.system("start E:\Python\AI\WeatherCon.wav")
                time.sleep(8)
                os.system("start E:\Python\AI\WindCon.wav")

            elif  speech =="goodbye Mavis":
                #writetolcd("Good Bye Patana")
                os.system("start E:\Python\AI\goodbye.wav")
                run = "End Program"
                print (run)

            elif  "light" in speech and "on" in speech:
                print("Light On")
                writetolcd("on")

            elif  "light" in speech and "off" in speech or "of" in speech:
                print("Light Off")
                writetolcd("off")

            elif  "search" in speech:
                new =2
                searchwW = speech.strip("search")
                url = "https://www.google.cc.uk/search?q="+str(searchwW)
                print (searchwW)
                pth = "C:\Program Files (x86)\google\Chome\Application\chome.exe"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(pth))
                chrome = webbrowser.get('chrome')
                chrome.open_new_tab(url)

            elif "open website" in speech or "open" and ".com" in speech:
                #Windows
                chrome_path = "C:\Program Files (x86)\google\Chome\Application\chome.exe"
                new =2
                if "open website" in speech:
                    openW = speech.strip("open website")
                else:
                    openW = speech.strip("open")
                print(openW)
                url = str(openW)
                pth = "C:\Program Files (x86)\Google\Chrome\Application\chome.exe"
                webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(pth))
                chrome = webbrowser.get('chrome')
                chrome.open_new_tab(url)

            else:
                print("I can't understand that yet")
                os.system("start E:\Python\AI\Dontun.wav")
                #writetolcd("Don't understand")
        elif speech == "What time is it":
                #print ("Let me Check")
                #Open port to Arduino
                now = datetime.datetime.now()
                timenow= (str(now.hour)+"o clock "+str(now.minute)+"minute")
                timetoar = "Now is "+str(now.hour)+":"+str(now.minute)
                #writetolcd(timeout)
                tts = gTTS(text= timenow, lang='en')
                tts.save("TimeNow.wav")
                os.system("mpg321 TimeNow.wav")
                os.system("start E:\Python\AI\TimeNow.wav")

        elif "thank you" in speech:
            print("Your Welcome")
            os.system("start E:\Python\AI\yourwelocme.wav")

        
























