from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.clock import Clock


class Game(Widget):

  started = False
  waves = []
  towers = []

  def __init__(self,*args,**kwargs):
    super(Game,self).__init__(*args,**kwargs)
    Builder.load_file('game.kv') ## load the game's assigned layout file ##
    Clock.schedule_interval(self.update,1/20)

  def set_level(self,level):
    pass

  def update(self,t):
    if started:
