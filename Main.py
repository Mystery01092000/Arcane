from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
from my_commands import *
from speech_reco import *
import random
import re
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib

def arcane(command):
    errors = [
        "I don\'t know what you mean!",
        "Excuse me?",
        "Can you please repeat that?"
    ]

    if 'Hello' in command:
        talk("Hello! I am Arcane. How can I help you?")
    elif 'open google' in command:
        reg_ex = re.search('open google (.*)', command)
        url = "https://www.google.com/"
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + 'r/' + subreddit

        webbrowser.open(url)
        print("Done")
    elif 'open google and search' in command:
        reg_ex = re.search('open google and search (.*)', command)
        search_for = command.split("search",1)[1]
        url = 'https://www.google.com'
        if reg_ex:
            subgoogle = reg_ex.group(1)
            url = url + 'r/' + subgoogle

        talk("Okay!")
        driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
        driver.get('http://www.google.com')
        search = driver.find_element_by_name('q')
        search.send_keys(str(search_for))
        search.send_keys(Keys.RETURN)

    elif 'email' or 'gmail' in command:
        talk("What is the subject")
        time.sleep(3)
        subject = myCommand()
        talk("What should I say?")
        time.sleep(3)

        message = myCommand()

        content = 'Subject: {}\n\n{}'.format(subject, message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        #identify to server
        mail.ehlo()


        #encrypt session
        mail.starttls()

        #login
        mail.login('your_gmail', 'your_gmail_password')

        #send message
        mail.sendmail('FROM','TO',content)

        #end the connection
        mail.close()

        talk('Email send.')

    else:
        error = random.choice(errors)
        talk(error)

talk("Arcane here!")

while(True):
    arcane(myCommand())

