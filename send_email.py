import smtplib

def send_email(command):
    if 'email' or 'gmail' in command:
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