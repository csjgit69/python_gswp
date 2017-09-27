# Following Links in Python
# 
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.
# 
# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data
# you need to process for the assignment
# 
# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
#
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Cristian.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: K
#
# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without
# writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete
# the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
# 
# Sample execution
# 
# Here is a sample execution of a solution:
# 
# $ python3 solution.py
# Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
# The answer to the assignment for this execution is "Anayah".


# for tag in tags:
#    if position is specified position
#       get the tag at the href
#       print the url 

#import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
visited = list()
todo = list()
# Let user input a URL
#url = input('Enter URL: ')
#count = int(input('Enter count: '))
#position = int(input('Enter position: '))

# hard-coded sample URL
#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
#count = 4
#position = 3

url = "http://py4e-data.dr-chuck.net/known_by_Cristian.html"
count = 7
position = 18

while count>0:
    print("====== To Retrieve:",count, "To Read:", url)
    count = count - 1
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    pCnt = 0
    for tag in tags:
        #print("Tags:",tag)
        pCnt += 1
        url = tag.get('href', None)
        if (url is not None and pCnt == position): break
print("Visited:",url)

# url = "http://py4e-data.dr-chuck.net/known_by_Cristian.html"
# count = 7
# position = 18
# 
# todo.append(url)
# 
# while count >0:
#     url = todo.pop()
#     #print("====== To Retrieve:",count, "To Read:", url)
#     count = count - 1
#     html = urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, "html.parser")
#     visited.append(url)
# 
#     # Retrieve all of the anchor tags
#     tags = soup('a')
#     pCnt = 0
#     for tag in tags:
#         #print("Tags:",tag)
#         pCnt += 1
#         newurl = tag.get('href', None)
#         if (newurl is not None and pCnt == position):
#             todo.append(newurl)
#             break
#print("Visited:",todo.pop())

