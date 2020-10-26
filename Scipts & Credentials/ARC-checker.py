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

import ezsheets
import datetime

arcResp = ezsheets.Spreadsheet('10DBMHzR7NVHHT8voEQdtZWnXWeZ_T19NPWbc3Cv5OmE')
arc = arcResp.sheets[0]
# check for new line in arcResp
i = 2
while arc[1,i] != '':
    i +=1
finalindex = i-1

latestDate = datetime.datetime.strptime(arc[1,finalindex], '%m/%d/%Y %H:%M:%S')
now = datetime.datetime.now()

# only run code when latest entry was submitted in the last five minutes
if (now - latestDate).seconds <= 300:
    print('RUN CODE')
    # Store all variables in new lines
    # Check if that spot is empty






