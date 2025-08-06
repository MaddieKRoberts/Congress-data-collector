import sqlite3

#creates connection to "congress.db"
conn = sqlite3.connect('congress.db')

#creates a cursor connected to "congress.db"
c = conn.cursor()

c.execute("INSERT INTO critters VALUES ('John', 'yea')")



#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#commits our command
conn.commit()

#close our connection
conn.close