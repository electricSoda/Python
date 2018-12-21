tnkSize = float(input('Size of tank in liters: '))
pctfll = float(input('Percent full(about): '))
mileage = float(input('km per liter(about): '))

range1 = (tnkSize - 5) * (pctfll / 100.0) * mileage
range0 = str(range1)
print('You can go another ' + range0 + " km.")
print('The next gas station is 200 km away')
if range1 >= 200:
      print('You can wait for the next gas station.')
else:
      print('Get gas now!')
