from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty


class Manager(ScreenManager):
  game = ObjectProperty(None)
