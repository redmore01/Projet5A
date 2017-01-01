
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
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.button import Button

class Boxheight(BoxLayout):
    pass

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

        print(self.listim)
		
        boxbot = Boxheight()
        boxbot.height= 45
		
        btnback = Button(text = 'Retour')
        btnback.bind(on_press = lambda a: self.disconnect())
		
        btnplay = Button(text = 'Lecture')	
        btnpause = Button(text = 'Pause')
        btnstop = Button(text = 'Stop')

        btnsend = Button(text = 'Enregistrer')
        # btnsend.bind(on_press = lambda a: self.send())
		
            
        if x <= 2:
            gridscreen = GridLayout(cols = x)
            for y in self.listim:
	
                # newimage= y+'.avi'
                video= VideoPlayer(source = y+'.avi')
                video.state='pause'
                btnplay.bind(on_press = lambda a, video=video: self.playvideo(video))
                btnpause.bind(on_press = lambda a, video=video: self.pausevideo(video))
                btnstop.bind(on_press = lambda a, video=video: self.stopvideo(video))



                gridscreen.add_widget(video)
        else:
            gridscreen = GridLayout(rows = x-2)
            for y in self.listim:

                # newimage= y+'.avi'
                video= VideoPlayer(source = y+'.avi', state = 'pause')
                btnplay.bind(on_press = lambda a, video=video: self.playvideo(video))
                btnpause.bind(on_press = lambda a, video=video: self.pausevideo(video))
                btnstop.bind(on_press = lambda a, video=video: self.stopvideo(video))
                gridscreen.add_widget(video)

        lastscreen = self.manager.get_screen('interface4').lastscreen
        lastscreen.clear_widgets()
		
        boxbot.add_widget(btnback)
        boxbot.add_widget(btnplay)
        boxbot.add_widget(btnpause)
        boxbot.add_widget(btnstop)
        boxbot.add_widget(btnsend)

        
        lastscreen.add_widget(gridscreen)
        lastscreen.add_widget(boxbot)


		
		
    # def lecturevideo(self):
        
    def playvideo(self, video):
        video.state='play'

				
    def pausevideo(self, video):
        video.state='pause'
               

    def stopvideo(self, video):
        video.state='stop'
               


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
