with open("data.csv","r") as f:
	import csv
	import random
	with open('testdata.csv', 'a',newline='') as f2:
		a = csv.writer(f2,delimiter=",")
		attri = [['inputsize','user','system','TT','elapsed','STS','text','rodata','data','bss']]
		a.writerows(attri)
		for x,line in enumerate(f):
			l=line.split(",")
			l1 = l[9].split("\n")
			if (x!= 0):
				sts = 0.08
				for c in range(8,41):
					#print(splitline[5],end="")
					sts = random.randrange(150,170)/1000
					data = [[l[0],l[1],l[2],'?',l[4],sts,l[6],l[7],l[8],l1[0]]]
					#print(l[9])
					a.writerows(data)
					#sts=sts + 0.005
					c=c+0.5
	

