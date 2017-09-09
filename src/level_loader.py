from grid import Grid
from locations import LEVELS, ASSETS

import json

class Level(object):

  def __init__(self,level):
    self.level = level
    self.name = level
    self.size = (16,10)
    self.map = []
    self.entry = []
    self.exit = []

    with open(ASSETS + 'Tower/towers.json') as f:
      self.towers = json.load(f)

    with open(LEVELS + level + '/data','r') as f:
      for l in f:
        l = l.strip()
        if l.startswith('name='):
          name = l.split('=')
          name.pop(0)
          name = ' '.join(name)

          self.name = name

        elif l.startswith('size='):
          size = l.split('=')
          size.pop(0)
          size = ''.join(size)
          size = size.split(',')

          size = map(float,size)

          self.size = tuple(size)


    with open(LEVELS + level + '/map','r') as f:
      rown = 0
      for l in f:
        l = l.strip()

        if l.startswith('#') or len(l) < 2:
          continue

        self.map.append([])

        row = l.split(',')
        for item in row:
          if item in [str(i) for i in range(6)]:
            self.map[rown].append(Grid(access=int(item)))

          else:
            print('WARN: Did not expect character \'' + str(item) + '\' in map declaration.')
            self.map[rown].append(Grid())

        rown += 1

      self.size = float(len(self.map)), float(len(self.map[0]))
      print(self.size)

  def getExit(self):
    for row in range(len(self.map)):
      for col in range(len(self.map[row])):
        if self.map[row][col].access == 5:
          return row,col

  def getEntry(self):
    for row in range(len(self.map)):
      for col in range(len(self.map[row])):
        if self.map[row][col].access == 4:
          return row,col
