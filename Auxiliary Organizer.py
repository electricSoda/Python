# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 18:48:17 2019

@author: Auxiliary Technologies
"""

## Auxiliary Company Organizer


##########################################
#get the needed libraries and wheels, etc.
import os
#####
#kivy imports
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
#####

##########################################

#initial code

#set default directory
os.chdir('C:\\teleport\\Code\\Python')

class LoginWindow(Screen):
    def trun(self):
        with open('trun', 'w') as tru1:
            tru1.write('True')
            tru1.close()

class NavigatorWindow(Screen):
    def btn(self):
        show_popup()


class WindowManager(ScreenManager):
    pass

class P(FloatLayout):
    pass

kv = Builder.load_file('auxiliary.kv')

#main class

class Auxiliary(App):
    def build(self):
        return kv


def show_popup():
    show = P()

    popupWindow = Popup(title="Error", content = show, size_hint=(None, None), size = (400, 400))

    popupWindow.open()





if __name__ == '__main__':
    Auxiliary().run()
