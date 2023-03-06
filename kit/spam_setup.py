#!/usr/bin/env python3
# coding: utf-8

from decouple import config
from scapy.all import *
from scrapy.mail import MailSender,settings
import smtplib
from email.message import EmailMessage

print('### [ EMAIL SETUP ]###')
smtphost=settings[config('MAIL_HOST')],
mailfrom=settings[config('MAIL_FROM')],
smtpuser=settings[config('MAIL_USER')],
smtppass=settings[config('MAIL_PASS')],
smtpport=settings.getint(config('MAIL_PORT')),
smtptls=settings.getbool(config('MAIL_TLS')),
smtpssl=settings.getbool(config('MAIL_SSL')),
mailer=MailSender().from_settings(settings)


def main():
    news_list = ["contact@bbiconnexion.com","th333boo@bbiwebsec.com"]
    subject = "Subject: This is the subject \n\n Message Body"
    html_body = "<td><h1>This is the html message</h1></td>"
    plain_txt = "This is a plain text message"

    with open('th333boo.txt') as f:
        msg.add_attachment(f.read(),filename="th333boo.txt")
    msg = EmailMessage()
    msg['subject'] = subject
    msg['from'] = smtpuser
    msg['to'] = news_list
    msg.set_content(html_body,subtype="html")
    msg.add_alternative(plain_txt,subtype="text")

    with smtplib.SMTP(smtphost,smtpport) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(smtpuser,smtppass)
        smtp.sendmail(smtpuser,msg)
        print(f"Preview of the email": {msg})