

import kivy
kivy.require('1.4.2')
import os
import sys
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.selectableview import SelectableView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.splitter import Splitter
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from functools import partial
from kivy.uix.pagelayout import PageLayout
BLEU = (0, 1, 1)
AllImage_ROOT = os.path.dirname(__file__)

#Can be used later for Heritage
'''List of classes that need to be instantiated in the factory from .kv files.
'''
CONTAINER_PNG = os.path.join(AllImage_ROOT, 'images')
IMAGES_NAMES = [c[:-4] for c in os.listdir(CONTAINER_PNG)]

 
class ImageButton(ButtonBehavior, Image):
    pass

class GridButton(ButtonBehavior, GridLayout):
    pass


class AllImage(BoxLayout):
    
    
    # screen_manager = ObjectProperty()
  
    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)
        self.orientation='vertical'

        self.splitter = Splitter(sizable_from = 'bottom')
        rootgrid = ScrollView()
        rootbox = ScrollView() 
		
        self.x=1
        self.listim = []
		
        self.layout = GridLayout(cols=4, spacing=10)
        self.layout.height= '800sp'
        self.layout.size_hint_y=None
		
        self.box = BoxLayout()
        self.box.orientation = 'horizontal'
        self.box.size_hint_x=None
        self.box.width=self.width
		
        self.add_widget(self.splitter)
        # super(AllImage, self).__init__(**kwargs)
        for im in IMAGES_NAMES:
            if IMAGES_NAMES != None :
                 
                btn = ImageButton(source = im+'.png')
                btn.bind(on_press=  lambda a, im=im:self.onpress_addpage(self.listim, im))                
                self.layout.add_widget(btn)
				
        print(self.listim)
        rootbox.add_widget(self.box)
        self.splitter.add_widget(rootbox)
        rootgrid.add_widget(self.layout)
         
        self.add_widget(rootgrid)
        

    def onpress_addpage(self, listim, im):
        newimage= im+'.png'
        existinlist=0
 
        for image in self.listim[:]:
            if newimage == image:
                self.listim.remove(newimage)
                
                existinlist=1
                break
            else:
                existinlist=0
        if existinlist == 0:    
            self.listim.extend([newimage])

        if existinlist==1: 
            self.box.clear_widgets()
			
        for nbmelement in range(0,len(self.listim)):
        
            self.box.clear_widgets()
            if nbmelement>=0:
            # if newimage not in self.listim[:]:
            
                self.box.width=(self.width) * 1
                
                gridpage1 = GridLayout(cols = 1, spacing=10)   
                button_interfaceswitch1 = GridButton(cols = 1)  
               
                for y in self.listim:
		
                    image = Image(source = y)
                    gridpage1.add_widget(image)
                button_interfaceswitch1.bind(on_press=lambda a, image=image:self.layout.add_widget( ImageButton(source = 'softboy.png') ))

                button_interfaceswitch1.add_widget(gridpage1)
                self.box.add_widget(button_interfaceswitch1)
				
            if nbmelement>=1:
            # if newimage not in self.listim[:]:
            
                self.box.width=(self.width) * 1.5 
                gridpage2 = GridLayout(rows = 1, spacing=10)  
                button_interfaceswitch2 = GridButton(cols = 1)  				
                for y in self.listim:
		
                    image = Image(source = y)
                    gridpage2.add_widget(image)
                button_interfaceswitch2.bind(on_press=lambda a, image=image:self.layout.add_widget( ImageButton(source = 'hy1.png') ))
                button_interfaceswitch2.add_widget(gridpage2)
                self.box.add_widget(button_interfaceswitch2)


            if nbmelement>=2:
            # if newimage not in self.listim[:]:
            
                self.box.width=(self.width) * 2
                gridpage3 = GridLayout(rows = 2, spacing=10)         
                button_interfaceswitch3 = GridButton(cols = 1)  				
                for y in self.listim:
		
                    image = Image(source = y)
                    gridpage3.add_widget(image)
                button_interfaceswitch3.bind(on_press=lambda a, image=image:self.layout.add_widget( ImageButton(source = '1211810004.png') ))
                button_interfaceswitch3.add_widget(gridpage3)
                self.box.add_widget(button_interfaceswitch3)

            if nbmelement>=3:
            # if newimage not in self.listim[:]:
            
                self.box.width=(self.width) * 2.5
                gridpage4 = GridLayout(cols = 2, spacing=10)               
                button_interfaceswitch4 = GridButton(cols = 1)  				
                for y in self.listim:
		
                    image = Image(source = y)
                    gridpage4.add_widget(image)
                button_interfaceswitch4.bind(on_press=lambda a, image=image:self.layout.add_widget( ImageButton(source = 'mix.png') ))
                button_interfaceswitch4.add_widget(gridpage4)
                self.box.add_widget(button_interfaceswitch4)

        print(self.listim)
        

	
	
	
    def change_color_btn(ImageButton): #A ajouter pour changer la couleur de l'arrier plan
	                                   #de l'image selectionner
        self.background_color= 1.0, 0.0, 0.0, 1.0	


class Interface1(App):
    '''The kivy App that runs the main root. All we do is build a AllImage
    widget into the root.'''

    def build(self):
        return AllImage()

    def on_pause(self):
        return True


if __name__ == "__main__":
    Interface1().run()
