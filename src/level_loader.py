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

        rown += 1

      self.size = float(len(self.map)), float(len(self.map[0]))
      print(self.size)
