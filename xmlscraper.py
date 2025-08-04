import xml.etree.ElementTree as ET
tree = ET.parse('roll948.xml')

print(tree)

root = tree.getroot()
legisname = ""
critterandvote = ""
legisvote = ""

for legis in root.findall("./vote-data/recorded-vote/legislator/"):  #grabs legislators name
	legisname = legis.text+","
	
	for legisv in root.findall("./vote-data/recorded-vote/vote/"):
		legisvote = legisv.text
	
	critterandvote = legisname+legisvote
	
	print (critterandvote)
	
desc = root.find(".//vote-desc").text+","
print (desc)
print (critterandvote)
RCD = desc+critterandvote

nf=open("testthree.csv","w")   #doesnt creat csv, dont know why
nf.write(RCD)
nf.close()	
