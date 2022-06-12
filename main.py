import pygame
import grid

pygame.init()
pygame.display.init()

s_w = 1000
s_h = 1000

dims = (s_w, s_h)

display = pygame.display.set_mode(dims)

new_grid = grid.Grid()

def draw_cells():

    for cell in new_grid.grid: 
        pygame.Surface.blit(display, cell.properties["surface"], cell.properties["position"])

def main():  

    started_flag = False
    
    while True: 

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
    
                if event.type == pygame.KEYDOWN: 

                    if event.unicode == 'a' and started_flag == False:
                        new_grid.set_all_alive()

                    if event.unicode == 's' and started_flag == False:
                        started_flag = True

                    if event.unicode == 'p' and started_flag == True: 
                        started_flag = False 

                    if event.unicode == 'r': 
                        started_flag = False
                        new_grid.reset_grid()

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    
                    if started_flag == False: 

                        for cell in new_grid.grid: 
                            mouse_pos = pygame.mouse.get_pos()

                            if pygame.Rect.collidepoint(cell.properties["rect"], mouse_pos): 
                                cell.on_click()

            if event.type == pygame.QUIT:  
                pygame.quit()
                break

        if new_grid.check_all_dead(): 
            started_flag = False

            # Automatically enter stopped state if all cells have died.

        if started_flag == True:

            for i in range(10**6 + (5*(10**6)) + (3*(10**6))):
                pass 

            # above code just for adding a time buffer between grid update cycles
            # slows update process down a bit so the game doesn't run so fast that you don't see the changing patterns well

            new_grid.update_state()

        draw_cells()
        pygame.display.flip()

main()