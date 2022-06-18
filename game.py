import pygame
from mazegen import Maze
from findpath import Dfs,Bfs
import random
from csvtolist import get_maze_list



pygame.init()


def generate():
    try: 
        maze = Maze()
        start = [random.randrange(row),random.randrange(col)]
        end = [random.randrange(row),random.randrange(col)]
        maze.generate_maze(row,col,start,end)
        maze.load_maze_csv("maze2.csv")
        maze = maze.get_maze()
        draw_rect(maze)
    except:
        pass




def draw_rect(maze,show=False):
    maze_row = len(maze)-1
    maze_col = len(maze[0])
    cell_height = int((max_height-20)/ maze_row)
    padding_width = int((max_width - max_height)/2)
    cell_width = cell_height -1
    for index,row in enumerate(maze):
        for index2,col in enumerate(row):   
            color = (10,10,10,10)
            width = 0
            if col == '#':
                color = (254,254,254,0)
                width = 0
            elif col == 'A':
                color = (255,0,0,0)
                width = 0
            elif col == 'E':
                color = (0,255,0,0)
                width = 0
            if show:
                if col == '*':
                    color = (100,0,255,255)
                    width = 0
            
            pygame.draw.rect(screen,color,(index2*cell_width+padding_width,index*cell_height+8,cell_height,cell_width),width=width)

def show_path_dfs():
    try:
        maze = get_maze_list('maze2.csv')
        dfs = Dfs()
        dfs.set_maze(maze)
        dfs.solve()
        draw_rect(dfs.maze.maze,True)
    except:
        pass

def show_path_bfs():
    try:
        maze = get_maze_list('maze2.csv')
        dfs = Bfs()
        dfs.set_maze(maze)
        dfs.solve()
        draw_rect(dfs.maze.maze,True)
    except:
        pass
    
 

def check_mouse(x,y,width,height):
    pos = pygame.mouse.get_pos()
    if pos[0] >= x and pos[0]<= height+x:
        if pos[1] >= y and pos[1]<=width+y:
            return True
        return False
    return False






### actual width = 1000
### padding 200

## actuall height 
max_width = 1200
max_height = 660
start = False

screen = pygame.display.set_mode((max_width,max_height))

global row
row = 20

global col
col = 20


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    font = pygame.font.SysFont('Arial', 15)
    
    but_gen = pygame.draw.rect(screen,"#16e0bd", (1000,200,150,50))
    screen.blit(font.render('Generate new maze',True,(0,0,0,100)), (1015,213))
    but_dfs = pygame.draw.rect(screen,"#16e0bd", (1000,300,150,50))
    screen.blit(font.render('Show path(DFS)',True,(0,0,0,100)), (1020,315))
    but_bfs = pygame.draw.rect(screen,"#16e0bd", (1000,400,150,50))
    screen.blit(font.render('Show path(BFS)',True,(0,0,0,100)), (1025,415))
    
    ### show path
    if check_mouse(1000,300,50,150):
        pygame.draw.rect(screen,"#00ff00", (1000,300,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            show_path_dfs()

    ##### gen  new maze
    elif check_mouse(1000,200,50,150):
        start = True
        pygame.draw.rect(screen,"#00ff00", (1000,200,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            generate()
    
    elif check_mouse(1000, 400,50,150):
        pygame.draw.rect(screen,"#00ff00", (1000,400,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            show_path_bfs()


        
    if not True:
    #pygame.draw.rect(screen,"#16e0bd",(230,140,700,200))
        font2 = pygame.font.SysFont('Arial',20)
        screen.blit(font2.render("This program use Dfs to find the path ",True,(50,0,0,0)),(350,250))
        screen.blit(font2.render("So this algorithm will give the path ",True,(50,0,0,0)),(360,280))
        screen.blit(font2.render("But not the optimized one",True,(50,0,0,0)),(390,310))
        
        
        
    
    pygame.display.update()