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
    self.routes = []
    while not _checkRoutesValidity():
      _getRoutes()

    def _getRoutes():
      new_routes = []
      for route in self.routes:
        for i in ((1,0),(-1,0),(0,1),(0,-1)):
          r = route
          new_loc = [x + y for x,y in zip(r[-1],i)]
          for index in new_loc:
            if index < 0:
              continue ## if the index causes a skip across the side of the array, ignore it and skip over
          try:
            if self.map[new_loc[0]][new_loc[1]].travellable:
              r.append(new_loc)
              new_routes.append(r)
          except IndexError:
            pass
      self.routes = new_routes

    def _checkRoutesValidity():
      for route in self.routes:
        if route[-1].access == 5:
          return route
          break
      else:
        return None
