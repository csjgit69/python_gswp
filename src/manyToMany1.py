import xml.etree.ElementTree as ET
import sqlite3
 
conn = sqlite3.connect('many2many1.sqlite')
cur = conn.cursor()
 
# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
 
CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT,
    email   TEXT
     
);
 
CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT
);
 
CREATE TABLE Member (
    user_id    INTEGER,
    course_id  INTEGER,
    role       INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')
name = 'Jane'
email = 'jane@tsugi.org'
cur.execute('''INSERT OR IGNORE INTO USER (name, email) VALUES ( ?, ? )''', ( name,email ) )
name = 'Ed'
email = 'Ed@tsugi.org'
cur.execute('''INSERT OR IGNORE INTO USER (name, email) VALUES ( ?, ? )''', ( name,email ) )
name = 'Sue'
email = 'Sue@tsugi.org'
cur.execute('''INSERT OR IGNORE INTO USER (name, email) VALUES ( ?, ? )''', ( name,email ) )

title = 'Python'
cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', ( title, ) )
title = 'SQL'
cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', ( title, ) )
title = 'PHP'
cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', ( title, ) )

cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id,role) VALUES ( 1,1,1 )''')
cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id,role) VALUES ( 2,1,0 )''')
cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id,role) VALUES ( 3,1,0 )''')

cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id,role) VALUES ( 1,2,0 )''')
cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id,role) VALUES ( 2,2,1 )''')

cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id,role) VALUES ( 2,3,1 )''')
cur.execute('''INSERT OR IGNORE INTO Member (user_id,course_id,role) VALUES ( 3,3,0 )''')

cur.execute('''select User.name, Member.role, Course.title 
    From User JOIN Member Join Course
    on Member.user_id = User.id AND Member.Course_id = Course.id 
    ORDER BY Course.title, Member.role DESC, User.name''')
    

conn.commit()
# 
# 
# # fname = input('Enter file name: ')
# # if ( len(fname) < 1 ) : fname = 'Library.xml'
# # 
# # # <key>Track ID</key><integer>369</integer>
# # # <key>Name</key><string>Another One Bites The Dust</string>
# # # <key>Artist</key><string>Queen</string>
# # def lookup(d, key):
# #     found = False
# #     for child in d:
# #         if found : return child.text
# #         if child.tag == 'key' and child.text == key :
# #             found = True
# #     return None
# 
# stuff = ET.parse(fname)
# all = stuff.findall('dict/dict/dict')
# print('Dict count:', len(all))
# for entry in all:
#     if ( lookup(entry, 'Track ID') is None ) : continue
# 
#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     genre = lookup(entry, 'Genre')
#     album = lookup(entry, 'Album')
#     count = lookup(entry, 'Play Count')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')
# 
#     if name is None or artist is None or genre is None or album is None or count is None or rating is None: 
#         continue
# 
#     print(name, artist, genre, album, count, rating, length)
#     print("name",name)
#     print("artist",artist)
#     print("genre", genre)
#     print("album", album)
#     print("count", count)
#     print("rating", rating)
#     print("length", length)
# 
#     cur.execute('''INSERT OR IGNORE INTO Artist (name) 
#         VALUES ( ? )''', ( artist, ) )
#     cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
#     artist_id = cur.fetchone()[0]
#     
#     cur.execute('''INSERT OR IGNORE INTO Genre (name) 
#         VALUES ( ? )''', ( genre, ) )
#     cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
#     genre_id = cur.fetchone()[0]
# 
#     cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
#         VALUES ( ?, ? )''', ( album, artist_id ) )
#     cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
#     album_id = cur.fetchone()[0]
# 
#     cur.execute('''INSERT OR REPLACE INTO Track
#         (title, album_id, genre_id, len, rating, count) 
#         VALUES ( ?, ?, ?, ?, ?, ? )''', 
#         ( name, album_id, genre_id, length, rating, count ) )
#     cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
#         FROM Track JOIN Genre JOIN Album JOIN Artist 
#         ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
#         AND Album.artist_id = Artist.id
#         ORDER BY Artist.name LIMIT 3''')
# 
#     conn.commit()
#     #break
