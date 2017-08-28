from kivy.uix.widget import Widget

from locations import ASSETS


class Enemy(Widget):

  name = 'DEFAULT'
  map = []

  src = Str(ASSETS + 'enemy/' + name + '.png')

  def __init__(self,name,map,*args,**kwargs):
    super(Enemy,self).__init__(*args,**kwargs)
    self.name = name

    self.src = ASSETS + 'enemy/' + self.name + '.png'
    self.map = map

  def route(self):
    while

    def _getRoutes():
      pass

    def _checkRoutesValidity():
      for route in self.routes:
        if route[-1].exit:
          return route
          break
      else:
        return None
