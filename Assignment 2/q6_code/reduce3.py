#!/usr/bin/env python
import sys

current_case = None
current_duration = 0

# input comes from STDIN
for line in sys.stdin:
    # remove whitespace and parse the input (case,(timestamp, duration)) we got from map3.py
    caseid_timestamp, duration = line.strip().split("\t")
    caseid = caseid_timestamp.strip().split("-")[0]
    # convert duration (currently a string) to int
    duration = int(duration)
    # shuffling is done by Hadoop
    if current_case != caseid:
        if current_case:
            # write result to STDOUT
            print('%s\t%s' % (current_case, current_duration))
        current_case = caseid
        current_duration = duration
    else:
        current_duration += duration

# output the last relation
if current_case == caseid:
    print('%s\t%s' % (current_case, current_duration))
