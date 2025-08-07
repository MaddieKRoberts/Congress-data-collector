import xml.etree.ElementTree as ET

o = 948
k = 1

for ro in range(ranger):
	
	s = '{}.xml'.format(k)
	n = '2011houseroll'
	snum = s.rjust(7, '0')
	sandn = n+snum
	print (sandn)
	k=k+1
	
	
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
	
	filenameandcsv = downloadedfilename+".csv"
	print(filenameandcsv)
	nf=open(filenameandcsv,"w")
	nf.write(RCD)
	nf.close()	
	thingy+1

