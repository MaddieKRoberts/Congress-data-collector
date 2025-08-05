import xml.etree.ElementTree as ET

ranger = 948
thingy = 1

for ro in range(ranger):

	somefilename = '2011houseroll'
	otherthing = '{}.xml'.format(thingy)
	z = otherthing.rjust(7, '0')
	filename = somefilename+z
	threething = '{}'.format(thingy)
	downloadedfilename = somefilename+threething
	tree = ET.parse(filename)
	print(tree)
	
	root = tree.getroot()
	legisname = ""
	critterandvote = ""
	legisvote = ""
	
#	for v in root.findall("./vote-data/recorded-vote"):
#		print(v[0].text)
#		legisname = v[0].text+","
#		legisvote = v[1].text+","+"\n"
#		critterandvote = critterandvote+legisname+legisvote
	
		
	
	RCD = "blarg" #critterandvote
	
	filenameandcsv = downloadedfilename+".csv"
	nf=open(filenameandcsv,"w")
	nf.write(RCD)
	nf.close()	
	thingy+1
