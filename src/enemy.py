from kivy.uix.widget import Widget
from kivy.properties import StringProperty as Str
from kivy.clock import Clock

from random import shuffle

from locations import ASSETS


class Enemy(Widget):

  name = 'DEFAULT'
  tile = (0,0)

  route = []
  route_t = []

  src = Str(ASSETS + 'enemy/' + name + '.png')

  def __init__(self, name, level, *args, **kwargs):
    super(Enemy, self).__init__(*args, **kwargs)
    self.name = name

    self.src = ASSETS + 'enemy/' + self.name + '.png'
    self.level = level

    self.tile = level.getEntry()

    Clock.schedule_interval(self.update, 1.0/10.0)

  def update(self, t):
    #self.tile = tile
    pass

  def getRoute(self):

    ''' Many thanks to TemporalWolf on StackOverflow for this bit'''
    def _genLee(start):

      travellable = [[i.travellable for i in row] for row in self.level.map]
      size = list(map(int,self.level.size))

      n_offsets = [(1,0), (-1,0), (0,1), (0,-1)]
      score = 0

      path_map = [[None for _ in range(size[1])] for _ in range(size[0])]
      node_list = [start]
      path_map[start[0]][start[1]] = 0
      for node in node_list:
        score = path_map[node[0]][node[1]]
        for n in n_offsets:
          n_x = node[0] + n[0]
          n_y = node[1] + n[1]
          if n_x < 0 or n_y < 0 or n_x >= size[0] or n_y >= size[1]:
            continue
          if not travellable[n_x][n_y]:
            continue
          if path_map[n_x][n_y] == None:
            node_list.append((n_x,n_y))
            path_map[n_x][n_y] = score + 1
      return path_map

    def _getLowestNeighbour(cell,path_map,route):
      n_offsets = [(1,0), (-1,0), (0,1), (0,-1)]

      for n in n_offsets:
        try:
          if path_map[cell[0]][cell[1]] - path_map[cell[0] + n[0]][cell[1] + n[1]] == 1 and (cell[0] + n[0],cell[1] + n[1]) not in route:
            return cell[0] + n[0],cell[1] + n[1]
        except:
          continue
      else:
        return 'fuck'

    def _getRoute():
      path_map = _genLee(self.level.getExit())
      entry = self.tile
      route = [entry]

      if path_map[entry[0]][entry[1]] == None:
        return False
      else:
        while path_map[route[-1][0]][route[-1][1]] != 0:
          route.append(_getLowestNeighbour(route[-1],path_map,route))
      return route

    self.route = _getRoute()

    self.route_t = []

    for i,j in self.route:
      self.route_t.append(self.level.map[i][j])
