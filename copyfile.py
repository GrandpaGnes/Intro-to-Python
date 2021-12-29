
fname1=input("Origin Filename to copy: ")
fname2=input("Create new Filename: ")
fhand2 = open(fname2,'w')

try:
    fhand1 = open(fname1,'r')
    inp = fhand1.read()
    #print(inp)
    
except:
    print("File not found! Error.")
    quit()

for lines in inp:
    fhand2.write(lines)

fhand1.close()
fhand2.close()

