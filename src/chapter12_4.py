import platform
import sys
import datetime
import string
from bs4 import BeautifulSoup

# 12_4 example play

#import urllib.request, urllib.parse, urllib.error
#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
fname = "romeo.txt"
fh = open(fname)

counts = dict()

#for line in fhand:
for line in fh:
    #words = line.decode().split()
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
flipped = list()
for x,y in counts.items():
    flipped.append((y,x))
 
flipped.sort(reverse=True)
for x,y in flipped[:10]:
    print(x,y)
    
# print("counts:")
# print(sorted(counts.items()))
# #flipped = sort(flipped)
# print("flipped:")
# print(flippedd)        
# print(sorted(flipped.items()))