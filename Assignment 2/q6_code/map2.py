#!/usr/bin/env python
import sys
import json

# input comes from STDIN
for line in sys.stdin:
    # remove whitespace and split row into values
    line_split = line.strip().split("\t")
    # load trace into list of activities
    activities = json.loads(line_split[1])
    for i in range(len(activities) - 1):
        # write the results to STDOUT;
        # key: (from,to), value: 1 (count of the relation)
        stru = activities[i] + "," + activities[i + 1]
        print('%s\t%s' % (stru, 1))
