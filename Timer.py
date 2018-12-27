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
time = IntVar()


#onoff variable
onoff = IntVar()
checked = True


#define the time function
def time1():
    global ja, sc, scds
    ja = time.get()
    print(ja)
    scds = True
    sc = 0


log = True
errors = True


#define the start function
def start():
    global log, got

    if log:
        logging = Label(root, text = 'Logging Outcome:', font = 'Helvetica')
        logging.config(fg = 'black', bg = 'white')
        logging.pack()
        log = False
    got = time.get()

        
    

    time1()



aof = Label(topFrame, text = 'Amount of time', font = 'Helvetica')
aof.pack()

spinbox1 = Spinbox(topFrame, from_=0, to=60,state=NORMAL, wrap =- True).pack()

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













#mainloop
root.mainloop()