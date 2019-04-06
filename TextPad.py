#TextPad


#import modules needed
import os
import time
import webbrowser
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


#################
#window

#root
root = Tk()

#setting width and height
w = 800
h = 600

#set the color
root.config(bg='white')

#get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#set title
root.title("TextPad")
#################



#initial code

#terminate function
def terminate():
    try:
        root.destroy()
    except Exception as a1:
        messagebox.showerror('Error', 'Error: Items Missing.')
        print(a1)

#save function
def save():
    got = text.get('1.0', END)
    saveDir = simpledialog.askstring('Save Directory', 'Directory:')
    name = simpledialog.askstring('File Name', 'File Name (excluding .txt, .pdf etc.):')
    try:
        os.chdir(saveDir)
        with open(name + '.txt', 'w+') as doc:
            doc.write(got)
    except Exception as e:
        messagebox.showerror('Error', 'Error: Invalid information.')
        print(e)

#print1 function
def print1():
    dir1 = simpledialog.askstring('Print Directory', 'Directory:')
    file = simpledialog.askstring('File Name', 'File Name (including .txt, pdf etc.):')

    try:
        os.chdir(dir1)
        os.startfile(file, 'print')
        root.messagebox.showinfo('Printing', 'Printing...')
        time.sleep(2)
    except Exception as ex:
        messagebox.showerror('Error', 'Error: Invalid information.')
        print(ex)

#hub function
def hub():
    global hub1
    hub1 = Tk()

    #setting width and height
    w1 = 200
    h1 = 100

    #set the color
    hub1.config(bg='white')

    #title of hub1
    hub1.title('Insert')

    #nononononono
    hub1.resizable(width = False, height=False)


    #get screen width and height
    ws1 = hub1.winfo_screenwidth()
    hs1 = hub1.winfo_screenheight()

    # calculate x and y coordinates for the Tk root window
    x1 = (ws1/2) - (w1/2)
    y1 = (hs1/2) - (h1/2)

    # set the dimensions of the screen and where it is placed
    hub1.geometry('%dx%d+%d+%d' % (w1, h1, x1, y1))

    insertTIME = Button(hub1, text='Insert Time', command = inserttime)
    insertTIME.pack()

    insertSEP = Button(hub1, text='Insert Separator', command = insertsep)
    insertSEP.pack()

    back = Button(hub1, text='Back', command=terminate1)
    back.pack()


#open function
def open1():
    dir3 = simpledialog.askstring('Directory', 'Directory:')
    file2 = simpledialog.askstring('File Name', "File Name (Including .txt, .pdf etc):")

    try:
        os.chdir(dir3)
        with open(file2) as op:
            theFile = op.read()
            text.insert(INSERT, theFile)
    except Exception as oooo:
        messagebox.showerror('Error', 'Error: Invalid File.')
        print(oooo)

#terminate1 function
def terminate1():
    try:
        hub1.destroy()
    except Exception as a2:
        messagebox.showerror('Error', 'Error: Items Missing.')
        print(a2)

#new function
def new():
    dir2 = simpledialog.askstring('Directory', 'Directory:')
    file1 = simpledialog.askstring('File Name', "New File's Name (including .txt, .pdf etc.):")

    try:
        os.chdir(dir2)
        with open(file1, 'w+') as nwn:
            pass

    except Exception as oof:
        messagebox.showerror('Error', 'Error: Failed to create new file.')
        print(oof)

#inserttime function
def inserttime():
    currentTime = time.asctime()
    text.insert(INSERT, currentTime + ' ')

#insertsep function
def insertsep():
    text.insert(INSERT, '\n' + '______________________________________________________________________________________________' )

#undo funcion
def undo():
    text.edit_undo()

#redo function
def redo():
    text.edit_redo()
###
#to be cleared after testing
def source():
    url = 'http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/text-methods.html'
    a = webbrowser.open_new(url)
    url1 = 'https://www.youtube.com/watch?v=iUmqLGUktek'
    b = webbrowser.open_new(url1)

###

# **** Menus **** #
menu = Menu(root)
root.config(menu = menu)

fileMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label='File', underline = 0, menu = fileMenu)
fileMenu.add_command(label='New File', command=new)
fileMenu.add_command(label='Open File...', command = open1)
fileMenu.add_separator()
fileMenu.add_command(label='Save', accelerator = 'Ctrl+S', command = save)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command = terminate)


editMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label='Edit', underline = 0, menu = editMenu)
editMenu.add_command(label='Undo', accelerator = 'Ctrl+Z', command = undo)
editMenu.add_command(label='Redo', accelerator = 'Ctrl+Shift+Z', command = redo)
editMenu.add_separator()
insertMenu = Menu(editMenu, tearoff = 0)
insertMenu.add_command(label='Insert Time', command=inserttime)
insertMenu.add_command(label='Insert Separator', command=insertsep)
editMenu.add_cascade(label = 'Insert', menu = insertMenu)


viewMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label='View', underline = 0, menu = viewMenu)

optionMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label='Options', underline = 0, menu = optionMenu)

helpMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label='Help', underline = 0, menu = helpMenu)


###
#to be cleared after testing
developerMenu = Menu(menu, tearoff = 0)
menu.add_cascade(label='DevMenu', underline = 0, menu = developerMenu)
developerMenu.add_command(label='Sources', command=source)

###

# **** **** #


# **** Toolbar **** #
toolbar = Frame(root, bg='orange')

insertBtn = Button(toolbar, text = 'Insert', command = hub)
insertBtn.pack(side = TOP, padx = 2, pady = 2)

printBtn = Button(toolbar, text = "Print", command = print1)
printBtn.pack(side = TOP, padx = 2, pady = 2)

saveBtn = Button(toolbar, text = 'Save', command = save)
saveBtn.pack(side = TOP, padx = 2, pady = 2)


toolbar.pack(side = LEFT, fill = Y)

# **** **** #



#text space
text = Text(root, width = w, height = h, undo = True)
text.pack()






#set the mainloop
root.mainloop()
