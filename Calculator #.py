import time
import os

os.system("title Calculator #")
print('                                            ')
print('Welcome to Calculator #')
print('                                            ')
time.sleep(1)
	
def space():
	print('                                                                 '*5)

space()

def Calculator():
        os.system("cls")
        operation = input('What is your operation? (*, +, /, -) >> ')
        space()	
        if operation == '*':
                times = int(input('What is your first number?>> '))
                space()
                times2 = int(input('What is your second number?>> '))
                print('Answer:' + str(times*times2))
        if operation == '+':
                add = int(input('What is your first number?>> '))
                space()		
                add2 = int(input('What is your second number?>> '))
                print('Answer:' + str(add+add2))
        if operation == '/':
                div = int(input('What is your first number?>> '))
                space()		
                div2 = int(input('What is your second number?>> '))
                print('Answer:' + str(div/div2))
        if operation == '-':
                minus = int(input('What is your first number?>> '))
                space()		
                minus2 = int(input('What is your second number?>> '))
                print('Answer:' + str(minus-minus2))
        space()
        time.sleep(1.6)
        space()	
        con = input('Continue? |[y]|  |[n]| :   ')
        if con == 'y':
                pass
        if con == 'n':
                space()
                exit()
        space()

while True:
	Calculator()
