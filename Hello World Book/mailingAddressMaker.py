#mailing address maker
import easygui

msgstrt = easygui.msgbox('''This is a little program
that allows you to create a
address for the mailers''', title = 'Mailing address maker', ok_button = 'Continue')

name = easygui.enterbox('Name (First and Last):', title = 'Name')

housenum = easygui.integerbox('House number:', title = 'House Number', default = 0, lowerbound = 0, upperbound = 10000)

street = easygui.enterbox('Street:', title = 'Street')

city = easygui.enterbox('City:', title = 'City')

pts = easygui.enterbox("Province/Territory/State:", title = 'Province/Territory/State')

myzip = easygui.integerbox('Zip code/Postal:', title = 'Zip code/Postal', default = 0, lowerbound = 0, upperbound = 10000000)

housenum1 = str(housenum)

address = easygui.msgbox('' + name + '''
''' + housenum1 + ' ' + street + '''
''' + city + ', ' + pts + '''
''' + str(myzip), title = 'Final Address', ok_button = 'Close')


