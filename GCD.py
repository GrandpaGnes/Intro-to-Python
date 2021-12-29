

A = int(input ("Please enter an integer positive number A: "))
B = int(input ("Please enter an integer positive number B: "))
R = int(1)

if A >= B:
        while R>0:
            R = A % B
            print ("The Remainder A divide by B is %",R)
            A=B
            B=R
            print ("The greatest common divisor (GCB) for A & B is %", A)
else:
    print ("Error")
