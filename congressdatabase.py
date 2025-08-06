import sqlite3

#creates connection to "congress.db"
conn = sqlite3.connect('congress.db')

#creates a cursor connected to "congress.db"
c = conn.cursor()

#creates a table in congress
c.execute("""CREATE TABLE critters (
        name DATATYPE,
        vote DATATYPE,
    )""")