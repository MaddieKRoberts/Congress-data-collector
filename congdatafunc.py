import sqlite3
import xml.etree.ElementTree as ET
import requests


def addhousebill(year, num):
    
    #connects to database and adds a tabl
    conn = sqlite3.connect('housedata.db')
    c = conn.cursor()
    crittervote = crittervote+year+num
    c.execute("""CREATE TABLE (?) (
            vote text,
            name text,
         )"""(crittervote))
    

    #finds url based on year and number provided
    s = "{}.xml".format(num)
    urlnum = s.rjust(7, 0)
    urlyear = "https://clerk.house.gov/evs/{}/roll".format(year)
    url =  urlyear+urlnum

    #creates filename to write as
    filename = year+houserollcall+num

    #downloads file
    try:
	    response = requests.get(url, stream=True)
		response.raise_for_status()
	
		with open(filename, 'wb') as f:
			for chunk in response.iter_content(chunk_size=8192):
			f.write(chunk)
		     print(f"file '{filename}' downloaded successfully.")
			
	    except requests.exceptions.RequestException as e:
		    print (f"Error downloading file: {e}")
    
    #scrapes the file
    print (filename)
	tree = ET.parse(filename)
	print(tree)
	
	root = tree.getroot()
	legisname = ""
	critterandvote = ""
	legisvote = ""
	
	for v in root.findall("./vote-data/recorded-vote"):
		print(v[0].text)
		legisname = v[0].text+","
		legisvote = v[1].text+","+"\n"
		c.execute("INSERT INTO crittervote VALUES (?,?)",(legisvote, legisname))
    
    c.execute("SELECT rowid, * FROM crittervote")
    print(c.fetchall())
    
	
		
	

	


