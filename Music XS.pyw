#Music XS
#import the modules needed
import webbrowser
import sys
import time
import tkinter
from tkinter import *
#from PIL import ImageTk, Image
import os

################################################
#window
root = Tk()

#setting width and height
w = 500
h = 500

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
root.title("Music XS")

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
#text
text = StringVar()

#cls function
def cls():
      query.delete(0, END)

#rvm function
def rvm():
      query.destroy()
      clear.destroy()
      rmvbtn.destroy()

#create the function exit
def exitTK():
      exit()

#create the function ok
def ok(event):
      output = text.get()
      webbrowser.open_new_tab('https://youtube.com/results?search_query=music %s' % output)
      return
      
#create the function searchmusic
def searchmusic():
      #global variables
      global query, rmvbtn, clear

      try:
        ifq = query.winfo_exists()
      except NameError:
        pass
      else:
        if ifq: return

      #query
      query = Entry(root, textvariable = text)
      query.pack()
      #config rmvbtn button
      rmvbtn = Button(root, text='^', command = rvm)
      rmvbtn.config(font=('Comic Sans', 10, 'bold'))
      rmvbtn.config(height = 0, width = 2)
      rmvbtn.pack()
      #config clear button
      clear = Button(root, text='Clear', command = cls)
      clear.config(bg='red', fg='gray1')
      clear.config(font=('Comic Sans', 10, 'bold'))
      clear.config(height = 1, width = 5)
      clear.pack()
      query.bind("<Return>", ok)

#define Help
def Help():
      #global variables
      global tk
      
      exit1()
      tk = Tk()
      #frame(s)
      bottomFRM = Frame(tk)
      bottomFRM.pack(side=BOTTOM)
      
      #*COPIED FROM THE START(again)*
      #setting width and height
      w = 250
      h = 250

      #get screen width and height
      ws = root.winfo_screenwidth()
      hs = root.winfo_screenheight()

      # calculate x and y coordinates for the Tk root window
      x = (ws/2) - (w/2)
      y = (hs/2) - (h/2)

      # set the dimensions of the screen and where it is placed
      tk.geometry('%dx%d+%d+%d' % (w, h, x, y))

      #title
      tk.title('Help')

      btn1 = Button(tk, text='Contact and Suggestions')
      btn1.config(bg='grey40', fg='black')
      btn1.pack()

      btn2 = Button(bottomFRM, text='Back', command = exit2)
      btn2.config(bg='dark slate blue', fg='light slate blue')
      btn2.config(height = 1, width = 4)
      btn2.pack()

#op function
def op():
      #new custom window just for options
      global win
      win = Tk()

      #*COPIED FROM THE START*
      #setting width and height
      w = 250
      h = 250

      #get screen width and height
      ws = root.winfo_screenwidth()
      hs = root.winfo_screenheight()

      # calculate x and y coordinates for the Tk root window
      x = (ws/2) - (w/2)
      y = (hs/2) - (h/2)

      # set the dimensions of the screen and where it is placed
      win.geometry('%dx%d+%d+%d' % (w, h, x, y))

      #title
      win.title('Options')

      #bg color
      win.config(bg='white')

      #create the menu
      menu = Menu(win)
      win.config(menu=menu)

      #aMenu
      aMenu = Menu(menu)
      menu.add_cascade(label = 'File', menu=aMenu)
      aMenu.add_command(label = 'History', command = hist)
      aMenu.add_command(label = 'Help', command=Help)
      aMenu.add_separator()
      aMenu.add_command(label = 'Back', command=exit1)

      #bMenu
      bMenu = Menu(menu)
      menu.add_cascade(label = 'About', menu = bMenu)
      bMenu.add_command(label = 'Blank', command = None)

      #cMenu
      cMenu = Menu(menu)
      menu.add_cascade(label = 'Others', menu = cMenu)
      cMenu.add_command(label = 'Easter Eggs', command = easter)

#hist function
def hist():
      #first delete ther win gui
      win.destroy()
      
      #new gui
      global nw
      nw = Tk()

      #*COPIED FROM THE START* (again and again)
      #setting width and height
      w = 250
      h = 250

      #get screen width and height
      ws = root.winfo_screenwidth()
      hs = root.winfo_screenheight()

      # calculate x and y coordinates for the Tk root window
      x = (ws/2) - (w/2)
      y = (hs/2) - (h/2)

      # set the dimensions of the screen and where it is placed
      nw.geometry('%dx%d+%d+%d' % (w, h, x, y))

      #title
      nw.title('History')
      
      #create the list of history
      slider = Scale(nw, from_ = 0, to = 10)
      slider.pack()

      #work in progrerss label
      wrk = Label(nw, text='A work in progress')
      wrk.pack()

#easter function
def easter():
      #global variables
      global js, rainbowToggle, check
      
      win.destroy()
      js = Tk()

      #*COPIED FROM THE START* (again and again and again i should stop writing this)
      #setting width and height
      w = 250
      h = 250

      #get screen width and height
      ws = root.winfo_screenwidth()
      hs = root.winfo_screenheight()

      # calculate x and y coordinates for the Tk root window
      x = (ws/2) - (w/2)
      y = (hs/2) - (h/2)

      # set the dimensions of the screen and where it is placed
      js.geometry('%dx%d+%d+%d' % (w, h, x, y))

      #title
      js.title('Easter Eggs')

      #bg color
      js.config(bg = 'white')
      
      #rainbow
      check = IntVar()
      rainbowToggle = Checkbutton(js, text = 'Rainbow Main Screen', state = ACTIVE, variable = check, command = rainbow)
      rainbowToggle.pack()

#rainbow function
def rainbow():
      #while True:
      root.config(bg = 'red')
      time.sleep(1)
      root.config(bg = 'orange')
      time.sleep(1)


#define orange
def orange():
      root.config(bg = 'orange')
      time.sleep(1)

#define orange
def yellow():
      root.config(bg = 'yellow')
      time.sleep(1)

#define orange
def green():
      root.config(bg = 'green')
      time.sleep(1)

#define orange
def blue():
      root.config(bg = 'blue')
      time.sleep(1)

#define orange
def indigo():
      root.config(bg = 'indigo')
      time.sleep(1)

#define orange
def violet():
      root.config(bg = 'violet')
      time.sleep(1)

#exit2 function
def exit2():
      tk.destroy()

#exit1 function
def exit1():
      win.destroy()     

#not needed until polishing product
#add background image
#img = ImageTk.PhotoImage(Image.open("back.jpg"))
#panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes") 
      
#define the exit button
exitbtn = Button(bottomFrame, text='Exit', command = exitTK)
exitbtn.config(bg='grey', fg='white')
exitbtn.config(font=('Comic Sans', 15, 'bold'))
exitbtn.config(height = 0, width = 5)
exitbtn.pack()

#define the search button
search = Button(topFrame, text='Search', command = searchmusic)
search.config(bg='blue', fg='light blue')
search.config(font=('Comic Sans', 17, 'bold'))
search.config(height = 1, width = 5)
search.pack()

#define the options button
options = Button(bottomFrame, text='Options', command = op)
options.config(bg='black', fg='white')
options.config(font=('Verdana', 10, 'bold'))
options.config(height = 1, width = 6)
options.pack()



















#set mainloop
root.mainloop()



