print('Which multiplication table would you like?')
number = int(input())
print('How high do you want to go?')
limit = int(input())
print("Here's your table:")
i = 1
while i <= limit:
      print(number, 'x', i,'=', number*i)
      i = i + 1
