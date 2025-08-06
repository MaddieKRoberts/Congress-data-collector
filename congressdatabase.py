import sqlite3

#creates connection to "congress.db"
conn = sqlite3.connect('congress.db')

#creates a cursor connected to "congress.db"
c = conn.cursor()

#query the databse
c.execute("SELECT * FROM critters")
#c.fetchone()
#c.fatchmany(3)
personvote = c.fetchall()

for i in personvote:
    print(i[1])


#commits our command
conn.commit()

#close our connection
conn.close