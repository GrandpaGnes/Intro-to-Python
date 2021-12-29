

D = [("Lambert",34,10.50),("Osborne",22,6.25),("Giacometti",5,100.70)]

print("{}\t{}\t{}".format('Last_Name','Hourly_Wages','Paid_Wages'))

for d in D:
    LN,HW,WH=d
    PW=HW*WH
    Len=len(LN)
    if Len<=7:
        print("{}\t\t{}\t\t{:.2f}".format(LN,HW,PW))
    else:
        print("{}\t{}\t\t{:.2f}".format(LN,HW,PW))

  
    




