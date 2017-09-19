import platform
import sys
import datetime


# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# fname = raw_input("Enter file name: ")

#name = raw_input("Enter file:")
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
names = dict()

for line in handle:
    if "From " not in line: continue
    lst = line.split()
    #print(lst)
    names[lst[1]] = names.get(lst[1],0)+1
biggest = None
name    = None 
for key,val in names.items():
    if (biggest is None or val>biggest):
        biggest = val
        name = key    
print(name,biggest)