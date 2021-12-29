
#data=[2,3,4,5,8,4,6,3,4,6,8,9,7,5,3,5,7,4,3,2,2,1,4,6,8,6,8,9,3]

i=0
L1=[]

def calcMode(data):
    if data!=0:
        data.sort()
        for i in data:
            num=data.count(i)
            L1.append(num)
            dic1=dict(zip(data,L1))
            dic2={d for (d,l) in dic1.items() if l == max(L1)}
        return str(dic2)
    else:
        return 0


def calcMedian(data):
    if data!=0:
        c = len(data)
        data.sort()
        if c % 2 == 0:
            meda = data[c//2]
            medb = data[c//2-1]
            medf = (meda+medb)/2
        else:
            medf = data[c//2]
        return medf
    else:
        return 0


def calcMean(data):
    if data!=0:
        c = len(data)
        avg = (sum(data)/c)
        return avg
    else:
        return 0
    
    
    




#c = len(data)
#data.sort()
#print(data)
#if c % 2 == 0:
#    meda = data[c//2]
#    medb = data[c//2-1]
#    medf = (meda+medb)/2
#else:
#    medf = data[c//2]
#print (medf)
        

#data.sort()
#for i in data:
    #num=data.count(i)
    #L1.append(num)
    #dic1=dict(zip(data,L1))
    #dic2={d for (d,l) in dic1.items() if l == max(L1)}
    #dic2=str(dic2)
#print(dic1)
#print(dic2)

        
    


    
