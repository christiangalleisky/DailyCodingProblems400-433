# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:13:31 2020

@author: Flea
Find out how many classrooms are needed given a list of 
tuples of start and end times
"""

def max_overlapping(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)
    print(intervals)
    print(starts)
    print(ends)
    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1
    return current_max


x = [(0, 50), (30, 45), (45, 55), (20, 25)]
print(max_overlapping(x))