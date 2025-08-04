import xml.etree.ElementTree as ET
tree = ET.parse('rollcall949.xml')

print(tree)

root = tree.getroot()

for legis in root.findall("./vote-data/recorded-vote/"):  #grabs legislators name & vote
	legisvote = legis.text+","
	print (legisvote)
	
for desc in root.findall("./vote-metadata/vote-desc/"):   #should grab the bill description, doesnt, dont know why
	description = desc.tag
	print (description)
	
nf=open("RCH949.csv","w")   #doesnt creat csv, dont know why
nf.write(legisvote)
nf.close()	
