#Initialize the constants

TAX_RATE = 0.2
STANDARD_DEDUCTION = 10000.0
DEPENDANT_DEDUCTION = 3000.0

#Request Inputs

grossIncome = input ("Enter Gross Income: ")
numDependents = input ("Enter no.dependents: ")

#ComputeIncomeTax
taxableIncome = float (grossIncome) - STANDARD_DEDUCTION - \
                DEPENDANT_DEDUCTION*int(numDependents)

incomeTax = taxableIncome*TAX_RATE

#Display incometax

print ("The income tax is $" + str(incomeTax))
print ("The income tax is $", incomeTax)
