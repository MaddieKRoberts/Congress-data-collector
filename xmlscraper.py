import xml.etree.ElementTree as ET
tree = ET.parse('rollcall949.xml')

print(tree)

root = tree.getroot()
for bill in root.iter ('bill')
	print (bill.text)