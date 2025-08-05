import xml.etree.ElementTree as ET

o = 948
k = 1

for ro in range(o):
	
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
		critterandvote = critterandvote+legisname+legisvote
	
		
	
	RCD = critterandvote
	
	filenameandcsv = n+'{}'.format(k)+".csv"
	print(filenameandcsv)
	nf=open(filenameandcsv,"w")
	nf.write(RCD)
	nf.close()	
	k=k+1
