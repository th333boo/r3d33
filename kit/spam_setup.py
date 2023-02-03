#!/usr/bin/env python3
from decouple import config
from scapy.all import *
from scrapy.mail import MailSender

print('### [ EMAIL SETUP ]###')
smtphost=settings[config('MAIL_HOST')],
mailfrom=settings[config('MAIL_FROM')],
smtpuser=settings[config('MAIL_USER')],
smtppass=settings[config('MAIL_PASS')],
smtpport=settings.getint(config('MAIL_PORT')),
smtptls=settings.getbool(config('MAIL_TLS')),
smtpssl=settings.getbool(config('MAIL_SSL')),
mailer=MailSender().from_settings(settings)