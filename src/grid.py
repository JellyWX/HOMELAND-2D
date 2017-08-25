from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

from random import choice

from locations import ASSETS


class Grid(Widget):

  buildable = True
  travellable = True

  rotation = NumericProperty(choice((0,90,180)))

  src = ASSETS + 'Grid/RustyPanel1.png'
  if buildable:
    overlay = ASSETS + 'Grid/overlay.png'
  else:
    overlay = ASSETS + 'placeholder/invisible.png'

  def __init__(self,*args,**kwargs):
    super(Grid,self).__init__(*args,**kwargs)
    self.rotation = choice((0,90,180))
    print(self.rotation)
