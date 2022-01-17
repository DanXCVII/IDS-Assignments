#!/usr/bin/env python
import sys

# input comes from STDIN
for line in sys.stdin:
    # remove whitespace and split row into values
    line_split = line.strip().split("\t")
    # assign case, activity, timestamp
    case = line_split[1]
    duration = line_split[-1]
    timestamp = line_split[3]
    # write the results to STDOUT;
    # key: case, value: (timestamp,duration)
    print('%s-%s\t%s' % (case, timestamp, duration))
