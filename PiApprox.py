
Iter = input ("Insert Your Number of Iteration: ")
itr1 = int(Iter)

LstPos=[]
LstNeg=[]

n=1
m=1

if itr1!=1:

    for b in range (1,itr1+1):
        N=(1/n)
        LstPos.append(N)
        n = n+2
        #print (LstPos)
    for c in range (1,itr1,2):
        M=LstPos[c]*-1
        LstNeg.append(M)
        #print (LstNeg)
    
    Total=sum(LstPos)+sum(LstNeg)+sum(LstNeg)
    Pi = 4*Total
    #print ("Total : ",Total)
    print ("Approx Pi =",Pi)

else:
    Pi = 4
    print ("Approx Pi =",Pi)
    
    
    
