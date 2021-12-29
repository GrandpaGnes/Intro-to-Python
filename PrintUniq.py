
fname1=input("Filename to use: ")

try:
    fhand1 = open(fname1,'r')
    inp = fhand1.read()
    str1 = inp
    rmstr1=str1.replace(',','')
    rmstr2=rmstr1.replace(';','')
    rmstr3=rmstr2.replace('.','')
    rmstr4=rmstr3.replace('—','')
    lowerstr1=rmstr4.lower()
    str2 = lowerstr1.split()
    uniqstr=[str2.sort()]
    uniqstr2=[]
    for i in str2:
        if i not in uniqstr:
            uniqstr.append(i)
            #print(uniqstr)

    for i in range (1,len(uniqstr)):
        if str2.count(uniqstr[i])==1:
            uniqstr2.append(uniqstr[i])
        else:
            continue
    print("The unique words from input text file shown as list below:")
    print(uniqstr2)
            
       
except:
    print("File not found! Error.")
    quit()
