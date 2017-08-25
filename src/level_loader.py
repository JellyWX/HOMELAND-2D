from locations import LEVELS


class Level(object):

  def __init__(self,level):
    self.level = level
    self.name = level
    self.aspect = (24,15)

    try:
      with open(LEVELS + level + '/data','r'):
        for l in f:
          l = l.strip()
          if l.startswith('name='):
            self.name = ' '.join(l.split('=').del(0))

          elif l.startswith('size='):
            self.aspect = tuple(' '.join(l.split('=').del(0)).split(','))
