from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import StringProperty


class Player(Widget):

  frags = 0
  crystals = 0

  rots = ('s','sw','w','nw','n','ne','e','se')
  rot = 's'

  img = StringProperty('player_' + rot + '.png')

  def __init__(self,*args,**kwargs):
    super(Player,self).__init__(*args,**kwargs)
    Clock.schedule_interval(self.update,1/10)

  def update(self,t):
    self.size
