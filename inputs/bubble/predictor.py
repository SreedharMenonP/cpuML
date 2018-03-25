import csv
import re
file1 = open("predictionbubble.csv")
r = next(file1)
i = 0
j=1
k=33
list1 = list(list())
l = []
list2 = []
minlist = []
for row in file1:
    if i<k:
        #l = []
        l.append(row)
        i=i+1
    else:
         s = row
         print(j,l,l[0][1],"\n")
         for sl in l:
             cc = sl.split(",")
             list2.append(sl.split(","))
             print(sl.split(","),"\n")
         print(list2,"\n")
         v = min(list2,key=lambda x: x[2])
         print(v,"\n")
         minlist.append(v)
         list2.clear()
         list1.append(l)
         l.clear()
         l.append(s)
         j=j+1
         k=k+32


for a, b in enumerate(minlist, 1):
    print( '{} {}'.format(a, b))
finallist = []
file2 = open("testdata.csv")
r = next(file2)
testdatalist=list(file2)
for mini in minlist:
    #print(type(testdatalist[int(mini[0])]))
    finallist.append((testdatalist[int(mini[0])].split(",")))
print(finallist[0][0])
#for m in list1:
#     print(m[0])
#print(list)

with open('finaltrainingset.csv', 'a',newline='') as fp:
    a = csv.writer(fp,delimiter=",")
    for i in range(0,len(finallist)):
        l9 = finallist[i][9].split("\n")
        newlist=[[finallist[i][0],finallist[i][5],finallist[i][6],finallist[i][7],finallist[i][8],l9[0]]]
        a.writerows(newlist)
