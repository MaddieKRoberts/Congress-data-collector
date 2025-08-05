import xml.etree.ElementTree as ET
tree = ET.parse('roll948.xml')

print(tree)

root = tree.getroot()
legisname = ""
critterandvote = ""
legisvote = ""

for recordedvote in root.findall("./vote-data/"):  #grabs legislators name
	recordedvote = legis.text+","

	
desc = root.find(".//vote-desc").text+","
print (desc)
print (critterandvote)
RCD = desc+critterandvote

nf=open("testthree.csv","w")   #doesnt creat csv, dont know why
nf.write(RCD)
nf.close()	
