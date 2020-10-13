#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:52:32 2020

@author: tylerkim


"""
import ezgmail,os


# prints list of unread emails
unreadThreads = ezgmail.unread() # List of GmailThread objects.
ezgmail.summary(unreadThreads)

len(unreadThreads) # number of unread emails

# Will probably use this more often
recentThreads = ezgmail.recent(maxResults=100)
len(recentThreads)


for i in range(len(unreadThreads)):
    print('SUB: '+unreadThreads[0].messages[0].subject)
    print('BODY: '+unreadThreads[0].messages[0].body)
    

firstEmail = ezgmail.search('subject:FIRST EMAIL')
