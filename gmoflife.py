import time
import pygame
import numpy as mmj


myBackgroundcolor=(12, 14, 20)
myColorofGrid=(40,40,40)
colorof_Die=(170,170,170)
colorof_alive=(255,255,255)

#Update screen, if you don't to want to go tho the next Generation. 
def update(screen, cells, size, with_progress=False):
    
#create Empty numpy array
            cellsrefresh = mmj.zeros((cells.shape[0], cells.shape[1]))

#Go to individual cells, for every cells, ndindex is n - dimensional on numpy
            for row, col in mmj.ndindex(cells.shape):
#Game rules
                        alive = int(cells[(row-1) % cells.shape[0], (col-1)% cells.shape[1]] +
                                    cells[(row-1) % cells.shape[0], col% cells.shape[1]] +
                                    cells[(row-1) % cells.shape[0], (col+1)% cells.shape[1]] +
                                    cells[row % cells.shape[0], (col-1)% cells.shape[1]] +
                                    cells[row % cells.shape[0], (col+1)% cells.shape[1]] +
                                    cells[(row+1) % cells.shape[0], (col-1)% cells.shape[1]] +
                                    cells[(row+1) % cells.shape[0], col% cells.shape[1]] +
                                    cells[(row+1) % cells.shape[0], (col+1)% cells.shape[1]]
                                    )
                        color = myBackgroundcolor if cells[row, col]==0 else colorof_alive
                        if cells[row, col] == 1:
                                    if alive < 2 or alive > 3:
                                                if with_progress:
                                                            color = colorof_Die
                                    elif 2 <= alive <=3:
                                                cellsrefresh [row, col] = 1
                                                if with_progress:
                                                            color = colorof_alive
                        else:
                                    if alive==3:
                                                cellsrefresh[row, col]=1
                                                if with_progress:
                                                            color=colorof_alive
                        pygame.draw.rect(screen, color, (col * size, row * size, size -2, size 
-2 ))
            return cellsrefresh

def main():
        pygame.init()
        screen = pygame.display.set_mode((1000, 600))
        cells = mmj.zeros((30, 50))
        screen.fill(myColorofGrid)
        update(screen, cells, 20)

        pygame.display.flip()
        pygame.display.update()

        running = False
#Game loop(we will be asking to the keyboard)
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            return
                    elif event.type == pygame.KEYDOWN:
                            
                            if event.key == pygame.K_SPACE:
                                    running = not running
                                    update(screen, cells, 20)
                                    pygame.display.update()
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        cells[pos[1]//20, pos[0]//20] = 1
                        update(screen, cells, 20)
                        pygame.display.update()
            screen.fill(myColorofGrid)

            if running:
                    cells=update(screen, cells, 20, with_progress=True)
                    pygame.display.update()
            time.sleep(0.05)

if __name__ == '__main__':
            main()