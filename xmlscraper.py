import xml.etree.ElementTree as ET
tree = ET.parse('roll948.xml')

print(tree)

root = tree.getroot()
legisname = ""
critterandvote = ""
legisvote = ""

for v in root.findall("./vote-data/recorded-vote"):
	# these two lines do the exact same thing, because v is
	#the first set of recorded votes, v[0] is the first legislator in the first recorded vote
	print(v[0].text)
	legisname = v[0].text+","
	legisvote = v[1].text+","+"/n"
	critterandvote = legisname+legisvote

	
desc = root.find(".//vote-desc").text+","
print (desc)
print (critterandvote)
RCD = desc+critterandvote

nf=open("testfive.csv","w")   #doesnt creat csv, dont know why
nf.write(RCD)
nf.close()	
