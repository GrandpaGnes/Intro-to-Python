
fname1=input("Input the first Filename: to compare: ")
fname2=input("Input the second Filename: to compare: ")

fhand1=open(fname1,'r')
fhand2=open(fname2,'r')
#fhand1=open("AboutText2.txt",'r')
#fhand2=open("NotAboutText2.txt",'r')

count=0

for linef1 in fhand1:
    count=count+1
    
    for linef2 in fhand2:
        
        if linef1 == linef2:
            print("YES")
        else:
            print("NO")
            
            linef1=linef1.rstrip()
            linef2=linef2.rstrip()
            
            print("Line:",count,"\tFirst File: ",linef1)
            print("Line:",count,"\tSecond File: ",linef2)
        break
            
fhand1.close()
fhand2.close()
        
            
