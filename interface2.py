

import kivy
kivy.require('1.0.5')
import os
import sys
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from kivy.uix.scatter import Scatter
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.splitter import Splitter
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from functools import partial
from kivy.uix.pagelayout import PageLayout


AllImage_ROOT = os.path.dirname(__file__)

from interface3 import Interface3App

'''List of classes that need to be instantiated in the factory from .kv files.
'''
CONTAINER_PNG = os.path.join(AllImage_ROOT, 'images')
IMAGES_NAMES = [c[:-4] for c in os.listdir(CONTAINER_PNG)]

LIST_IM = os.listdir(CONTAINER_PNG)
 
class ImageButton(ButtonBehavior, Image):
    pass

class GridButton(ButtonBehavior, GridLayout):
    pass

class BoxDisc(BoxLayout):
    pass
	
	
class ScatterWithImage(Scatter):
    src = StringProperty("softboy.png")

class ToggleWithImage(ToggleButton):
    src = StringProperty("softboy.png")

class GridWithCanvas(GridButton):
    pass

	
class AllImage(Screen):
    
    list = ['']
    # self.screen_manager = ObjectProperty()
    screen = ObjectProperty()
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
		
		
        boxdiscornnect = BoxDisc()
        buttondisconnect = Button(text='Se deconnecter')
        buttondisconnect.bind(on_press= lambda a:self.backtologin())
        boxdiscornnect.add_widget(buttondisconnect)
		
        self.mainbox = BoxLayout()
        self.add_widget(self.mainbox)
        self.mainbox.orientation='vertical'

        self.splitter = Splitter(sizable_from = 'bottom')
        rootgrid = ScrollView()
        rootbox = ScrollView() 
		
        self.x=0
        self.listim = []
		
        self.layout = GridLayout(cols=4, spacing=10)
        self.layout.height= '800sp'
        self.layout.size_hint_y=None
		
        self.box = BoxLayout()
        self.box.orientation = 'horizontal'
        self.box.size_hint_x=None
        self.box.spacing = 40
        self.box.width=self.width
		
        self.mainbox.add_widget(self.splitter)
        # super(AllImage, self).__init__(**kwargs)
        for im in IMAGES_NAMES:
            if IMAGES_NAMES != None :
	
                toggleimage = ToggleWithImage(src=im+'.png')
                toggleimage.bind(on_press=  lambda a, im=im:self.onpress_addpage(self.listim, im)) 
                self.layout.add_widget(toggleimage)

				
        print(self.listim)
        rootbox.add_widget(self.box)
        self.splitter.add_widget(rootbox)
        rootgrid.add_widget(self.layout)
         
        self.mainbox.add_widget(rootgrid)
        self.mainbox.add_widget(boxdiscornnect)
		
        trylist = ListProperty([1,1,1,1])
        print(trylist)
        

    def onpress_addpage(self, listim, im):
        # newimage= im+'.png'
        existinlist=0
 
        for image in self.listim[:]:
            if im == image:
                self.listim.remove(im)
                
                existinlist=1
                break
            else:
                existinlist=0
        if existinlist == 0:    
            self.listim.extend([im])

        if existinlist==1: 
            self.box.clear_widgets()
			
        for nbmelement in range(0,len(self.listim)):
        
            self.box.clear_widgets()
            if nbmelement>=0:
            
                self.box.width=(self.width) * 1
                
                gridpage1 = GridLayout(cols = 1, spacing=2)   

                button_interfaceswitch1 = GridWithCanvas()  
                for y in self.listim:
		
                    newimage= y+'.png'
                    image = Image(source = newimage)
                    gridpage1.add_widget(image)
                button_interfaceswitch1.bind(on_press=lambda a: self.change_screen(1,self.listim))
                button_interfaceswitch1.add_widget(gridpage1)
                self.box.add_widget(button_interfaceswitch1)
				
            if nbmelement>=1:
           
                self.box.width=(self.width) * 1.5 
                gridpage2 = GridLayout(rows = 1, spacing=2)  
                button_interfaceswitch2 = GridWithCanvas()  				
                for y in self.listim:
		
                    newimage= y+'.png'
                    image = Image(source = newimage)
                    gridpage2.add_widget(image)
                button_interfaceswitch2.bind(on_press=lambda a: self.change_screen(3,self.listim))
                button_interfaceswitch2.add_widget(gridpage2)
                self.box.add_widget(button_interfaceswitch2)


            if nbmelement>=2:
           
                self.box.width=(self.width) * 2
                gridpage3 = GridLayout(rows = 2, spacing=2)         
                button_interfaceswitch3 = GridWithCanvas()  				
                for y in self.listim:
		
                    newimage= y+'.png'
                    image = Image(source = newimage)
                    gridpage3.add_widget(image)
                button_interfaceswitch3.bind(on_press=lambda a: self.change_screen(4,self.listim))
                button_interfaceswitch3.add_widget(gridpage3)
                self.box.add_widget(button_interfaceswitch3)

            if nbmelement>=3:
            
                self.box.width=(self.width) * 2.5
                gridpage4 = GridLayout(cols = 2, spacing=2)   
                			
                button_interfaceswitch4 = GridWithCanvas()  				
                for y in self.listim:
		
                    newimage= y+'.png'
                    image = Image(source = newimage)
                    gridpage4.add_widget(image)
                button_interfaceswitch4.bind(on_press=lambda a: self.change_screen(2,self.listim))
                button_interfaceswitch4.add_widget(gridpage4)
                self.box.add_widget(button_interfaceswitch4)

        print(self.listim)
        

    def change_screen(self, x, list): 
        print("login : %s || pass : %s")
        
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

		
		
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'interface3'
        self.manager.get_screen('interface3')
        self.manager.list1 = self.listim
        self.manager.x = x
	
    def backtologin(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

	

    
class Interface2App(App):
    '''The kivy App that runs the main root. All we do is build a AllImage
    widget into the root.'''

    def build(self):
        
        screen = AllImage()
        screen.name = 'interface2'
        return screen

if __name__ == "__main__":
    Interface2App().run()
