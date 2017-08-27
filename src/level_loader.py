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
          if item in ['0', 'all', 'bt']:
            self.map[rown].append(Grid())
            #self.map[rown].append(0)

          elif item in ['1', 't']:
            self.map[rown].append(Grid(buildable=False))
            #self.map[rown].append(1)

          elif item in ['2', 'b']:
            self.map[rown].append(Grid(travellable=False))
            #self.map[rown].append(2)

          elif item in ['3', 'n', 'none']:
            self.map[rown].append(Grid(buildable=False,travellable=False))
            #self.map[rown].append(3)

          else:
            print('WARN: Did not expect character \'' + str(item) + '\' in map declaration.')

        rown += 1

      self.size = float(len(self.map)), float(len(self.map[0]))
      print(self.size)
