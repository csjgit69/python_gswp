import platform
import sys
import datetime


# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#name = raw_input("Enter file:")
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
times = dict()

for line in handle:
    if 'From ' not in line: continue
    line = line.rstrip()
    lst = line.split()
    lst = lst[5].split(":")
    times[lst[0]] = times.get(lst[0],0)+1
for k,v in sorted(times.items()):
    print(k,v)