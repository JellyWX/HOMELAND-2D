from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.clock import Clock


class Game(Widget):

  started = False
  waves = []
  towers = []
  path = []

  def __init__(self,*args,**kwargs):
    super(Game,self).__init__(*args,**kwargs)
    Builder.load_file('game.kv') ## load the game's assigned layout file ##
    Clock.schedule_interval(self.update,1/20)

  def set_level(self,level): ## method for loading levels from files
    pass

  def update(self,t):
    if started:
      self.sort_widgets()

  def sort_widgets(self): ## method to make sure objects render in the correct order
    children_sorted = sorted(self.children,key=lambda w: w.y)
    children_sorted.reverse()

    if children_sorted != self.children:
      for i in children_sorted:
        self.remove_widget(i)
        self.add_widget(i)
