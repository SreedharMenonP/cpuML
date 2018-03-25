import csv
mycsv = csv.reader(open("predictionbubble.csv"))
l=list()
i=1
j=0
zz=1
newList = list()
row1 = next(mycsv)
for row in mycsv:
	if i<=33:
		l.append([float(row[2]),row[0]])
		i=i+1
		##if i!=1:
			#print(row[2])
			#l.append([float(row[2]),i])
	else:
		i=0
		l=sorted(l)
		b=list()
		#print(l)
		n,m = min(l)
		for a in l:
			if a[0]== n:
				b.append(int(a[1]))
		minVal = n
		#print(b)
		newcsv =  csv.reader(open("testdata.csv"))
		ii=1
		myrow=next(newcsv)
		c=list()
		b=sorted(b)
		# print(b)
		for rr in newcsv:
			if ii in b:
				ii=ii+1
				# print(rr)
				c.append(float(rr[5]))
			else:
				ii=ii+1
		z=sum(c)/len(c)
		newList.append([z,minVal])
		l.clear()

with open('finaltest.csv', 'a',newline='') as fp:
	a = csv.writer(fp,delimiter=",")
	a.writerows(newList)
