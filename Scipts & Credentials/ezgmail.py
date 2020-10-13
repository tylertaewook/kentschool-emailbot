#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:46:17 2020

@author: tylerkim

http://automatetheboringstuff.com/2e/chapter18/
"""
import ezgmail, os

os.chdir('/Users/tylerkim/SpyderProjects/AutomatePython/Emails')
ezgmail.init()

ezgmail.send('tylerkim.bot@gmail.com','FIRST EMAIL','''
             Dear Tyler,
             
             This is the first email sent with python.
             
             Best,
             Tyler
             ''')

# # attachments
# ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
# ['attachment1.jpg', 'attachment2.mp3'])

# # cc & bcc
# ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
# cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')


