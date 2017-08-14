from kivy.uix.widget import Widget

class Player(Widget):
  frags = 0
  crystals = 0

  def __init__(self,*args,**kwargs):
    super(Player,self).__init__(*args,**kwargs)
