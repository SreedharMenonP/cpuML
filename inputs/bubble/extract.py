file = open("bubbletimes.txt","r")
import csv
i=1
j=0
k=0
with open('data.csv', 'a',newline='') as fp:
	for line in file:
		a = csv.writer(fp,delimiter=",")
		if i==(1 + 3*j):
			row1 = line
			j=j+1
		elif i==(2 + 3*k):
			time = line.split(" ")
			time_0=time[0].split("user",1)[0]
			time_1=time[1].split("system",1)[0]
			time_2=time[2].split("elapsed",1)[0]
			data1 = [[row1,time_0,time_1,time_2]]
			a.writerows(data1)
			k=k+1
		i=i+1
file.close();
