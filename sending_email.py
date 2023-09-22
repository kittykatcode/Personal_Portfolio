import smtplib, ssl

def sent_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'testing.test.kat@gmail.com'
    password = 'xxxxxxxxxxxx'

    context = ssl.create_default_context()

    reciver = 'testing.test.kat@gmail.com'

    with smtplib.SMTP_SSL(host,port) as server:
        server.login(username, password)
        server.sendmail(username,reciver, message)

