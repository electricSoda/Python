import time

#How long will it take to go somewhere in a car
print('''The distance from the "place" is (in km and the format is a int)''')
dis = int(input('>>>'))
time.sleep(0.5)
print('''The average speed for the travel is (in km and the format is a int)''')
speed =int(input('>>>'))
time.sleep(0.5)
time123 = dis/speed
print("The time to travel from the distance%4dkm at the speed of%4dkm is: %4.2f" % (dis, speed, time123))
time.sleep(4)
