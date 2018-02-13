import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.app import Builder
from kivy.uix.button import Label

Builder.load_file("./main.kv")

class PocketPythonApp(App):

  def build(self):
    return Label()

pocketPython = PocketPythonApp()
pocketPython.run()
