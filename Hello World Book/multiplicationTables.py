print('Which multiplication table would you like?')
number = int(input())
print('How high do you want to go?')
limit = int(input())
limit = limit + 1
print("Here's your table:")

for i in range(1, limit):
      print(number, 'x', i,'=', number*i)
