from kivy.app import App
from kivy.base import EventLoop
from kivy.core.window import Window

from screenmanager import Manager

class Main(App):

  def on_start(self):
    self.manager.game.set_level('level_02')
    Window.bind(mouse_pos=self.manager.game.catch_mouse)

  def build(self):
    self.manager = Manager()
    return self.manager

td = Main()
