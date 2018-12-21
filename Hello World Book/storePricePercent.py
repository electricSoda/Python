import time

print('What is the purchase price?')
price = float(input())

if price <= 10:
      print('You get 10% discount')
      discount = 0.1 * price
      price1 = price - discount
      print('Your purchase amount after the discount is ' + str())
else:
      print('You get 20% discount')
      discount1 = 0.2 * price
      price2 = price - discount1
      print('Your purchase amount after the discount is ' + str(price2))
