from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
visited = list()
todo = list()

url = "https://github.com"
count = 1
position = 0

while count>0:
    print("====== To Retrieve:",count, "To Read:", url)
    count = count - 1
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    pCnt = 0
    for tag in tags:
        pCnt += 1
        url = tag.get('href', None)
        if (url is not None and re.search(r'http',url)):
            #wPage = re.findall('http',url)
            print("URL:",url)
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

