import congdatafunc
import sqlite3
import time

congdatafunc.emergencydeletetable()
r = 1990
n = 1
t = 1200
for i in range(r):
    year = r
    for z in range(t):
        num = n
        congdatafunc.addhousebill(year, num)
        num+1
        time.sleep(10)
    year+1
