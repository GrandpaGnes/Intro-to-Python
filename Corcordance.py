
str1="Never give in — Never, never, never, never, in nothing great or small, \
large or petty, never give in except to convictions of honour and good sense. \
Never yield to force; never yield to the apparently overwhelming might of the enemy. O horror, horror, horror. \
Words, words, word. But you never know now do you now do you now do you."

rmstr1=str1.replace(',','')
rmstr2=rmstr1.replace(';','')
rmstr3=rmstr2.replace('.','')
rmstr4=rmstr3.replace('—','')
lowerstr1=rmstr4.lower()

str2=lowerstr1.split()
#print(str2)
uniqstr=[str2.sort()]

for i in str2:
    if i not in uniqstr:
        uniqstr.append(i)
        #print(uniqstr)

for i in range (1,len(uniqstr)):
    print("The word", uniqstr[i],"appears", str2.count(uniqstr[i]),"times")



