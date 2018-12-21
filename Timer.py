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

#text variable
text = IntVar()

#text1 variable
text1 = IntVar()

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
errors1 = True

#define the start function
def start():
    global log, errors1, errors, got, got1

    if log:
        logging = Label(root, text = 'Logging Outcome:', font = 'Helvetica')
        logging.config(fg = 'black', bg = 'white')
        logging.pack()
        log = False
    try:
        got = text.get()
    except:
        if errors:
            error = Label(root, text = "ERROR, EMPTY VALUE IN 'MINUTES'")
            error.config(fg = 'red')
            error.pack()
            errors = False
    try:
        got1 = text1.get()
    except:
        if errors1:
            error1 = Label(root, text = "ERROR, EMPTY VALUE IN 'HOURS'")
            error1.config(fg = 'red')
            error1.pack()
            errors1 = False

    time1()



label = Label(topFrame, text = 'How much minutes?', font = 'Helvetica')
timer = Entry(topFrame, width = 20, textvariable = text)
timer.config(bg = 'orange')
label.pack()
timer.pack()
hours = Label(topFrame, text = 'How much hours?', font = 'Helvetica')
timer1 = Entry(topFrame, width = 20, textvariable = text1)
timer1.config(bg = 'red')
hours.pack()
timer1.pack()

starts = Button(root, text = 'Start Timer', bg = 'white', fg = 'black', font = 'Helevetica', command = start)
starts.config(height = 2, width = 9)
starts.pack()
starts.bind("<Return>", ok)













#mainloop
root.mainloop()