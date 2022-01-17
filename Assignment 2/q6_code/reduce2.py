#!/usr/bin/env python
import sys

current_relation = None
current_count = 0
relation = None

# input comes from STDIN
for line in sys.stdin:
    # remove whitespace
    line = line.strip()
    # parse the input ((from,to),count) we got from mapper.py
    relation, count = line.split('\t', 1)
    # convert count (currently a string) to int
    count = int(count)
    # shuffling is done by Hadoop
    if current_relation != relation:
        if current_relation:
            # write result to STDOUT
            print('%s\t%s' % (current_relation, current_count))
        current_relation = relation
        current_count = count
    else:
        current_count += count

# output the last relation
if current_relation == relation:
    print('%s\t%s' % (current_relation, current_count))
