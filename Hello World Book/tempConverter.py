import time

#Converting Fahrenheit to Celcius
print('What is your temperature in Fahrenheit? (Integer and Floats only)')
F = float(input('>>>'))
C = 5/9*(F - 32)
print('Your temperature in Celcius is: %7.2f' % C)
time.sleep(4)
