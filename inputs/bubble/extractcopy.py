import csv
list2=[]
with open ("sizebubble.txt","r") as file2:
	for line in file2:
				for x,line in enumerate(file2):
					splitline = line.split()
					if (x==13 or x==15 or x==23 or x==24):
						list2.append(int(splitline[1]))
			#print(list2)
file2.close()
with open('datacopy2.csv', 'w',newline='') as fp:
	a = csv.writer(fp,delimiter=",")
	attri = [['inputsize','user','system','TT','elapsed','STS','text','rodata','data','bss']]
	a.writerows(attri)
	for c in range(0,100):
		#print("hai")
		i=1
		j=0
		k=0
		with open("bubbletimes.txt","r") as file1,open ("sizebubble.txt","r") as file2:
			for line in file1:
				if i==(1 + 3*j):
					row1 = line.split();
					j=j+1
				elif i==(2 + 3*k):
					time = line.split(" ")
					time_0=time[0].split("user",1)[0]
					time_1=time[1].split("system",1)[0]
					time_2=time[2].split("elapsed",1)[0]
					time_exec = float(time_0) + float(time_1)
					sts = 0.16
					for x in range(0,10):
						data1 = [[row1[0],time_0,time_1,time_exec,time_2,sts,list2[0],list2[1],list2[2],list2[3]]]
						a.writerows(data1)
						sts = sts + 0.001
					k=k+1
				i=i+1
			c=c+1
		file1.close();
		file2.close();
