#!/usr/bin/python

import time
import datetime
import sys
import argparse
import os.path

def timestamp():
    ts = time.time()
    datestamp = datetime.datetime.fromtimestamp(ts).strftime('%m%d%Y')
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    f = '/home/jason/timecard-' + datestamp + '.dat'

    # Sets the switches for the different functions of the application.
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-t', '--task', dest='TASK',
        action='store_true', default=False,
        help='Ask for input which it logs as current task with timestamp, also if it already has a current task it logs last task as stopped with timestamp before starting new one.')
    parser.add_argument('-b', '--break', dest='BREAK',
        action='store_true', default=False,
        help='Logs break with timestamp, if there is already a break logged it logs break stopped with timestamp and ask you for current task.')
    parser.add_argument('-l', '--login', dest='LOGIN',
        action='store_true', default=False,
        help='Login option is to be used with computer login, this will log Arrived at work with timestamp.')
    parser.add_argument('-L', '--logout', dest='LOGOUT',
        action='store_true', default=False,
        help='Logout option is to be used with computer logoff, this will log Leaving work with timestamp.')

    args = parser.parse_args()

    # Checks to see if the file exist and can be opened.
    if os.path.exists(f):
        try:
            with open(f, 'a'): pass
            fileerror = False
        except IOError:
            fileerror = True
    else:
        fileerror = True

    # Checks against parser for the argument passed to the application, if it returns then it logs a specific message for type of input with a timestamp.
    if args.TASK and fileerror == False:
        # if parser returns as TASK then it ask for input and logs with timestamp.
        ## Need to add a line that stops the last task or break with a timestamp before adding the next string.
        answer = raw_input("Please enter your task and press 'Enter'. ")
        print "Thank you, your request is logged."
        with open(f, 'a')as file:
            file.write('Started working on \"' + answer + '\": ' + timestamp + "\n")
    elif args.BREAK and fileerror == False:
        # if parser returns as BREAK then it logs BREAK with timestamp.
        ## Need to add a line that stops the last task with a timestamp before adding the string.
        ## Need to add a line that returns "Already on break" if break is already in progress.
        print "Thank you, your request is logged."
        with open(f, 'a')as file:
            file.write('Started BREAK: ' + timestamp + "\n")
    elif args.LOGIN and fileerror == True:
        # if parser returns as LOGIN then it creates file if it does not exist, timestamp-$(date +%m%d%Y).dat and then adds line "Arrived at work" with timestamp
        print "Thank you, your request is logged."
        with open(f, 'w+') as file:
            file.write('Arrived at work: ' + timestamp + "\n")
    elif args.LOGIN and fileerror == False:
        print "You have already logged an entry for Work arrival on this day's timecard."
    elif args.LOGOUT and fileerror == False:
        # if parser returns as LOGOUT then it adds line "Leaving work" with timestamp this should be intiated when computer begins to shutdown.  The rest of this line will take entire logfile and compile unique lines and calculate total time spent on each followed by sending results to email.
        ## Need to add a line that stops the last task or break with a timestamp before adding the "Leaving work" string.
        print "Thank you, your request is logged."
        with open(f, 'a')as file:
            file.write('Leaving work: ' + timestamp + "\n")
    elif fileerror == True:
        # Only returns if the file does not exist and an option that is trying to append to the file is called..
        print "No timecard file detected, maybe you didn't login correctly?."
    else:
        # Print help message for application
        parser.print_usage()
timestamp()

#############
#
# Possible idea's beyond timestamp, make entry only so many characters like 20.  That way the only thing entered is a specific task, for example: Fixed Tony's Laptop, or Setup base-build for Mike.  Then offer some type of input to add aditional notes.  However seperate it from the task line, so that notes and task do not get mixes up in the compilation of the daily task but if further details are needed later there is a log.
#
#############
