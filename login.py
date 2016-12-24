import kivy
kivy.require('1.0.5')
import os
import sys
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

from interface1 import Interface1
from interface2 import Interface2App

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

# from interface1 import KivyCatalogApp

Builder.load_string('''
<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'erreur'
    Button:
        text: 'Erreur de login ou mot de pass'
        on_press: root.dismiss()

''')

class CustomPopup(Popup):
	pass

class Login(Screen):

	screen = ObjectProperty()
	def do_login(self, login, pwd):
		if login == 'KivyLayout':
			if pwd == 'Houssam':
				self.manager.current = self.manager.next()
			else:
				self.show_popup()
		else:
			self.show_popup()
				

	def show_popup(self):
		p = CustomPopup()
		p.open()
				
	def resetForm(self):
		self.ids['login'].text = ""
		self.ids['password'].text = ""

class LoginApp(App):
	def build(self):
		manager = ScreenManager()

		# ajout de l'instance de login
		manager.add_widget(Login(name='login'))

		# ajout de la vue 'interface1'
		app = Interface1()
		app.load_kv()
		interfacen1 = app.build()
		manager.add_widget(interfacen1)
		
		# ajout de la vue 'interface2'
		app2 = Interface2App()
		app2.load_kv()
		interfacen2 = app2.build()
		manager.add_widget(interfacen2)

		manager.transition = SlideTransition(direction="left")
		return manager

		# return Login()

	# def on_pause(self):
		# return True

if __name__ == '__main__':
	LoginApp().run()
