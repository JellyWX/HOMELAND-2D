from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock

from locations import LEVELS


class BG(Widget):
  r = NumericProperty(0.15)


class Game(Widget):

  ## game objects ##

  bg = ObjectProperty(None)

  ## game details ##

  started = 1

  waves = []
  towers = []
  monsters = []
  path = []


  ## rendering stuff ##

  aspect_x = 16.0/10
  aspect_y = 10.0/16

  proper_w = 24
  proper_h = 15

  def __init__(self,*args,**kwargs):
    super(Game,self).__init__(*args,**kwargs)
    Builder.load_file('game.kv') ## load the game's assigned layout file ##
    Clock.schedule_interval(self.update,1.0/20)

  def set_level(self,level): ## method for loading levels from files ##
    pass

  def update(self,t):
    if float(self.width) / self.height < self.aspect_x:
      self.proper_w = self.width
      self.proper_h = self.width * self.aspect_y

    elif float(self.width) / self.height > self.aspect_x:
      self.proper_w = self.height * self.aspect_x
      self.proper_h = self.height

    if self.started:
      #self.sort_widgets()
      self.size_widgets()

  def sort_widgets(self): ## method to make sure objects render in the correct order ##
    children_sorted = sorted(self.children,key=lambda w: w.y)
    children_sorted.reverse()

    if children_sorted != self.children:
      for i in children_sorted:
        if not 'NO_SORT' in i.tags:
          self.remove_widget(i)
          self.add_widget(i)

  def size_widgets(self):
    self.bg.size = self.proper_w,self.proper_h
    self.bg.center = self.center
    self.bg.r = self.proper_h * 1 / 100
