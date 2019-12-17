# coding=utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib


class Mail:
    def __init__(self,image_name):
        self.__smtp_host="stmp host"
        self.__mail_from="mail adresi"
        self.__mail_from_password="password"
        self.__mail_to=""
        self.image_name=image_name

    def sendMail(self):
        try:
            msg = MIMEMultipart()
            password = self.__mail_from_password
            msg['From'] =self.__mail_from
            msg['To'] = self.self.__mail_to
            msg['Subject'] = "Rapor"
            msg.attach(MIMEImage(file("./screenshots/" + self.image_name).read()))
            server = smtplib.SMTP(self.__smtp_host)
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg["To"].split(","), msg.as_string())
            print ('Mail gonderildi...')
        except:
            print ('Mail göndermede bir sorun meydana geldi')

    def getHost(self):
        return self.__smtp_host

    def setHost(self,stmpHost):
        self.__smtp_host=stmpHost

    def getFrom(self):
        return self.__mail_from

    def setFrom(self,mailFrom):
        self.__mail_from=mailFrom

    def setFromPassword(self,mailFromPassword):
        self.__mail_from_password=mailFromPassword

    def getMailTo(self):
        return self.__mail_to

    def setMailTo(self,mail_to):
        self.__mail_to=mail_to
