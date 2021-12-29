from stats import calcMode
from stats import calcMedian
from stats import calcMean

mathli=[2,3,4,5,8,4,6,3,4,6,8,9,7,5,3,5,7,4,3,2,2,1,4,6,8,6,8,9,3]

mode = calcMode(mathli)
#print(mathli)
print("Mode for list is/are:", mode)


med = calcMedian(mathli)
#print(mathli)
print("Median for list is:", med)

mean = calcMean(mathli)
#print(mathli)
print("Mean for list is:", mean)



