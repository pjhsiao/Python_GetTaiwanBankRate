import smtplib
fromaddr = 'xxx@gmail.com'
username = 'xxx@gmail.com'
password = 'xxxx'

# def send(msg):
#     server = smtplib.SMTP('smtp.gmail.com:587')
#     server.ehlo()
#     server.starttls()
#     server.login(username,password)
#     server.sendmail(fromaddr, toaddrs, msg)
#     server.quit()

class GmailSender:
    def __init__(self):
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        print("gmail sender created.")
    def send(self, toAddrs, msg):
        self.server.ehlo()
        self.server.starttls()
        self.server.login(username,password)
        self.server.sendmail(fromaddr, toAddrs, msg)
        self.server.quit()