import sqlite3

#creates connection to "congress.db"
conn = sqlite3.connect('congress.db')

#creates a cursor connected to "congress.db"
c = conn.cursor()

#update database
c.execute("DELETE from critters WHERE rowid = 3")


conn.commit()





#query the databse
c.execute("SELECT rowid, * FROM critters")

personvote = c.fetchall()

for critterandvote in personvote:
    print (critterandvote)


#commits our command
conn.commit()

#close our connection
conn.close