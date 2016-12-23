
import kivy
kivy.require('1.4.2')
import os
import sys
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.graphics import Color, Ellipse, Rectangle, RoundedRectangle
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

 

class Catalog(Screen):
    
    
    screen = ObjectProperty()
  
    def __init__(self, **kwargs):
        self._previously_parsed_text = ''
        super(Catalog, self).__init__(**kwargs)
  
        self.carousel = None
    
    def change_color(self, source):
        Color(*BLEU)
		
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'interface1'
        self.manager.get_screen('interface1')

class Interface2App(App):
    '''The kivy App that runs the main root. All we do is build a catalog
    widget into the root.'''

    def build(self):
        screen = Catalog()
        screen.name = 'interface2'
        return screen
    def on_pause(self):
        return True


if __name__ == "__main__":
    Interface2App().run()