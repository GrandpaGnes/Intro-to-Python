
Num=[]
C=0

while True:
        A = input("Please enter a number to continue or ENTER to quit: ")
        if A != '':
            Num.append(int(A))
            C=C+1
            #print (Num)
            #print (C)
        elif A == '':
            S = sum(Num)
            #print(S)
            V = int(S/C)
            #print(V)
            print ("The sums of all numbers ", S)
            print ("The average of all numbers ",V)
            break
        
        
