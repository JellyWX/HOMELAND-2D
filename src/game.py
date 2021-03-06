from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock

from locations import LEVELS
from grid import Grid
from level_loader import Level
from enemy import Enemy


class BG(Widget):
    r = NumericProperty(0.15)


class Game(Widget):

    ## game objects ##

    bg = ObjectProperty(None)

    ## game details ##

    started = 1

    grid_size = (24.0,15.0)

    ## rendering stuff ##

    aspect_x = 16.0/10
    aspect_y = 10.0/16

    proper_w = 24
    proper_h = 15

    ## useful things ##

    mouse_pos = (0,0)

    selection_state = False
    clicked_cell = False

    def __init__(self,*args,**kwargs):
        super(Game,self).__init__(*args,**kwargs)
        Builder.load_file('game.kv') ## load the game's assigned layout file ##

        Clock.schedule_interval(self.update,1.0/60)

    def set_level(self,level): ## method for loading levels from files ##
        self.level = Level(level)

        self.grid_size = self.level.size
        self.aspect_x = self.grid_size[0]/self.grid_size[1]
        self.aspect_y = self.grid_size[1]/self.grid_size[0]

        self.grid = self.level.map
        for row in self.grid:
            for item in row:
                self.add_widget(item)

        self.enemy = Enemy('DEFAULT',self.level)

    def catch_mouse(self,etype,pos):
        self.mouse_pos = pos

    def on_touch_down(self,mouse):
        self.selection_state = not self.selection_state

    def update(self,t):
        if float(self.width) / self.height < self.aspect_x:
            self.proper_w = self.width
            self.proper_h = self.width * self.aspect_y

        elif float(self.width) / self.height > self.aspect_x:
            self.proper_w = self.height * self.aspect_x
            self.proper_h = self.height

        if self.started:
            self.enemy.getRoute()
            self.size_widgets()

    def size_widgets(self):
        set_overlay = 0

        self.bg.size = self.proper_w,self.proper_h
        self.bg.center = self.center
        self.bg.r = self.proper_h * 1 / 100

        xpos = 0
        for row in self.grid:
            ypos = 0
            for item in row:
                item.x = self.bg.x + self.bg.width/self.grid_size[0] * xpos
                item.y = self.bg.y + self.bg.height/self.grid_size[1] * ypos
                item.size = self.bg.width/self.grid_size[0],self.bg.height/self.grid_size[1]

                if item in self.enemy.route_t:
                    item.shade = [0,1,0,1]
                else:
                    item.shade = [1,1,1,1]

                if not self.selection_state:

                    if not set_overlay and item.collide_point(self.mouse_pos[0],self.mouse_pos[1]):
                        if self.clicked_cell: ## if this is the first cell covered when the user presses the mouse out of selected mode:

                            if self.selected_cell == item:
                                if self.selected_cell.tower is not None:
                                    item.clear()
                                elif self.selected_cell.buildable:
                                    item.build(self.level.towers['gatling'])
                                    try:
                                        self.enemy.getRoute()
                                    except:
                                        item.clear()

                            self.clicked_cell = False

                        item.overlay_col = [1,0,0,1] ## sets to red (hover)
                        set_overlay = 1 ## confirms that only one cell can be selected at once
                        self.selected_cell = item

                    else:
                        item.overlay_col = [0,0,0,1]

                else:
                    self.clicked_cell = True
                    self.selected_cell.overlay_col = [0,0,1,1] ## sets to blue (clicked)

                ypos += 1
            xpos += 1
