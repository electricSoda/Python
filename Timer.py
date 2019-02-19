# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:31:18 2019

@author: Justin Ge
"""



#timer for eyes

#import the libraries
import os
import time
import random
from tkinter import *



#########################################
#initial code

#root

#root
root = Tk()

#onoff variable
onoff = IntVar()
checked = True



#different messages
messages = ['You were never created to live depressed, defeated, guilty, condemned, ashamed or unworthy. You were create to be victorious.',
            'It’s gonna get harder before it gets easier. But it will get better, you just gotta make it through the hard stuff first', 
            'Recovery is something that you have to work on every single day and it’s something that doesn’t get a day off', 
            'If you find yourself in a hole, the first thing to do is stop digging', 
            'There is no shame in beginning again, for you get a chance to build bigger and better than before', 
            'Recovery is about progression not perfection', 
            'I’m not telling you it is going to be easy, I’m telling you it’s going to be worth it', 
            'It does not matter how slowly you go as long as you do not stop']

listnumber = random.randint(0, 7)



#exit function
def exit1():
    os.system("shutdown /p")



#define the end function
def end():
    root.overrideredirect(False)
    root.attributes('-fullscreen', True)
    le = Label(root, text='Timer End!', font = 'Times 20 bold', bg='yellow', fg='red').pack()
    starts.config(state=DISABLED)
    time.sleep(10)
    #exit the computer
    exit1()

#define the time function
def time1():
    
    #Not a chance!
    root.overrideredirect(True)
    
    seconds = int(got) * 60
    seconds1 = seconds + 1
    for x in range(1, seconds1):
        time.sleep(1)
        print(x)
    end()
    


log = True


#define the start function
def start():
    global log, got

    if log:
        logging = Label(root, text = 'Logging Outcome:', font = 'Helvetica')
        logging.config(fg = 'black', bg = 'white')
        logging.pack()
        log = False   
    
    got = set1.get(set1.curselection())
    
    if got:
        root.attributes('-fullscreen', False)
        root.protocol("WM_DELETE_WINDOW", callback)
        
    

    time1()



def callback():
    pass


def mainGUI():      
    global set1, starts
    ################################################
    #window
    
    root.attributes('-fullscreen', True)
    
    #bg
    root.config(bg='white')
    
    
    #set title
    root.title("Flow Timer")
    
    #frames
    leftFrame = Frame(root)
    leftFrame.pack(side=LEFT)
    
    rightFrame = Frame(root)
    rightFrame.pack(side=RIGHT)
    
    topFrame = Frame(root)
    topFrame.pack(side=TOP)
    
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    
    ################################################
    
    
    
    quote = Label(topFrame, text = 'Quote of the day:', font = 'Helvetica 14 bold')
    quote.config(fg='red', bg='light green')
    quote.pack()
    
    
    qq = messages[listnumber]
    
    quote1 = Label(topFrame, text = qq, font='MSSerif 18 bold')
    quote1.pack()
    
        
    aof = Label(topFrame, text = 'Amount of time', font = 'Helvetica 20')
    aof.pack()
    
    
    set1 = Listbox(topFrame)
    mytime = ['1', '3', '5', '8', '10', '13', '15', '18', '20', '21', '22', 
              '23', '24', '25', '26', '27', '28', '30', '31', '35']
    
    for i in range(1,21):
        set1.insert(i, mytime[i-1])
    set1.pack()
    
    starts = Button(root, text = 'Start Timer', bg = 'white', fg = 'black', font = 'Helevetica', command = start)
    starts.config(height = 2, width = 9)
    starts.pack()

#passCor function
def passCor():
    os.unlink('flow_TimerCount.txt')




#blankScreen function
def blankScreen():
    global entered
        
    #window
    blank = Tk()
    
    #bottom Frame
    bottmFrame = Frame(blank)
    bottmFrame.pack(side=BOTTOM)

    
    #fullscreen
    blank.attributes('-fullscreen', True)
    
    #title
    blank.title('Flow Timer')
    
    #bg
    blank.config(bg='white')    
    
    entered = Entry(blank)
    
    entered.pack()
    
    sub = Button(blank, text='Submit', command = pressEvent)
    sub.pack()
    
    shutDown = Button(bottmFrame, text='Shut Down', command = exit1)
    shutDown.pack()
    
    

def pressEvent():
    got1 = entered.get()
    if got1 == 'prg0p':
        passCor()
    else:
        pass


#check if flow_CountTimer.txt exists
checked = os.path.isfile('flow_TimerCount.txt')

#check if the user has used the computer for more than 5 or 6 consecutive times
if not checked:
    with open("flow_TimerCount.txt","w+") as flow:
        flow.write('1' + '\n')
        mainGUI()
else:    
    print('File Exists: flow_TimerCount.txt')
    with open('flow_TimerCount.txt') as flow1:
        tied = flow1.read()
        numOfChars = len(tied.split())
        print('Characters:')
        print(numOfChars)
        print()
        app = int(numOfChars)
    with open('flow_TimerCount.txt', 'a') as flow2:
        if app == 1:
            flow2.write('2' + '\n')
            mainGUI()
        else:
            pass
    with open('flow_TimerCount.txt', 'a') as flow3:
        if app == 2:
            flow3.write('3' + '\n')
            mainGUI()
        else:
            pass
    with open('flow_TimerCount.txt', 'a') as flow4:
        if app == 3:
            flow4.write('4' + '\n')
            mainGUI()
    with open('flow_TimerCount.txt', 'a') as flow5:
        if app == 4:
            flow5.write('5' + '\n')
            mainGUI()
        else:
            pass
    with open('flow_TimerCount.txt', 'a') as flow6:
        if app == 5:
            flow6.write('6' + '\n')
            mainGUI()
        else:
            pass 
    with open('flow_TimerCount.txt', 'a') as flow7:
        if app == 6:
            blankScreen()                     
        else:
            pass
    




#mainloop
root.mainloop()