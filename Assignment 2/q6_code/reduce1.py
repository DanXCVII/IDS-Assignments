#!/usr/bin/env python
import sys
import json

current_case = None

# input comes from STDIN
for line in sys.stdin:
    # remove whitespace and parse the input (case,(timestamp, activity)) we got from mapper.py
    caseid_timestamp, activity = line.strip().split("\t")
    caseid = caseid_timestamp.strip().split("-")[0]
    # shuffling is done by Hadoop
    if caseid != current_case:
        # write result to STDOUT
        if current_case:
            print('%s\t%s' % (current_case, json.dumps(current_trace)))
        # reset current trace
        current_case = caseid
        current_trace = [activity]
    else:
        current_trace.append(activity)

# output the last word
if current_case == caseid:
    print('%s\t%s' % (caseid, json.dumps(current_trace)))
