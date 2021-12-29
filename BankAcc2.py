from datetime import date
from datetime import datetime
from SavingsAccount2 import SaveAccount


today = str(date.today())

print ("Welcome to XXX Bank.")
Ans = input("Create New Acc (y=Yes, n=No, o=retrievepin):")

if Ans == 'y' or 'n' or 'o':

    if Ans == 'y':
        print ("Create Your New Account......")
        firstname = input("Please enter your first name:  ")
        lastname = input("Please enter your last name:  ")
        myobj=SaveAccount(firstname,lastname, today)
        myobj.CreateAccount()
        myobj.verifyInfo()
        myobj.computeInterest()
        myobj.getBalance()
        myobj.getName()
        #myobj.getPin()
        myobj.deposit()
        myobj.withdraw()
    
        print("Done")

    if Ans == 'n':
        firstname = input("Please enter your first name:  ")
        lastname = input("Please enter your last name:  ")
        myobj=SaveAccount(firstname,lastname, today)
        myobj.verifyInfo()
        myobj.computeInterest()
        myobj.getBalance()
        myobj.getName()
        ##myobj.getPin()
        myobj.deposit()
        myobj.withdraw()

        print("Done")

    if Ans == 'o':
        firstname = input("Please enter your first name:  ")
        lastname = input("Please enter your last name:  ")
        myobj=SaveAccount(firstname,lastname, today)
        myobj.verifyName()
        myobj.getPin()

else:
    print("Invalid input. Please try again")

