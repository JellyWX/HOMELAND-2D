from locations import LEVELS


class Level(object):

  def __init__(self,level):
    self.level = level
    self.name = level
    self.size = (24,15)

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
