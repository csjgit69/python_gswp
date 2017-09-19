import platform
import sys
import datetime

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

tLen = len(text)
sPos = text.find(':')
#print(text[sPos+1],text[tLen])
sStr = text[sPos+1:]
sStr = sStr.strip()
num = float(sStr)
print(num)
print(tLen)
print(text[0], text[28], text[-1])
