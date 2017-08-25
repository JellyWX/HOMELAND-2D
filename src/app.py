from kivy.app import App
from kivy.base import EventLoop

from screenmanager import Manager

class Main(App):

  def on_start(self):
    self.manager.game.set_level('')

  def build(self):
    self.manager = Manager()
    return self.manager

uf = Main()
