import csv
mycsv = csv.reader(open("predictionbubble.csv"))
l=list()
i=0
j=0

for row in mycsv:
	if i<=33:
		i=i+1
		if i!=1:
			print(row[2])
			l.append([float(row[2]),i])	
l=sorted(l)
b=list()
#print(l)
n,m = min(l)
for a in l:
	if a[0]	== n:
		b.append(a[1])
minVal = n
#print(b)
newcsv =  csv.reader(open("testdata.csv"))
i=1
c=list()
for row in newcsv:
	if i in b:
		i=i+1
		#print(row)
		c.append(float(row[5]))
	else:
		i=i+1		
z=sum(c)/len(c)
print(z)
print(minVal)		
