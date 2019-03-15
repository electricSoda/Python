#TextPad


#import modules needed
import os
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
    root.destroy()

#save function
def save():
    got = text.get('1.0', END)
    saveDir = simpledialog.askstring('Save Directory', 'Directory:')
    name = simpledialog.askstring('File Name', 'File Name (excluding .txt, .pdf etc.):')
    try:
        os.chdir(saveDir)
        with open(name + '.txt', 'w+') as doc:
            doc.write(got)
    except:
        messagebox.showerror('Error', 'Error: Invalid information.')


# **** Menus **** #
menu = Menu(root)
root.config(menu = menu)

fileMenu = Menu(menu)
menu.add_cascade(label='File', menu = fileMenu)
fileMenu.add_command(label='New File')
fileMenu.add_command(label='New...')
fileMenu.add_command(label='Open File...')
fileMenu.add_command(label='Reopen File')
fileMenu.add_separator()
fileMenu.add_command(label='Save', command = save)
fileMenu.add_separator()
fileMenu.add_command(label='Open Toolbar')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command = terminate)


editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu = editMenu)
editMenu.add_command(label='Undo')
editMenu.add_command(label='Redo')
editMenu.add_separator()
editMenu.add_command(label='Cut')
editMenu.add_command(label='Copy')
editMenu.add_command(label='Paste')
editMenu.add_command(label='Paste Without Reformatting')
editMenu.add_command(label='Select All')


viewMenu = Menu(menu)
menu.add_cascade(label='View', menu = viewMenu)

winMenu = Menu(menu)
menu.add_cascade(label='Window', menu = winMenu)

optionMenu = Menu(menu)
menu.add_cascade(label='Options', menu = optionMenu)

helpMenu = Menu(menu)
menu.add_cascade(label='Help', menu = helpMenu)

# **** **** #


# **** Toolbar **** #
toolbar = Frame(root, bg='orange')

insertBtn = Button(toolbar, text = "Insert")
insertBtn.pack(side = TOP, padx = 2, pady = 2)

printBtn = Button(toolbar, text = "Print")
printBtn.pack(side = TOP, padx = 2, pady = 2)

saveBtn = Button(toolbar, text = 'Save', command = save)
saveBtn.pack(side = TOP, padx = 2, pady = 2)


toolbar.pack(side = LEFT, fill = Y)

# **** **** #



#text space
text = Text(root, width = w, height = h)
text.pack()






#set the mainloop
root.mainloop()
