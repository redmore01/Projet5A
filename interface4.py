
import kivy
kivy.require('1.0.5')
import os
import sys
from kivy.app import App
from kivy.uix.image import Image
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
from kivy.uix.video import Video

 

class Catalog(Screen):
    
    
    lastscreen = ObjectProperty()
  
    def __init__(self, **kwargs):
        self._previously_parsed_text = ''
        super(Catalog, self).__init__(**kwargs)
  
        self.carousel = None
		
    def on_enter(self):
        self.listim = self.manager.list1
        # self.grid = self.manager.gridtest
        x = self.manager.x
        print(x)
		
            
        if x <= 2:
            gridscreen = GridLayout(cols = x)
            for y in self.listim:
	
                newimage= y+'.mp4'
                gridscreen.add_widget(Video(source=newimage))
        else:
            gridscreen = GridLayout(rows = x-2)
            for y in self.listim:

                newimage= y+'.mp4'
                gridscreen.add_widget(Video(source=newimage))

        lastscreen = self.manager.get_screen('interface4').lastscreen
        lastscreen.clear_widgets()
        
        lastscreen.add_widget(gridscreen)
		
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'interface3'
        self.manager.get_screen('interface3')

class Interface4App(App):
    '''The kivy App that runs the main root. All we do is build a catalog
    widget into the root.'''

    def build(self):
        screen = Catalog()
        screen.name = 'interface4'
        return screen
    def on_pause(self):
        return True


if __name__ == "__main__":
    Interface4App().run()