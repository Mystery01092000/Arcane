import smtplib, ssl

#Starting a secure connection with server

def send_plain_text_mail():
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_gmail = "arc4n30101@gmail.com"
    password = input("Enter the password")

    reciever_email = input("Please enter reciever email")
    message = """\
    Subject: Hi there

    This is my first email message using python.
    """
    ## Creating a secure SSL context
    context = ssl.create_default_context()

    ## Try to login to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_gmail, password)
        server.sendmail(sender_gmail, reciever_email, message)

    except:
        print(e)
    finally:
        server.quit()