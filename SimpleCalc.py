
X = input ("Please insert a number x : ")
Y = input ("Please insert a number y : ")

x=int(X)
y=int(Y)

Calc = input ("Please choose an Arithmetric Operator (Plus = 0, Minus = 1, Multiplication = 2, Divide = 3) : ")

C=int(Calc)

if C == 0:
   F = x + y
   print ("x plus y =", F)
elif C == 1:
     F = x - y
     print ("x minus y =", F)
elif C == 2:
     F = x * y
     print ("x times y =", F)      
elif C == 3:
     F = x/y
     print ("x divide y =", F)
else:
    print ("Wrong Operator, Please select within 0 to 3")


