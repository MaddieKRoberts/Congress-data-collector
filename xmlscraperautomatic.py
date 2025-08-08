import xml.etree.ElementTree as ET
import requests

o = 218
k = 1

for ro in range(o):
	
<<<<<<< Updated upstream
<<<<<<< Updated upstream
	s = '{}.xml'.format(k)
	n = '2011houseroll'
	snum = s.rjust(7, '0')
	sandn = n+snum
	print (sandn)
	
	
	tree = ET.parse(sandn)
	print(tree)
	
	root = tree.getroot()
	legisname = ""
	critterandvote = ""
	legisvote = ""
	
	for v in root.findall("./vote-data/recorded-vote"):
		print(v[0].text)
		legisname = v[0].text+","
		legisvote = v[1].text+","+"\n"
		critterandvote = critterandvote+legisvote+legisname
	
=======
=======
>>>>>>> Stashed changes
	try:	
		s = '{}.xml'.format(k)
		n = '2025houseroll'
		snum = s.rjust(7, '0')
		sandn = n+snum
		print (sandn)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
		
		
		tree = ET.parse(sandn)
		print(tree)
		
		root = tree.getroot()
		legisname = ""
		critterandvote = ""
		legisvote = ""
		
		for v in root.findall("./vote-data/recorded-vote"):
			print(v[0].text)
			legisname = v[0].text+","
			legisvote = v[1].text+","+"\n"
			critterandvote = critterandvote+legisname+legisvote
		
			
		
		RCD = critterandvote
		
		filenameandcsv = n+'{}'.format(k)+".csv"
		print(filenameandcsv)
		nf=open(filenameandcsv,"w")
		nf.write(RCD)
		nf.close()	
		k=k+1
	except requests.exceptions.RequestException as e:
		print ("Error downloading file")