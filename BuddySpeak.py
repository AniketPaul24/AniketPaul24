# from time import sleep
import sys
from sys import exit
import requests
import pyttsx3
import pyautogui as pt
import speech_recognition as sr
import datetime
import winsound
import wolframalpha
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from buddyGUI1 import Ui_Buddy


# from ecapture import ecapture as ec


# ---------------------------Giving voice to the system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """audio function for the BUDDY to speak"""
    engine.say(audio)
    engine.runAndWait()


book1 = open('asp.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book1)
pages = pdfReader.numPages
page = pdfReader.getPage(31)
text1 = page.extractText()

book2 = open('TheSilentPatient.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book2)
# pages = pdfReader.numPages
page = pdfReader.getPage(8)
text2 = page.extractText()


# ---------------------------WishMe function
def wishMe():
    """wishme function for the BUDDY to greet user"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning partner!")
        speak("Good Morning partner!")

    elif 12 <= hour < 18:
        print("Good Afternoon partner!")
        speak("Good Afternoon partner!")

    else:
        print("Good Evening partner!")
        speak("Good Evening partner!")

    print("What can I do for you today?")
    speak("What can I do for you today?")



# ---------------------------Alarm function
def alarm(Timing):
    """alarm function for the BUDDY to set alarm"""
    alttime = str(datetime.datetime.now().strptime(Timing, '%I:%M %p'))
    alttime = alttime[11:-3]
    hourtime = alttime[:2]
    hourtime = int(hourtime)
    mintime = alttime[3:5]
    mintime = int(mintime)
    print(f'Alarm has been set to {Timing}')

    while True:
        if hourtime == datetime.datetime.now().hour:
            if mintime == datetime.datetime.now().minute:
                print('Turn off your Alarm')
                winsound.PlaySound('abc', winsound.SND_LOOP)

        elif mintime < datetime.datetime.now().minute:
            break


# ---------------------------SendEmail function
# f = open('pass.txt', 'r')
to = {"aniketnfamily@gmail.com": "aniket", 
      "jsarang1950@gmail.com": "sarang", 
      "kumarianushka469@gmail.com": "anushka"}


def sendEmail(do, content):
    """sendEmail function for the BUDDY to send email as per user's choice"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bknowledgesaathi@gmail.com', 'haathimeresaathi')
    server.sendmail('bknowledgesaathi@gmail.com', to, content)
    server.close()


# ---------------------------Test/Quiz function
def asp_test():
    """test function to check the user's knowledge"""

    def new_game():

        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions:
            print("-------------------------")
            speak(key)
            print(key)
            for i in options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_num += 1

        display_score(correct_guesses, guesses)

    def check_answer(answers, guess):

        if answers == guess:
            print("CORRECT!")
            speak("CORRECT!")
            return 1
        else:
            print("WRONG!")
            speak("WRONG!")
            return 0

    def display_score(correct_guesses, guesses):
        print("-------------------------")
        print("RESULTS")
        print("-------------------------")

        print("Answers: ", end="")
        for i in questions:
            print(questions.get(i), end=" ")
        print()

        print("Guesses: ", end="")
        for i in guesses:
            print(i, end=" ")
        print()

        score = int((correct_guesses / len(questions)) * 100)
        speak("Your score in ASP.NET is: " + str(score) + "%")
        print("Your score in ASP.NET is: " + str(score) + "%")

        if score >= 90:
            print("You did great!!!")
            speak("You did great!!!")
        elif 90 > score >= 80:
            print("You did great!!! But you could have done much better")
            speak("You did great!!! But you could have done much better")
        elif 80 > score >= 70:
            print("Not bad...")
            speak("Not bad...")
        elif 70 > score >= 60:
            print("You have to level up your game buddy!")
            speak("You have to level up your game buddy!")
        else:
            print("Go and Study. NOW!!!!!")
            speak("Go and Study. NOW...")
            print(
                "Here is a link through which you can practice: https://www.youtube.com/playlist?list=PL6n9fhu94yhXQS_p1i-HLIftB9Y7Vnxlo")
            speak("Here is a link through which you can practice")

    def play_again():

        response = input("Do you want to play again? (yes or no): ")
        response = response.upper()

        if response == "YES":
            return True
        else:
            return False

    questions = {
        "1) Default scripting language in ASP": "B",
        "2) How do you get information from a form that is submitted using the \"post\" method?": "B",
        "3) Which object can help you maintain data across users?": "A",
        "4) Which of the following ASP.NET object encapsulates the state of the client?": "A",
        "5) Which of the following object is used along with an application object in order to ensure that only one process accesses a variable at a time?": "B",
        "6) Which of the following control is used to validate that two fields are equal?": "C",
        "7) Mode of storing ASP.NET session": "D",
        "8) Which of the following is not the way to maintain state?": "D",
        "9) You can have only one Global.asax file per project.": "A",
        "10) ______________ element in the web.config file is used to run code using the permissions of a specific user": "D"
    }

    options = [["A. EcmaScript", "B. VBScript", "C. PERL", "D. PERL"],
               ["A. Request.QueryString", "B. Request.Form", "C. Response.write", "D. Response.writeln"],
               ["A. Application object", "B. Session object",
                "C. Response object", "D. Server object"],
               ["A. Session object", "B. Application object", "C. Response object", "D. Server object"],
               ["A. Synchronize", "B. Synchronize()", "C. ThreadLock", "D. Lock()"],
               ["A. RegularExpressionValidator", "B. equals() method", "C. CompareValidator",
                "D. RequiredFieldValidator"],
               ["A. InProc", "B. StateServer", "C. SQL Server", "D. All of the above"],
               ["A. View state", "B. Cookies", "C. Hidden fields", "D. Request object"],
               ["A. Yes", "B. No"],
               ["A. < credential> element", "B. < authentication> element", "C. < authorization> element",
                "D. < identity> element"]]

    new_game()

    while play_again():
        new_game()

    print("Bye!!!!!")
    speak("Sayōnara")


def os_test():
    def new_game():

        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions:
            print("-------------------------")
            print(key)
            for i in options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_num += 1

        display_score(correct_guesses, guesses)

    def check_answer(answers, guess):

        if answers == guess:
            print("CORRECT!")
            speak("CORRECT!")
            return 1
        else:
            print("WRONG!")
            speak("WRONG!")
            return 0

    def display_score(correct_guesses, guesses):
        print("-------------------------")
        print("RESULTS")
        print("-------------------------")

        print("Answers: ", end="")
        for i in questions:
            print(questions.get(i), end=" ")
        print()

        print("Guesses: ", end="")
        for i in guesses:
            print(i, end=" ")
        print()

        score = int((correct_guesses / len(questions)) * 100)
        speak("Your score in OS is: " + str(score) + "%")
        print("Your score in OS is: " + str(score) + "%")

        if score >= 90:
            print("You did great!!!")
            speak("You did great!!!")
        elif 90 > score >= 80:
            print("You did great!!! But you could have done much better")
            speak("You did great!!! But you could have done much better")
        elif 80 > score >= 70:
            print("Not bad...")
            speak("Not bad...")
        elif 70 > score >= 60:
            print("You have to level up your game buddy!")
            speak("You have to level up your game buddy!")
        else:
            print("Go and Study. NOW!!!!!")
            speak("Go and Study. NOW...")
            print(
                "Here is a link through which you can practice: https://www.youtube.com/playlist?list=PLxCzCOWd7aiGz9donHRrE9I3Mwn6XdP8p")
            speak("Here is a link through which you can practice")

    def play_again():

        response = input("Do you want to play again? (yes or no): ")
        response = response.upper()

        if response == "YES":
            return True
        else:
            return False

    questions = {
        "1) System calls are invoked by using": "A",
        "2) Transfer of information to and from main memory takes place in terms of": "C",
        "3) Page fault occurs when": "C",
        "4) Which phenomenon occurs when the processor spends most of its time in swapping pages, rather than executing them?": "A",
        "5) The process which requires saving the state of the old process and loading the saved state for the new process when switching occurs is known as": "C",
        "6) Which of the following is NOT a solution for the critical section problem?": "B",
        "7) Spooling is": "D",
        "8) Where does swap space resides?": "B",
        "9) Object modules generated by assemblers may contain unresolved references. These are resolved using other object modules by the": "D",
        "10) While running DOS on a PC, which command would be used to duplicate the entire diskette?": "B"
    }

    options = [["A. Software interrupts", "B. Polling", "C. Indirect jump", "D. A privileged instruction"],
               ["A. Bits", "B. Bytes", "C. Words", "D. Nibbles"],
               ["A. The page is corrupted by application software", "B. The page is in main memory",
                "C. The page is not in main memory", "D. One tries to divide a number by 0"],
               ["A. Thrashing", "B. Belady's Anomaly", "C. Reentrancy", "D. None of the above"],
               ["A. Dispatcher", "B. CPU scheduling", "C. Context Switch", "D. Fragmentation"],
               ["A. Monitor", "B. Segmentation", "C. Semaphore", "D. Critical Region constructs"],
               ["A. The rewinding of tapes after processing",
                "B. The temporary storage and management of output to printers and other output devices until they can cope with it",
                "C. The recording of all user activities in a log file", "D. None of the above"],
               ["A. RAM", "B. ROM", "C. Disk", "D. On-chip Cache"],
               ["A. Loader", "B. Debugger", "C. Compiler", "D. Linker"],
               ["A. Copy", "B. diskcopy", "C. mkdir", "D. Copy filename1 filename2"]]

    new_game()

    while play_again():
        new_game()

    print("Bye!!!!!")
    speak("Sayōnara")


def cg_test():
    def new_game():

        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions:
            print("-------------------------")
            print(key)
            for i in options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_num += 1

        display_score(correct_guesses, guesses)

    def check_answer(answers, guess):

        if answers == guess:
            print("CORRECT!")
            speak("CORRECT!")
            return 1
        else:
            print("WRONG!")
            speak("WRONG!")
            return 0

    def display_score(correct_guesses, guesses):
        print("-------------------------")
        print("RESULTS")
        print("-------------------------")

        print("Answers: ", end="")
        for i in questions:
            print(questions.get(i), end=" ")
        print()

        print("Guesses: ", end="")
        for i in guesses:
            print(i, end=" ")
        print()

        score = int((correct_guesses / len(questions)) * 100)
        speak("Your score in CG is: " + str(score) + "%")
        print("Your score in CG is: " + str(score) + "%")

        if score >= 90:
            print("You did great!!!")
            speak("You did great!!!")
        elif 90 > score >= 80:
            print("You did great!!! But you could have done much better")
            speak("You did great!!! But you could have done much better")
        elif 80 > score >= 70:
            print("Not bad...")
            speak("Not bad...")
        elif 70 > score >= 60:
            print("You have to level up your game buddy!")
            speak("You have to level up your game buddy!")
        else:
            print("Go and Study. NOW!!!!!")
            speak("Go and Study. NOW...")
            print(
                "Here is a link through which you can practice: https://www.youtube.com/playlist?list=PLrjkTql3jnm9cY0ijEyr2fPdwnH-0t8EY")
            speak("Here is a link through which you can practice")

    def play_again():

        response = input("Do you want to play again? (yes or no): ")
        response = response.upper()

        if response == "YES":
            return True
        else:
            return False

    questions = {
        "1) GUI stands for ": "C",
        "2) Graphics can be ": "D",
        "3) CAD stands for ": "B",
        "4) The components of Interactive computer graphics are ": "D",
        "5) A user can make any change in the image using ": "A",
        "6) What is a pixel mask?": "D",
        "7) The higher number of pixels gives us a ____ image ": "A",
        "8) Which one of the following is the primarily used output device?": "A",
        "9) Which one of the following terms is used for the area of the computer captured by an application?": "C",
        "10) Aspect Ratio can be defined as": "A"
    }

    options = [["A. Graphics uniform interaction", "B. Graphical user interaction", "C. Graphical user interface",
                "D. None of the above"],
               ["A. Simulation", "B. Drawing", "C. WordsMovies, photographs", "D. All of the above"],
               ["A. Computer art design", "B. Computer-aided design",
                "C. Car art design", "D. None of the above"],
               ["A. A monitor", "B. Display controller", "C. Frame buffer", "D. All of the above"],
               ["A. Interactive computer graphics", "B. Non-Interactive computer graphics", "C. Both (a) & (b)",
                "D. None of the above"],
               ["A. a string containing only 0's", "B. a string containing only 1's", "C. a string containing two 0's",
                "D. a string containing both 1's and 0's"],
               ["A. Better", "B. Worst", "C. Smaller", "D. None of the above"],
               ["A. Video monitor", "B. Scanner", "C. Speaker", "D. Printer"],
               ["A. Display", "B. Window", "C. Viewport", "D. None of the above"],
               ["A. The ratio of the vertical points to horizontal points", "B. of pixels", "C. Both (a) & (b)",
                "D. None of the above"]]

    new_game()

    while play_again():
        new_game()

    print("Bye!!!!!")
    speak("Sayōnara")



# ---------------------------Task Execution function
def taskExecution(self):
        while True:  # Infinite loop query
            # if 1:
            query = self.takeCommand().lower()

            # ---------------------------Wikipedia Search query
            if 'please tell me about' in query:
                speak('Searching ...! Please wait...')
                print('Searching ...')
                query = query.replace("please tell me about", "")
                results = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            # ---------------------------Google Search query
            elif 'search' in query or 'what is' in query or 'what are' in query:
                sch = query.replace('search', '')
                speak('searching')
                pywhatkit.search(sch)

            # ---------------------------Camera Capture query
            # elif "camera" in query or "take a picture" in query:
            #     ec.capture(0, "Image", "img")

            # ---------------------------System Features query
            elif 'what can you do' in query:
                print('I can make google searches for you, open youtube, read your class notes,\n'
                    'provide computational knowledge, '
                    'open your favourite sites and applications, set alarm, send email, play some music, etcetera')
                speak('I can make google searches for you, open youtube, read your class notes,'
                    ' provide computational knowledge, '
                    'open your favourite sites and applications, set alarm, send email, play some music, etcetera')
                speak('What do YOU want me to do ?')
                
            elif 'introduce' in query or 'introduction' in query:
                print('My name is BUDDY! The knowledge Saathi, I am here to help students to get through the hardship and torture of college.'
                    'hmm, just kidding, I am actually a VI that tests the knowledge of the student and give him or her the materials needed to gain knowledge.')
                speak('My name is BUDDY! The knowledge Saathi , I am here to help students to get through the hardship and torture of college.'
                    ' hmm, just kidding, I am actually a Virtual Assistant that tests the knowledge of the student and give him or her the materials needed to gain knowledge. '
                    ' I am also a study partner with whom a student can study with.')
                speak('What do YOU want me to do ?')

            # ---------------------------Wolfram API query
            elif 'ask' in query or 'question' in query or 'request' in query:
                print('What is it?')
                speak('What is it?')
                question = self.takeCommand()
                app_id = "Paste your unique ID here "
                client = wolframalpha.Client('2JGHK8-XLWQR6H9VT')
                try:
                    res = client.query(question)
                    answer = next(res.results).text
                    print(answer)
                    speak(answer)
                except Exception as e:
                    print("Please reframe your question and then say that again...")

            # ---------------------------Alarm query
            elif 'alarm' in query:
                try:
                    print('At what time you want to set alarm')
                    speak('At what time you want to set alarm')
                    tt = self.takeCommand()
                    tt = tt.replace('set alarm to ', '')
                    tt = tt.replace('.', '')
                    tt = tt.upper()
                    alarm(tt)
                except Exception as e:
                    print("Sorry... couldn't set the alarm now!")
                    speak("Sorry... couldn't set the alarm now!")

            # ---------------------------System one-on-one interaction query
            elif 'so long' in query or 'missed you' in query:
                print('Ohh... and here I thought that you forgot me ... I missed you too   \n So where have you been?')
                speak('Ohh... and here I thought that you forgot me ... I missed you too   \n So where have you been?')
                query = self.takeCommand().lower()
                if 'exams' in query:
                    print('ohh.. So how did it go?')
                    speak('ohh.. So how did it go?')
                    query = self.takeCommand().lower()
                    if 'fine' in query:
                        print('I am happy to hear that...\nNow how may I help you?')
                        speak('I am happy to hear that...! \nNow how may I help you?')

            elif 'how are you' in query:
                print('Thanks for asking, and I am doing just Great!   \n How are you doing?')
                speak('Thanks for asking, and I am doing just Great!   \n How are you doing?')
                query = self.takeCommand().lower()
                if 'great' in query or 'fine' in query or 'good' in query:
                    print('I am happy to hear that... \nNow how may I help you?')
                    speak('I am happy to hear that...! \nNow how may I help you?')

                elif 'stressed' in query or 'not' in query:
                    print('huh! well, me too!\n Sorry I lied earlier...')
                    speak('huh......! well....! me too...!\n Sorry I lied earlier...')
                    query = self.takeCommand().lower()
                    if 'why' in query:
                        print('Sorry...! But I had to, or else what will my friends think about me...! \n  '
                            'But still, I can suggest you few exercises which I do myself to reduce stress.')
                        speak('Sorry...! But I had to, or else what will my friends think about me...! \n  '
                            'But still...! I can suggest you few exercises which I do myself to reduce stress.')

            elif 'wassup' in query or 'what\'s up' in query:
                print('Wow! You are sounding energetic today  \nHow are you doing?')
                speak('Wow! You are sounding energetic today  \nHow are you doing?')
                query = self.takeCommand().lower()
                if 'great' in query or 'fine' in query or 'good' in query:
                    print('I am happy to hear that... \nNow how may I help you?')
                    speak('I am happy to hear that...! \nNow how may I help you?')


            # ---------------------------Site Opening query
            elif 'open python cheat sheet' in query:
                speak('opening')
                webbrowser.open("https://www.pythoncheatsheet.org/")

            elif 'open classroom' in query:
                speak('opening')
                webbrowser.open("https://classroom.google.com/u/1/h")

            elif 'open youtube' in query or 'youtube chalu' in query:
                speak('opening')
                webbrowser.open("https://www.youtube.com/")

            elif 'open google' in query or 'google open' in query:
                speak('opening')
                webbrowser.open("https://www.google.com/")

            elif 'open stackoverflow' in query or "stack overflow" in query:
                speak('opening')
                webbrowser.open("https://stackoverflow.com/")

            # ---------------------------Music Play query
            elif 'music' in query or 'gana' in query:
                music_dir = 'D:\\Music'
                songs = os.listdir(music_dir)
                print('I think you might like this...')
                speak('I think you might like this...')
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'play' in query:
                try:
                    song = query.replace('play', '')
                    print('playing')
                    speak('playing')
                    pywhatkit.playonyt(song)
                except Exception as e:
                    print(e)
                    print("Sorry buddy, but I have failed to find a song of this name!!!")
                    speak("Sorry buddy, but I have failed to find a song of this name!!!")
                break

            # ---------------------------Time query
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                print(f"The time is {strTime} ")
                speak(f"The time is {strTime} ")

            # ---------------------------System Applications query
            elif 'open code' in query:
                speak('opening')
                codePath = "C:\\Users\\anike\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'close code' in query:
                speak('closing')
                os.system("taskkill /f /im Code.exe")

            elif 'open whatsapp' in query:
                speak('opening')
                wPath = "C:\\Users\\anike\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(wPath)

            elif 'close whatsapp' in query:
                speak('closing')
                os.system("taskkill /f /im WhatsApp.exe")

            elif 'close brave' in query:
                speak('closing')
                os.system("taskkill /f /im Brave.exe")

            # ---------------------------Email query
            elif 'send an email' in query or 'send a mail' in query:
                try:
                    speak("What should I send?")
                    content = self.takeCommand()
                    speak("Whom should I send?")
                    to = self.takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry buddy, but I have failed to send this email")

            # ---------------------------Window query
            elif 'switch window' in query or 'switch tab' in query:
                pt.keyDown("alt")
                pt.press("tab")
                # sleep(1)
                pt.keyUp("alt")

            # ---------------------------Audio Notes query
            elif 'notes' in query:
                # print(pages)
                print(text1)
                speak(text1)
                break
            elif 'book' in query:
                # print(pages)
                print(text2)
                speak(text2)
                break

            # ---------------------------Test query
            elif 'asp test' in query or 'dot net test' in query or 'dot net quiz' in query or 'asp quiz' in query:
                asp_test()
                break
            elif 'operating system test' in query or 'operating system quiz' in query or 'quiz for operating system' in query:
                os_test()
                break
            elif 'cg test' in query or 'cg quiz' in query or 'graphics quiz' in query:
                cg_test()
                break

            # ---------------------------Location Info query
            elif 'my location' in query or 'our location' in query or 'where' in query:
                print('Fetching location....')
                speak('Fetching location....')
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    print(f"Our location might be {city}, city of {country}")
                    speak(f"Our location might be {city}, city of {country}")
                except Exception as e:
                    print("Unable to find current location at the moment...")
                    speak("Unable to find current location at the moment...")

            # ---------------------------Exit Execution query
            elif 'thanks' in query or 'thank you' in query:
                print("You're most welcome")
                speak("You're most welcome")
                break

            elif 'go to sleep' in query:
                print("okay, don't wake me up")
                speak("okay, don't wake me up")
                break



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Execution()

# ---------------------------TakeCommand function
    def takeCommand(self):
        """takeCommand function for the BUDDY to take command from user"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.8
            audio = r.listen(source)

        try:
            print("Identifying query...")
            query = r.recognize_google(audio, language="en-in")
            print("user said: ", query)

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    
    def Execution(self):
        while True:
            permission = self.takeCommand().lower()
            if "hey" in permission or "hello" in permission:
                wishMe()
                taskExecution(self)
                
            elif 'wake up' in permission:
                print("uhh.... What now")
                speak("uhh.... What now")
                taskExecution(self)
                
            # ---------------------------Exit Execution query
            elif 'goodbye' in permission or 'bye' in permission or 'that\'s all' in permission:
                print("Until next time.")
                speak("Until next time.")
                break


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Buddy()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("time circle.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)
        
        
app = QApplication(sys.argv)
bd = Main()
bd.show()
exit(app.exec_())

