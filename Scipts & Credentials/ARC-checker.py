#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:28:00 2020

@author: tylerkim
"""
# =============================================================================
# ARC-checker.py
# This file will run every 5 minutes to check for any new google form submissions
# For new submissions, this script will automatically check if it's a valid form and
# record it in ARC signup google sheet.
# =============================================================================

import ezsheets, datetime, ezgmail

arcResp = (ezsheets.Spreadsheet('10DBMHzR7NVHHT8voEQdtZWnXWeZ_T19NPWbc3Cv5OmE')).sheets[0]
arc = (ezsheets.Spreadsheet('1DHee5woHPxNfU8PkcKXH3mOBhjJNywKVNPfb4drdv0g')).sheets[1]
ezgmail.init()

# check for new line in arcResp
i = int(arcResp[13,2]) # where most recent numRows is saved
while arc[1,i] != '':
    i +=1
finalindex = i
arcResp[13,2] = str(i)
#TODO: also this should be able to handle multiple submissions in 5min span

latestDate = datetime.datetime.strptime(arcResp[1,finalindex], '%m/%d/%Y %H:%M:%S')
now = datetime.datetime.now()

# Store all variables in new lines
email = arcResp[2,finalindex]
name = arcResp[3,finalindex]
form = arcResp[4,finalindex]
day = arcResp[5,finalindex]
time = arcResp[6,finalindex]
course = arcResp[7,finalindex]
teacher = arcResp[8,finalindex]

dictDays = {
  "Monday": [2,list(range(6,12))],
  "Tuesday": [5,list(range(6,12))],
  "Wednesday": [8,list(range(6,12))],
  "Thursday": [2,list(range(6,12))],
  "Friday": [5,list(range(6,12))],
  "Sunday": [8,list(range(6,12))],
}

dictTimes = {"8:00 - 8:20": 0,"8:20 - 8:40": 1,"8:40 - 9:00": 2,"9:00 - 9:20": 3,
             "9:20 - 9:40": 4,"9:40 - 10:00": 5,
}

# only run code when latest entry was submitted in the last five minutes
# if (now - latestDate).seconds <= 300:
if True:
    # Check if that spot is empty
    row = dictDays[day][1][dictTimes[time]]
    col = dictDays[day][0]
    if not arc[col, row]:
        arc[col,row] = name
        arc[col+1,row] = f'{course} ({teacher})'

        ezgmail.send(email, 'ARCBOT: Confirmation for your recent ARC reservation',f'''
Dear {name},
             
This is an automated email to notify you of a recent ARC reservation.
             
Student: {name} ({form})
Time: {day} {time}
Teacher: {teacher} ({course})
             
             
Best,
ARCBOT
             ''')
        
    else:
        print('already booked; notify user')
        #TODO: send 'already booked' email
        
        ezgmail.send(email, 'ARCBOT: Reservation failed',f'''
Dear {name},
             
It seems like the time you chose has already been booked.
Please check the google sheet and try with another time slot.
             
             
Best,
ARCBOT
             ''')
        

    