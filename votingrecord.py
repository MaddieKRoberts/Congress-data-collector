d=open("C:/Users/Kolro/Downloads/sen113kh.ord","r")

gd=""

rccd=d.read()
lines=rccd.splitlines()
def rundata(rccd):
	nccd=[]
	gd=""
	for i in rccd.split( ):
		nccd.append(i)
	print(nccd)
	for si in nccd[-2]:
		if si.isalpha():
			gd=gd+si

	gd=gd+","
	for ti in nccd[-1]:
		gd=gd+ti+","

	return gd

for ln in lines:
	gd=gd+rundata(ln)+"\n"

nf=open("sen113data.csv","w")
nf.write(gd)
nf.close()















