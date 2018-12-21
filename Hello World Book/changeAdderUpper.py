import time

print('Change adder-upper')
time.sleep(0.2)
print()
print()
print('How many quarters?')
q = float(input())
print()
print()
print('How many dimes?')
d = float(input())
print()
print()
print('How many nickels?')
n = float(input())
print()
print()
print('How many pennies?')
p = float(input())

qAmount = q * 0.25
dAmount = d * 0.10
nAmount = n * 0.05
pAmount = p * 0.01
total = qAmount + dAmount + nAmount + pAmount

time.sleep(1)
print()
print()
print('Your total amount of the change is $' + str(total))

#exit scheme
a = input()
if a == "":
    exit()
else:
    def exitt():
        exit()
    exitt()
