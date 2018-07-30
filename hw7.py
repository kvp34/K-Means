import sys
import random

# read data file
datafile = sys.argv[1]

with open(datafile) as f:
    data=[]
    i=0
    l=f.readline()
    while (l!=''):
        a=l.split()
        l2=[]
        for j in range(0,len(a),1):
            l2.append(float(a[j]))
        data.append(l2)
        l=f.readline()
rows=len(data)
cols=len(data[0])

k = int(sys.argv[2])
trainlabels={}

for x in range(0,rows):
    trainlabels[x]=random.sample(range(0, k), 1)[0]  

#distance between vector
def distance(list1,list2):
    dist = [(a - b)**2 for a, b in zip(list1, list2)]
    return sum(dist)
	
prevobj = 10000000
obj = prevobj - 10
stop_cond=0.001

while(prevobj - obj > stop_cond):
    prevobj = obj
    
    #Calculate mean
    m = [[0] * cols for i in range(k)]
    n = [0] * k
    for x in range(0,rows):
        for z in range(0,k):
            if(trainlabels.get(x)==z):
                n[z]=n[z]+1
                for y in range(0,cols):
                    m[z][y]=m[z][y]+data[x][y]
    for z in range(0,k):
        for y in range(0,cols):
            if(n[z]!=0):
                m[z][y]=m[z][y]/n[z]
                
    #Reassign Clusters
    dist=[]
    for i in range(0,rows):
        d1=[]
        for z in range(0,k):
            d1.append(distance(m[z],data[i]))
        dist.append(d1)
    for i in range(0,rows):
        trainlabels[i]=dist[i].index(min(dist[i]))
    
    #objective
    obj=0
    for x in range(0,rows):
        for z in range(0,k):
            if(trainlabels.get(x)==z):
                obj=obj+(distance(m[z],data[x]))
    print("Objective = ",obj)

for i in range(0, rows, 1):
        print(trainlabels[i], " ",i)