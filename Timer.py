#timer for eyes
import time
import tkinter
from tkinter import *

################################################
#window
root = Tk()

#setting width and height
w = 620
h = 650

#set the color OPTIONAL
#root.config(bg='white')

global ws, hs
#get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

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

#time variable
time = StringVar()


#onoff variable
onoff = IntVar()
checked = True


#define the time function
def time1():
    global ja, ja1, mt, ht, amount, sc, scds
    ja = text.get()
    ja1 = text1.get()
    mt = ja * 60
    ht = ja1 * 3600
    amount = mt + ht
    scds = True
    sc = 0


def ok():
    print('done')


##########################
#change the 'if ja or ja1 => 1:' 
#    while scds:
#    if ja or ja1 => 1:
#        sc = sc + 1
#        print(sc)
#        time.sleep(1)
#        if sc == amount:
#            print('IT WORKED!!!')
#            break
#            return
#    else:
#        oof = Label(root, text = "ERROR, CANNOT COMPREHEND '0'")
#        oof.config(fg = 'red')
#        oof.pack()
##########################


log = True
errors = True

#define the start function
def start():
    global log, errors, got

    if log:
        logging = Label(root, text = 'Logging Outcome:', font = 'Helvetica')
        logging.config(fg = 'black', bg = 'white')
        logging.pack()
        log = False
    try:
        got = time.get()
    except:
        if errors:
            error = Label(root, text = "ERROR, EMPTY VALUE IN 'TIME'")
            error.config(fg = 'red')
            error.pack()
            errors = False
    

    time1()



aof = Label(topFrame, text = 'Amount of time', font = 'Helvetica')
aof.pack()

spinbox1 = Spinbox(topFrame, from_=0, to=60,state=NORMAL).pack()

set1 = Listbox(topFrame)
set1.insert(1, '1')
set1.insert(2, '3')
set1.insert(3, '5')
set1.insert(4, '8')
set1.insert(5, '10')
set1.insert(6, '13')
set1.insert(7, '15')
set1.insert(8, '18')
set1.insert(9, '20')
set1.insert(10, '21')
set1.insert(11, '22')
set1.insert(12, '23')
set1.insert(13, '24')
set1.insert(14, '25')
set1.insert(15, '26')
set1.insert(16, '27')
set1.insert(17, '28')
set1.insert(18, '30')
set1.insert(19, '31')
set1.insert(20, '35')
set1.insert(21, '40')
set1.insert(22, '45')
set1.insert(23, '48')
set1.insert(24, '50')
set1.insert(25, '55')
set1.insert(26, '60')
set1.pack()

starts = Button(root, text = 'Start Timer', bg = 'white', fg = 'black', font = 'Helevetica', command = start)
starts.config(height = 2, width = 9)
starts.pack()













#mainloop
root.mainloop()