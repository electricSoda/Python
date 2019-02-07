# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:31:18 2019

@author: Justin Ge
"""



#timer for eyes
import time
from tkinter import *

################################################
#window
root = Tk()

root.attributes('-fullscreen', True)

#set the color OPTIONAL
#root.config(bg='white')


#set title
root.title("G. Timer")

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
#initial code

#onoff variable
onoff = IntVar()
checked = True


#define the end function
def end():
    root.attributes('-fullscreen', True)
    le = Label(root, text='Timer End!', font = 'Times 20 bold', bg='yellow', fg='red').pack()
    starts.config(state=DISABLED)
    time.sleep(5)
    print('test')
    #exit the computer

#define the time function
def time1():
    seconds = int(got) * 60
    sc = True
    scc = 0
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



aof = Label(topFrame, text = 'Amount of time', font = 'Helvetica 20')
aof.pack()

set1 = Listbox(topFrame)
mytime = ['1', '3', '5', '8', '10', '13', '15', '18', '20', '21', '22', 
          '23', '24', '25', '26', '27', '28', '30', '31', '35', '40', '45',
          '48', '50', '55', '60']
for i in range(1,27):
    set1.insert(i, mytime[i-1])
set1.pack()

starts = Button(root, text = 'Start Timer', bg = 'white', fg = 'black', font = 'Helevetica', command = start)
starts.config(height = 2, width = 9)
starts.pack()


def callback():
    pass







#mainloop
root.mainloop()