from datetime import datetime
class SaveAccount:

    def __init__(self, firstname,lastname,today):
        self.AccFirstname = firstname
        self.AccLastname = lastname
        self.AccFullname = firstname+lastname
        self.Today = today
        self.AccNum = lastname + "520149"
        self.AccPin = firstname + "123456"
        self.depowith = float(0.0)
        self.AccBalance = float(0.0)
        self.AccInterest = float (0.02)
        
    def CreateAccount(self):
        try:
            check = open(self.AccFullname+".txt")
        except:
            print("Creating New Account")
            #newfile = open(self.AccFullname+".txt","w")
            #header = ("'Account Name'\t'Account Number'\t'Account Pin'\t'Transaction'\t'Account Balance'\t'Interest'")
            #newfile.write(header)
            #print (header)
            #newfile.close()
            newfile = open(self.AccFullname+".txt","w")
            name = self.AccFullname
            AC = self.AccNum
            pin = self.AccPin
            change = self.depowith
            bal = self.AccBalance
            cumint = self.AccInterest
            date = self.Today
            #print(name, AC, pin, change, bal, cumint, date)
            newfile.write("\n{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(name, AC, pin, change, bal, cumint, date))
            newfile.close()
            print ("New Account Opened. Done")
            print ("Please login")
            
        else:
            print ("You already have an account with us. Please login your account.")
            check.close()
            
    def verifyInfo(self):
        try:
            check = open(self.AccFullname+".txt")
        except:
            print ("Please create an account.")
        else:
            with open(self.AccFullname+".txt","r") as fopen:
                alline = fopen.read()
                split = alline.split()
                #print(split)
                verify = input("Please enter pin: ")
                if verify == split[2]:
                    print("Correct Pin. Done")
                    #ac=split[1]
                    #b=float(split[4])
                    #print ("Account Number: {}".format(ac)+ "\nYour Balance: {:.2f}".format(b))
                else:
                    print ("Wrong Pin. Try Again")

    def verifyName(self):
        try:
            check = open(self.AccFullname+".txt")
        except:
            print ("Please create an account.")
        else:
            with open(self.AccFullname+".txt","r") as fopen:
                alline = fopen.read()
                split = alline.split()
                #print(split)
                verify = input("Please enter account number: ")
                if verify == split[1]:
                    print("Account Number exist!")
                    #print ("Account Number: {}".format(ac)+ "\nYour Balance: {:.2f}".format(b))
                else:
                    print ("Wrong Account Number. Try Again")

    def getBalance (self):
        with open(self.AccFullname+".txt","r") as fopen:
                alline = fopen.read()
                split = alline.split()
                #print(split)
                ac=split[1]
                b=float(split[4])
                print ("Account Number: {}".format(ac)+ "\nYour Balance: {:.2f}".format(b))
                
    def getName (self):
        with open(self.AccFullname+".txt","r") as fopen:
                alline = fopen.read()
                split = alline.split()
                #print(split)
                n=split[0]
                print ("Acc Owner: {}".format(n))

    def getPin (self):
        with open(self.AccFullname+".txt","r") as fopen:
                alline = fopen.read()
                split = alline.split()
                #print(split)
                p=split[2]
                print ("Your Pin: {}".format(p)) 

    def deposit (self):
        ans = input("Deposit? (y = yes, n= no): ")
        if ans == 'y':
            self.depowith = float(input("Amount to Deposit: "))
            with open(self.AccFullname+".txt","r") as fopen:
                alline = fopen.read()
                split = alline.split()
                #print(split)
                b=float(split[4])
                nb = b + self.depowith
                print ("Your New Balance: {:.2f}".format(nb))
            fopen = open(self.AccFullname+".txt","w")
            name = self.AccFullname
            AC = self.AccNum
            pin = self.AccPin
            change = self.depowith
            bal = nb
            cumint = self.AccInterest
            date = self.Today
            #print(name, AC, pin, change, bal, cumint, date)
            fopen.write("\n{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(name, AC, pin, change, bal, cumint, date))
            fopen.close()
                
        if ans == 'n':
            return

    def withdraw (self):
        ans = input("Withdraw? (y = yes, n= no): ")
        if ans == 'y':
            self.depowith = float(input("Amount to Withdraw: "))
            with open(self.AccFullname+".txt","r") as fopen:
                alline = fopen.read()
                split = alline.split()
                #print(split)
                b=float(split[4])
                nb = b - self.depowith
                if self.depowith > b:
                    print ("Amount Withdraw exceed Balance.")
                    fopen.close
                    return
                else:
                    print ("Your New Balance: {:.2f}".format(nb))
                fopen = open(self.AccFullname+".txt","w")
                name = self.AccFullname
                AC = self.AccNum
                pin = self.AccPin
                change = self.depowith
                bal = nb
                cumint = self.AccInterest
                date = self.Today
                #print(name, AC, pin, change, bal, cumint, today)
                fopen.write("\n{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(name, AC, pin, change, bal, cumint, date))
                fopen.close()
                return
        if ans == 'n':
            return

    def computeInterest (self):
        with open(self.AccFullname+".txt","r") as fopen:
                alline = fopen.read()
                split = alline.split()
                Olddate = datetime.strptime(split[6],'%Y-%m-%d')
                #print(Olddate)
                #print(split)
                fopen = open(self.AccFullname+".txt","w")
                name = split[0]
                AC = split[1]
                pin = split[2]
                change = split[3]
                bal = float(split[4])
                date = datetime.strptime(self.Today,'%Y-%m-%d')
                when = date-Olddate
                passed = int(when.days)
                cumint = float(float(split[4])*passed/365*0.02)
                #print(split)
                #print(bal, date, passed, when, cumint)
                nb = bal + cumint
                #print(bal, date, passed, when, cumint,nb)
                fopen.write("\n{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(name, AC, pin, change, nb, cumint, date))
                fopen.close()
        return 
