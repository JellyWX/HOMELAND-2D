from grid import Grid
from locations import LEVELS


class Level(object):

  def __init__(self,level):
    self.level = level
    self.name = level
    self.size = (16,10)
    self.map = []

    with open(LEVELS + level + '/data','r') as f:
      for l in f:
        l = l.strip()
        if l.startswith('name='):
          name = l.split('=')
          name.pop(0)
          name = ' '.join(name)

          self.name = name

        #elif l.startswith('size='):
        #  size = l.split('=')
        #  size.pop(0)
        #  size = ''.join(size)
#          size = size.split(',')
#
#          size = map(float,size)
#
#          self.size = tuple(size)

    #self.map = [[Grid() for i in range(int(self.grid_size[1]))] for i in range(int(self.grid_size[0]))]

    with open(LEVELS + level + '/map','r') as f:
      row = 0
      for l in f:
        self.map.append([])

        if l.startswith('#'):
          continue

        row = l.split(',')
        for item in row:
          if item in ['0', 'all', 'bt']:
            self.map[row].append(Grid())

          elif item in ['1', 't']:
            self.map[row].append(Grid(buildable=False))

          elif item in ['2', 'b']:
            self.map[row].append(Grid(travellable=False))

          elif item in ['3', 'n', 'none']:
            self.map[row].append(Grid(buildable=False,travellable=False))

          else:
            raise ValueError('Did not expect character \'' + str(item) + '\' in map declaration.')
            
        row += 1
