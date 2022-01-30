import pygame, random

width, height = 1280, 720 #width and height for the window in pixels
resolution = 10 #size of one square of the grid
cols, rows = width//resolution, height//resolution #number of columns and rows in the grid

def create_grid(rand=False):
    'Creates a new grid with either random values or zeros for the cells'
    grid = [[0 for i in range(cols+2)] for j in range(rows+2)]
    if rand:
        for i in range(1, cols+1):
            for j in range(1, rows+1):
                grid[j][i] = round(random.random())
    return grid

def draw_grid(screen, grid):
    'Draws the grid on the screen'
    screen.fill((255, 255, 255))
    #Draws a white cell for value 0 and and black cell for value 1
    #The first and last rows and columns won't be drawn
    for i in range(1, cols+1):
        for j in range(1, rows+1):
            rect = pygame.Rect((i-1)*resolution, (j-1)*resolution, resolution, resolution)
            if grid[j][i] == 1:
                pygame.draw.rect(screen, (0, 0, 0), rect) #fully black cell
            else:
                pygame.draw.rect(screen, (200, 200, 200), rect, 1) #only grey borders aka white cell

def check_neighbours(row, col, grid):
    'Checks the number of alive neighbours'
    alive = -grid[row][col] #The cell to be checked won't be counted as alive
    for i in range(col-1, col+2):
        for j in range(row-1, row+2):
            if grid[j][i] == 1:
                alive += 1
    return alive

def update_grid(grid):
    'Creates a new updated grid according to the rules'
    new_grid = create_grid()
    for i in range(1, cols+1):
        for j in range(1, rows+1):
            alive = check_neighbours(j, i, grid)
            if grid[j][i] == 1 and (alive == 2 or alive == 3):
                new_grid[j][i] = 1
            elif grid[j][i] == 0 and alive == 3:
                new_grid[j][i] = 1
    return new_grid

def main():
    'Initialize pygame and start main loop'
    pygame.init()
    pygame.display.set_caption("Game of Life")

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    running = True
    grid = create_grid(rand=True) #grid with random values

    while running:
        clock.tick(30) #Loop runs 30 times a second

        draw_grid(screen, grid) #draw current grid
        pygame.display.update() 

        grid = update_grid(grid) #udpate to new grid
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                grid = create_grid(rand=True) #Clicking any mouse button creates a new random grid

if __name__ == '__main__':
    main()