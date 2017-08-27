from kivy.uix.widget import Widget
from kivy.properties import NumericProperty as Num, StringProperty as Str, ListProperty as Li

from random import choice

from locations import ASSETS


class Grid(Widget):

  buildable = True
  travellable = True

  rotation = Num(choice((0,90,180)))

  src = Str(ASSETS + 'Grid/Grid.png')
  overlay = Str(ASSETS + 'Grid/overlay.png')
  overlay_col = Li([0,0,0,1])

  def __init__(self,buildable=True,travellable=True,*args,**kwargs):
    super(Grid,self).__init__(*args,**kwargs)
    self.rotation = choice((0,90,180))

    self.buildable = buildable
    self.travellable = travellable

    if self.buildable:
      self.overlay = ASSETS + 'Grid/overlay.png'
      self.src = ASSETS + 'Grid/RustyPanel1.png'
    else:
      self.overlay = ASSETS + 'placeholder/invisible.png'

    if not (self.buildable and self.travellable):
      self.src = ASSETS + 'Grid/hole.png'
