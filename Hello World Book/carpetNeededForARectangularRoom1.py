print('What is the rooms width? (in feet)')
width = float(input())
print()
print('What is the rooms length? (in feet)')
length = float(input())
print()
print('What is the cost for every sq yrd?')
cost = float(input())

totalSQ = width * length
totalYRD = totalSQ / 9
totalCost = totalYRD * cost


print()
print('The total amount of carpet in sq ft is ' + str(totalSQ))
print()
print('The total amount of carpet in sq yrds is ' + str(totalYRD))
print()
print('The total cost for the carpet is ' + str(totalCost))

#exit scheme
a = input()
if a == "":
    exit()
else:
    def exitt():
        exit()
    exitt()
    

