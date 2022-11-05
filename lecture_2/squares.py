from functions import sqr
#import functions then use sqr as functions.sqr

sumOfSqr=0

for x in range(10):
    print(f"sqr of {x+1} is {sqr(x+1)}")
    sumOfSqr+=sqr(x+1)

print(f"Sum of sqr is {sumOfSqr}")