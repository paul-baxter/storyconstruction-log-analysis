#!/usr/bin/env python3
#
# analysis.py
#
# need to use > python 3.5.3 (to use pandas)
#   assuming use of python3.8 in Ubuntu 20.04
#   sudo apt install python3-pip
#   sudo apt install python3-numpy python3-pandas python3-matplotlib python3-scipy
#   python3 -m pip install --upgrade bootstrapped
#
# "analysis of log files from story construction study, 2019"
# "University of Lincoln, U.K."
#
# run using (where data.dat is a log file):
#   python3 analysis.py data.dat
#

import numpy as np
import pandas as pd
import scipy.stats as stats
import statsfunctions as sf
import sys
import csv

fileInName = str(sys.argv[1])
print("    File to process: ", fileInName)

with open(fileInName, newline='') as file:
    read = csv.reader(file)
    data = list(read)

firstEvent = True
ttsCount = 0
ttsCounts = []
ttsPageTime = []
ttsPageTimes = []
startTime = 0
pageTime = 0
pageTimes = []
pageCount = 0
ttsStrings = ""

# get the participant ID number
ID = str(data[0][0])
print("\t Participant ID: ", ID)

# the actual data starts at 'row' 3 until the end
for line in data[3:]:
    if (line[2]=="page"):
        #new page has come up
        pageCount += 1
        #print("New page detected")
        startTime = int(line[1])
        ttsCount = 0
    elif (line[2]=="tts"):
        #
        #print("TTS event detected")
        ttsCount += 1
        ttsPageTime.append(int(line[1]) - startTime)
    elif (line[2]=="event"):
        #page
        if (firstEvent):
            firstEvent = False
            continue
        #print("Event detected")
        pageTime = int(line[1]) - startTime
        pageTimes.append(pageTime)
        ttsCounts.append(ttsCount)
        ttsPageTimes.append(ttsPageTime)
        startTime = 0
        pageTime = 0
        ttsCount = 0
        ttsPageTime = []
    elif (line[2]==""):
        #
        #print("End of interaction detected")
        interactionDuration = int(line[6])
    else:
        #
        print("No matching message type")

#process tts times list to turn into intervals rather than from start...
ttsIntervals = []
for pT in ttsPageTimes:
    page = pT
    times = []
    for index, t in enumerate(page):
        if (index == 0): t = t
        else: t = t - page[index-1]
        times.append(t)
    ttsIntervals.append(times)

#construct result string and append to results file
resultLine = ID + "," + str(interactionDuration) + "," + str(pageCount) + ","

for i in range(pageCount):
    resultLine = resultLine + str(pageTimes[i]) + "," + str(ttsCounts[i]) + "," + str(sf.meanFromList(ttsIntervals[i])) + "," + str(sf.stdevFromList(ttsIntervals[i])) + ","
resultLine = resultLine + "\n"

print ("\t", str(interactionDuration), str(pageCount))

with open("processedData.dat", 'a') as outFile:
    outFile.write(resultLine)
