import platform
import sys
import datetime

if __name__ == '__main__':
    print("_____Hello World_____")

print("Python major version: %s"%sys.version_info.major)
print()  
print("Python system version info:")
print(sys.version)
print(sys.version_info.releaselevel)
print(sys.platform)

print()
print("Python version in use: %s" %platform.python_version())

print("There are <", 2**3, "> possibilities!")
print('eggs', 'ham', sep='\t')
print('eggs', 'ham', sep=' -> ')

print("There are <", 2**32, "> possibilities!", sep='')
print("Today is: {0:%a %b %d %H:%M:%S %Y}".format(datetime.datetime.now()))

print("My name is {0:8}".format('Fred'))

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)