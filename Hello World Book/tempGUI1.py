#tempgui1.py
#EasyGui version of temperature-converter program
#converts Fahrenheit to Celcius
import easygui

rootMenu = easygui.msgbox('''Welcome to the EasyGui
version of the program 'tempConverter'.''', title = 'GUI ver. of tempConverter', ok_button = 'Continue')
F1 = easygui.integerbox('What is your temperature in Fahrenheit?', title = 'Fahrenheit Temperature', default = '0', lowerbound = 0, upperbound = 300)
F = float(F1)
C = 5/9*(F - 32)
answer = easygui.msgbox('Your temperature in celcius is %7.2f' % C, title = 'Answer')

