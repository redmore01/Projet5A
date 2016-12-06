
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

BLEU = (0, 1, 1)
CATALOG_ROOT = os.path.dirname(__file__)

#Can be used later for Heritage
'''List of classes that need to be instantiated in the factory from .kv files.
'''
CONTAINER_KVS = os.path.join(CATALOG_ROOT, 'container_kvs')
CONTAINER_CLASSES = [c[:-3] for c in os.listdir(CONTAINER_KVS)
    if c.endswith('.kv')]




class Catalog(BoxLayout):
    
    language_box = ObjectProperty()
    screen_manager = ObjectProperty()
  
    def __init__(self, **kwargs):
        self._previously_parsed_text = ''
        super(Catalog, self).__init__(**kwargs)
  
        self.carousel = None
    
    def change_color(self, source):
        Color(*BLEU)


class KivyCatalogApp(App):
    '''The kivy App that runs the main root. All we do is build a catalog
    widget into the root.'''

    def build(self):
        return Catalog()

    def on_pause(self):
        return True


if __name__ == "__main__":
    KivyCatalogApp().run()
