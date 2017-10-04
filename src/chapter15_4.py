
import sqlite3
import re

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Tracks''')

cur.execute('''CREATE TABLE Tracks (title TEXT, plays INTEGER)''')

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)', ('My Way', 15))
conn.commit()
print("Tracks:")
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
    
# cur.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()

cur.execute('SELECT * FROM Tracks WHERE title = ?',('My Way',))
conn.commit()
for thing in cur:
    print(dir(cur))

conn.close()


