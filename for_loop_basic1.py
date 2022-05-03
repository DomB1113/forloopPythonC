#Print all integers from 0 to 150
# for x in range(0,151):
#     print(x)

#Print all the multiples of 5 from 5 to 1,000
# y = 0 
# while(y<=1000):
#     print(y)
#     y += 5

# Print integers 1 to 100. If divisible by 5, print "Coding" instead.
# If divisible by 10, print "Coding Dojo".

# for i in range(0,101):
#     if(i % 10 ==0):
#         print("Coding Dojo")
#     elif(i % 5 == 0):
#         print("Coding")
#     else:
#         print(i)


# Add odd integers from 0 to 500,000, and print the final sum.

finalSum = 0
for L in range(1,500000,2):
    finalSum += L
print(finalSum)


# Print positive numbers starting at 2018, counting down by fours.
# positiveNum = 2018
# while(positiveNum > 0):
#     print(positiveNum)
#     positiveNum -= 4

#  Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
#  For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

# lowNum = 0
# highNum= 5
# mult = 5
# for F in range(lowNum,highNum,mult):
#     print(F)