from pygame import Color

class Cell:

    def __init__(self):

        self.color_white = Color(255,255,255)
        self.color_blue = Color(0,0,255)
        
        self.properties = {

            "color"      : self.color_white, 
            
            "height"     : 0, 
            "live_count" : 0, 
            "state"      : 0, 
            "width"      : 0, 
            "id"         : 0, 
            
            "rect"       : None, 
            "surface"    : None, 
            
            "position"   : [], 
            "neighbors"  : [] 

        }

    def on_click(self):
        
        if self.properties["state"] == 1: 

            self.properties["state"] = 0
            self.properties["color"] = self.color_white
            self.properties["surface"].fill(self.color_white)

        else: 

            self.properties["state"] = 1
            self.properties["color"] = self.color_blue
            self.properties["surface"].fill(self.color_blue)

    
    def set_alive(self): 

        self.properties["state"] = 1 
        self.properties["color"] = self.color_blue
        self.properties["surface"].fill(self.color_blue)


    def set_dead(self): 

        self.properties["state"] = 0
        self.properties["color"] = self.color_white
        self.properties["surface"].fill(self.color_white)





