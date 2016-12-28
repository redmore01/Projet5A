
import kivy
kivy.require('1.0.5')
import os
import sys
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.graphics import Color, Ellipse, Rectangle, RoundedRectangle
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter

# from interface1 import Interface1App

class ScatterWithImage(Scatter):
    src = StringProperty("softboy.png")

class Catalog(Screen):
    
    list = ['']
    screen = ObjectProperty(None)
  
    def __init__(self, **kwargs):
        self._previously_parsed_text = ''
        super(Catalog, self).__init__(**kwargs)

        self.carousel = None


    # def new_changes(self):
    
	
    def on_enter(self):
        self.listim = self.manager.list1
        # self.grid = self.manager.gridtest
        x = self.manager.x
        print(x)
		
            
        if x <= 2:
            gridscreen = GridLayout(cols = x)
            for y in self.listim:
	
                newimage= y+'.png'
                gridscreen.add_widget(ScatterWithImage(src=newimage))
        else:
            gridscreen = GridLayout(rows = x-2)
            for y in self.listim:

                newimage= y+'.png'
                gridscreen.add_widget(ScatterWithImage(src=newimage))

        screen = self.manager.get_screen('interface2').screen
        screen.clear_widgets()
      
        screen.add_widget(gridscreen)
        # self.manager.list1 = self.listim
        # self.manager.x = self.x
		
		
	
    def change_screen(self): 
		

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'interface4'
        self.manager.get_screen('interface4')
        self.manager.list1 = self.listim
        self.manager.x = self.x
		
		
		
    def backtointerface1(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'interface2'
        self.manager.get_screen('interface2')

class Interface3App(App):
    '''The kivy App that runs the main root. All we do is build a catalog
    widget into the root.'''

    def build(self):
        screen = Catalog()
        screen.name = 'interface3'
        return screen
    def on_pause(self):
        return True


if __name__ == "__main__":
    Interface3App().run()
