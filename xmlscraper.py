import xml.etree.ElementTree as ET
tree = ET.parse('roll948.xml')

print(tree)

root = tree.getroot()
legisname = ""
critterandvote = ""
legisvote = ""

for recordedvote in root.findall("./vote-data/"):  #grabs legislators name
	recordedvote = legis.text+","

# star dads code
for v in root.findall("./vote-data/recorded-vote"):
	# these two lines do the exact same thing, because v is
	#the first set of recorded votes, v[0] is the first legislator in the first recorded vote
	print(v[0].text)
	print(v.find('./legislator').text)
	
desc = root.find(".//vote-desc").text+","
print (desc)
print (critterandvote)
RCD = desc+critterandvote

nf=open("testthree.csv","w")   #doesnt creat csv, dont know why
nf.write(RCD)
nf.close()	
