import cell
from pygame import Surface
from pygame import Rect

class Grid:

    def __init__(self): 
        self.cell_lookup_table = dict()
        self.pos_to_id_lookup_table = dict()
        self.grid = list()

        self.screen_width = 1000 
        self.screen_height = 1000

        self.cell_w = 15
        self.cell_h = 15
        self.cell_dims = [self.cell_w, self.cell_h]

        self.pad = 5

        self.num_cells = ( (self.screen_width // (self.cell_w + self.pad )) * (self.screen_height // (self.cell_h + self.pad)) )


        self.x_inc = self.cell_w + self.pad
        self.y_inc = self.cell_h + self.pad
        self.initialization_routine()

    def initialization_routine(self):

        self.add_cells()
        self.set_cell_positions()
        self.set_cell_rects()
        self.set_cell_surfaces()
        self.set_cell_neighbors()

    def add_cells(self):
        # first create a cell and add its properties 
        # then add the other pygame objects to the cells property dictionary 
        # get the values for the pygame objects from their respective values in the cell's property dictionary

        for i in range(self.num_cells + 1): 
                new_cell = cell.Cell()
                new_cell.properties["width"] = self.cell_w
                new_cell.properties["height"] = self.cell_h
                new_cell.properties["id"] = i
                self.cell_lookup_table[i] = new_cell
                self.grid.append(new_cell)

    def set_cell_positions(self): 
        # this needs to be made better because the cells don't fit perfectly within the screens dimensions
        x = self.pad
        y = self.pad
        
        for cell in self.grid: 

            cell.properties["position"] = [x,y]
            self.pos_to_id_lookup_table[str(cell.properties["position"])] = cell.properties["id"]

            if x + self.x_inc + self.cell_w > ( self.screen_width ): 

                x = self.pad

                if y + self.y_inc + self.cell_h > ( self.screen_height ):
                    pass
                else:
                    y += self.y_inc

            else: 
                x += self.x_inc

    def set_cell_rects(self):

        for cell in self.grid:
            cell.properties["rect"] = Rect(cell.properties["position"], self.cell_dims)
        
    def set_cell_surfaces(self):

        for cell in self.grid:

            cell_surface = Surface(self.cell_dims)
            cell_surface.fill(cell.properties["color"])

            cell.properties["surface"] = cell_surface
    
    def check(self, key_obj):
        # to make checking if a neighbor position is valid much quicker
        # (a cell neighbor position that would be off the screen is invalid)
        # but gets collected in the brute force search for all possible neighbor positions of a given cell anyway
        try:
            self.pos_to_id_lookup_table[key_obj]
            return True

        except:
            return False

    def set_cell_neighbors(self):

        for cell in self.grid: 
            a0 = [cell.properties["position"][0] - self.x_inc, cell.properties["position"][1] - self.y_inc]
            a1 = [cell.properties["position"][0]             , cell.properties["position"][1] - self.y_inc]
            a2 = [cell.properties["position"][0] + self.x_inc, cell.properties["position"][1] - self.y_inc]
            a3 = [cell.properties["position"][0] - self.x_inc, cell.properties["position"][1]]

            a4 = [cell.properties["position"][0] + self.x_inc, cell.properties["position"][1]]
            a5 = [cell.properties["position"][0] - self.x_inc, cell.properties["position"][1] + self.y_inc]
            a6 = [cell.properties["position"][0]             , cell.properties["position"][1] + self.y_inc]
            a7 = [cell.properties["position"][0] + self.x_inc, cell.properties["position"][1] + self.y_inc]
            
            #k = list(self.pos_id_lookup_table.keys()) part of old solution

            if self.check(str(a0)): 
                cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a0)])
            if self.check(str(a1)): 
                cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a1)])
            if self.check(str(a2)): 
                cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a2)])
            if self.check(str(a3)): 
                cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a3)])
            if self.check(str(a4)): 
                cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a4)])
            if self.check(str(a5)):
                cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a5)])
            if self.check(str(a6)):
                cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a6)])
            if self.check(str(a7)): 
                cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a7)])
            
            #if str(a0) in k: 
            #    cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a0)])
            #if str(a1) in k: 
            #    cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a1)])
            #if str(a2) in k: 
            #    cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a2)])
            #if str(a3) in k: 
            #    cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a3)])
            #if str(a4) in k: 
            #    cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a4)])
            #if str(a5) in k:
            #    cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a5)])
            #if str(a6) in k:
            #    cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a6)])
            #if str(a7) in k: 
            #    cell.properties['neighbors'].append(self.pos_to_id_lookup_table[str(a7)])
        
        # old solution 1654193048277257000 start time ns; 1654193069389577000 end time ns
        # new solution 1654193130635696000 start time ns; 1654193130869904000 end time ns
        # Old solution was 90 times slower


    def count_live_neighbors(self): 

        for cell in self.grid: 
            c = 0

            for neighbor_id in cell.properties["neighbors"]: 
                if self.cell_lookup_table[neighbor_id].properties["state"] == 1:
                    c += 1 

            cell.properties["live_count"] = c 

    def check_all_dead(self):
        # If all the cells have died return true 

        for cell in self.grid:

            if cell.properties["state"] == 1: 
                return False
        
        return True

    def set_all_alive(self):
        # random function to set all the cells to alive
        # completely unnecessary

        for cell in self.grid:
            cell.set_alive()


    def apply_conways_rules(self):
        self.count_live_neighbors()

        for cell in self.grid:

            if cell.properties["state"] == 0:
                if cell.properties["live_count"] == 3: 
                    cell.set_alive()

            if cell.properties["live_count"] < 2 :
                cell.set_dead()

            elif cell.properties["live_count"] > 3:
                cell.set_dead()

    def update_state(self):
        self.apply_conways_rules()

    def reset_grid(self): 

        for cell in self.grid: 
            cell.set_dead()
