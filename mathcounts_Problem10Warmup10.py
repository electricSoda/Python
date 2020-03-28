#Problem 10:
#A bin has 2 white balls and 3 black balls. You play a game as follows:
#you draw balls at random out of the bin, one at a time,
#withour replacement. Every time you draw a white ball, you win a dollar,
#but every time you draw a black ball, you lose a dollar.
#This looks bad for you, since there are more black balls than white balls.
#But you are allowed to stop the game at any time.
#Devise a strategy for playing this game which results in an expected profit

import random

money = []
tick = 0

def randomNum1():
    global num1, color1
    num1 = random.randint(1,5) #2 white, 3 black
    color1 = random.randint(1,2) #1 is white, and 2 is black

def randomNum2():
    global num2, color2
    num2 = random.randint(1,4) # 2 black, 2 white
    color2 = random.randint(1,2)

def randomNum3():
    global num3, color3
    num3 = random.randint(1,3)
    color3 = random.randint(1,2)

def stop():
    global tick
    combine1 = '$' + str(money[tick])
    print(str(num1), str(color1), combine1)
    tick = 0

def stop1():
    global tick
    combine2 = '$' + str(money[tick])
    print(str(num2), str(color2), combine2)
    tick = 0

def stop2():
    global tick
    combine3 = '$' + str(money[tick])
    print(str(num3), str(color3), combine3)
    tick = 0

def formula():
    global tick
    tick = 0
    randomNum1()
    if color1 == 1: #white
        money.append(int(1))
        stop()
    elif color1 == 2: #black
        randomNum2()
        print(color2, num2)
        if color2 == 1 and num2 <= 2: #white
            money.append(int(0))
            tick = tick + 1
            stop1()
        else: #black
            randomNum3() #1 black and 2 white
            if color3 == 1 and num3 >=2:
                money.append(int(0))
                tick = tick + 1
                stop2()
            else:
                print('quick maths')
    else:
        print('There was an error.')

for i in range(0, 10):
    formula()
