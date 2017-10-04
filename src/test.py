import platform
import sys
import datetime
from pip._vendor.requests.packages.urllib3.util.connection import select

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

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

x = '40'
y = int(x) + 2
print(y)

x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])

print(len('banana')*7)

greet = '  Hello Bob  '

print(greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

x = range(5)
print(x)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

t = [9, 41, 12, 3, 74, 15]
print(t[2:4])
t.append(16)
print(t)

friends = [ 'Joseph', 'Glenn', 'Sally' ]
f2 = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends)

def chomp (thing):
    thing.pop(0)
    thing.pop(-1)
    
def chomp2 (thing2):
    t2 = thing2
    t2.pop(0)
    t2.pop(-1)
    return t2
    
print("is f2 frieds?", f2 is friends)
print(chomp(f2))
print(f2)

print(chomp(friends))
print(friends)

print("\n===============")
print("little class example, private var and call to increment it")

class PartyAnimal:
    x = 0
    name = ""  
    def __init__(self, nam):
        self.name = nam
        print(self.name,"constructed")        
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count",self.x)    
    def __del__(self):
        print(self.name,"destructed after",self.x,"parties")

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        print(self.name,"points",self.points)
        self.party()
            
an = PartyAnimal("an")
print("*** HERE ***")            
PartyAnimal.party(an)
print("*** HERE ***")            
joe = PartyAnimal("Joe")
jan = FootballFan("Jan")
bob = PartyAnimal("Bob")

#print(dir(an))
joe.party()
jan.touchdown()
joe.party()
joe.party()
jan.touchdown()
joe = 42
print("joe contains",joe)
print("===============")

# SQL test commands
# CREATE TABLE Users (
#   name VARCHAR(128),
#   email VARCHAR(128)
# )
# INSERT INTO Users (name, email) VALUES ('Brian Lawrence','B.Lawrence@F5.com')
# DELETE FROM Users WHERE email='B.Lawrence@F5.com'
# UPDATE Users SET name='Al Danielson' WHERE email='a.danielson@F5.com'
insert into artist (name) values (Led Zepplin)
insert into Album (title, artist_id) values ('IV', 1)
insert into Track (title, rating, len, count, album_id, genre_id) values ('Black Dog', 5, 297, 0, 2, 1)
select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id

select Track.title, Artist.name from 
    Track join Artist
    on Track.artist_id = Artist.id 


select Track.title, Artist.name, Album.title, Genre.name from 
    Track join Genre join Album join Artist
    on Track.genre_id = Genre.id 
    and Album.album_id = Artist.id 
    and Track.artist_id = Artist.id 



