from kivy.uix.widget import Widget

from locations import ASSETS

class Tower(Widget):

  name = 'DEFAULT'

  targets = ['air','ground']
  damage = 0
  rng = 0
  speed = 0

  in_range = []

  base = ASSETS + 'Tower/base.png'
  turret = ASSETS + 'placeholder/invisible.png'

  def attack(self):
    pass


class Gatling(Tower):
  name = 'Gatling'

  targets = ['ground','air']
  damage = 5
  rng = 2.5
  speed = 0.15

  turret = ASSETS + 'Tower/Gatling/turret.png'
