#Inputs

HourlyWages = input ("How much is the Hourly Wages: ")
HW=float(HourlyWages)

NumRegHr = input ("What is the Regular Working Hour Per Day: ")
RH=float(NumRegHr)

TotalOverTime = input ("What is your Total Overtime Hour: ")
TOT=float(TotalOverTime)

#Compute

OverTimePay = 1.5*HW*TOT
TotalWeeklyPay = HW*RH*7 + OverTimePay

#Display

#print ("Total OverTimePay is $", OverTimePay)
print ("Your weekly pay for the week is $", TotalWeeklyPay)
