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
emailBot = ezsheets.Spreadsheet('1DHee5woHPxNfU8PkcKXH3mOBhjJNywKVNPfb4drdv0g')
arc = emailBot.sheets[1]
# check for new line in arcResp
i = 2
while arc[1,i] != '':
    i +=1
finalindex = 2

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
  "Sundasy": [8,list(range(6,12))],
}

dictTimes = {
  "8:00 - 8:20": 0,
  "8:20 - 8:40": 1,
  "8:40 - 9:00": 2,
  "9:00 - 9:20": 3,
  "9:20 - 9:40": 4,
  "9:40 - 10:00": 5,
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
    else:
        print('already booked; notify user')



