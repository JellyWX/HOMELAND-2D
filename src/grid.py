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

  shade = Li([1,1,1,1])

  tower = None

  tower_parts = {
    base: Str(ASSETS + 'placeholder/invisible.png',)
    turret: Str(ASSETS + 'placeholder/invisible.png')
  }

  def __init__(self,access=0,*args,**kwargs):
    super(Grid,self).__init__(*args,**kwargs)
    self.rotation = choice((0,90,180))

    self.access = access

    if self.access in [0,2]:
      self.overlay = ASSETS + 'Grid/overlay.png'

    else:
      self.overlay = ASSETS + 'placeholder/invisible.png'

    if self.access == 0:
      self.src = ASSETS + 'Grid/RustyPanel1.png'
      self.buildable = True
      self.travellable = True

    elif self.access in [1, 4, 5]:
      self.buildable = False
      self.travellable = True

      if self.access == 1:
        self.src = ASSETS + 'Grid/RustyGrid1.png'

      elif self.access == 4:
        self.src = ASSETS + 'Grid/Entry.png'

      else:
        self.src = ASSETS + 'Grid/Exit.png'

    elif self.access == 2:
      self.buildable = True
      self.travellable = False

    elif self.access == 3:
      self.buildable = False
      self.travellable = False
      self.src = ASSETS + 'Grid/hole.png'

  def build(self,tower):
    self.travellable = False
    self.buildable = False

    self.tower = tower
    self.tower_parts['base'] = ASSETS + 'Tower/base.png'
    self.tower_parts['turret'] = ASSETS + 'Tower/' + tower['name'] + '/turret.png'
