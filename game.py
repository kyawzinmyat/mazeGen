import pygame
from mazegen import Maze
from findpath import Dfs,Bfs,Gbfs,Astar
import random
from csvtolist import get_maze_list
import time


pygame.init()

max_width = 1500
max_height = 800
start = False
e_s = 0 # numbers of explored state
p_l = 0 # lengths of path

#screen = pygame.display.set_mode((max_width,max_height))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

global row
row = 10

global col
col = 10

def generate():
    try:
        reset_pl_es()
        maze = Maze()
        start = [random.randrange(row),random.randrange(col)]
        end = [random.randrange(row),random.randrange(col)]
        maze.generate_maze(row,col,start,end)
        maze.load_maze_csv("maze2.csv")
        maze = maze.get_maze()
        draw_rect(maze)
        return 
    except:
        return




def draw_rect(maze,show=False):
    maze_row = len(maze)-1
    maze_col = len(maze[0])
    cell_height = int((max_height-100)/ maze_row)
    padding_width = int((max_width - max_height)/3)
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
            
            pygame.draw.rect(screen,color,(index2*cell_width+padding_width,index*cell_height+50,cell_height,cell_width),width=width)



def draw_rect_by_indecies(list_of_indices,maze, delay = 100, color = None, increment_state = False):
    draw_rect(maze,show=False)
    maze_row = len(maze)-1
    maze_col = len(maze[0])
    cell_height = int((max_height-100)/ maze_row)
    padding_width = int((max_width - max_height)/3)
    cell_width = cell_height -1
    is_break = False
    global e_s
    e_s = 0
    while not is_break:
        for index in list_of_indices:
            if maze[index[0]][index[1]] != "A" and maze[index[0]][index[1]] != 'E':
                if not color:
                    color = (100,0,255,255)
                width = 0
                pygame.draw.rect(screen,color,(index[1]*cell_width+padding_width,index[0]*cell_height+50,cell_height,cell_width),width=width)
                if increment_state:
                    e_s += 1
                    set_state(e_s)
                pygame.time.delay(delay)
                pygame.display.update()
    
        is_break = True
        pygame.time.delay(1000)





def reset_pl_es():
    global e_s
    global p_l
    e_s, p_l =0, 0

def set_pl_es(es, pl):
    global e_s
    global p_l
    e_s, p_l =es, pl


def new_find_path(algo_obj, show = False):
    try:
        maze = get_maze_list('maze2.csv')
        algo_obj.set_maze(maze)
        algo_obj.solve(fill = True, exp=True)
        if show:
            draw_rect_by_indecies(algo_obj.visited, maze, 100, (233,0,230,50), True)
        path_index_list = algo_obj.get_indexlist()[::-1]
        draw_rect_by_indecies(path_index_list, maze)
        reset_pl_es()
        set_pl_es(algo_obj.explored - 1, len(path_index_list))

    except:
        pass
    
 

def check_mouse(x,y,width,height):
    pos = pygame.mouse.get_pos()
    if pos[0] >= x and pos[0]<= height+x:
        if pos[1] >= y and pos[1]<=width+y:
            return True
        return False
    return False



def set_state(states = 0, length = 0):
    global font
    font = pygame.font.SysFont('Arial', 15)
    but_states = pygame.draw.rect(screen,"#00ffff", (1190, 100, 200, 100))
    screen.blit(font.render('Explored States', True, (0, 0, 0, 100)), (1240, 113))
    font = pygame.font.SysFont('Arial', 30)
    screen.blit(font.render(str(states), True, (0, 0, 0, 100)), (1280, 150))

    font = pygame.font.SysFont('Arial', 15)
    but_states = pygame.draw.rect(screen,"#00ffff", (1190, 230, 200, 100))
    screen.blit(font.render('Path length', True, (0, 0, 0, 100)), (1240, 240))
    font = pygame.font.SysFont('Arial', 30)
    screen.blit(font.render(str(length), True, (0, 0, 0, 100)), (1280, 270))



### actual width = 1000
### padding 200

## actuall height 



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    font = pygame.font.SysFont('Arial', 15)
    
    but_gen = pygame.draw.rect(screen,"#16e0bd", (1000, 200, 150, 50))
    screen.blit(font.render('Generate new maze',True,(0, 0, 0, 100)), (1010, 213))

    but_dfs = pygame.draw.rect(screen,"#16e0bd", (1000, 300, 150, 50))
    screen.blit(font.render('Show path(DFS)',True,(0, 0, 0, 100)), (1020, 315))

    but_bfs = pygame.draw.rect(screen,"#16e0bd", (1000, 400, 150, 50))
    screen.blit(font.render('Show path(BFS)',True,(0, 0, 0, 100)), (1025, 415))

    but_bfs_show = pygame.draw.rect(screen,"#16e0bd", (1000, 500, 150, 50))
    screen.blit(font.render('Show path(DFS)2',True,(0, 0, 0, 100)), (1020, 515))

    but_bfs_show = pygame.draw.rect(screen,"#16e0bd", (1000, 600, 150, 50))
    screen.blit(font.render('Show path(BFS)2',True,(0,0,0,100)), (1025,615))

    but_gbfs = pygame.draw.rect(screen,"#16e0bd", (1000, 700, 150, 50))
    screen.blit(font.render('Show path(GBFS)',True,(0, 0, 0, 100)), (1015, 715))

    but_gbfs_show = pygame.draw.rect(screen,"#16e0bd", (1200, 400, 150, 50))
    screen.blit(font.render('Show path(GBFS)2',True,(0, 0, 0, 100)), (1205, 415))

    but_astar = pygame.draw.rect(screen,"#16e0bd", (1200, 500, 150, 50))
    screen.blit(font.render('Show path(A*)',True,(0, 0, 0, 100)), (1215, 515))

    but_astar_show = pygame.draw.rect(screen,"#16e0bd", (1200, 600, 150, 50))
    screen.blit(font.render('Show path(A*)2',True,(0, 0, 0, 100)), (1215, 615))

    but_quit = pygame.draw.rect(screen,"#ff0000", (1000, 100, 150, 50))
    screen.blit(font.render('Exit ?',True,(0, 0, 0, 50)), (1035, 113))


    set_state(states=e_s, length=p_l)

    
    ### show path
    if check_mouse(1000,300,50,150):
        pygame.draw.rect(screen,"#00ff00", (1000,300,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            new_find_path(Dfs())

    
    elif check_mouse(1000, 400,50,150):
        pygame.draw.rect(screen,"#00ff00", (1000,400,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            #show_path_bfs()
            new_find_path(Bfs())
    
    elif check_mouse(1000,500,50,150):
        pygame.draw.rect(screen,"#00ff00", (1000,500,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            new_find_path(Dfs(), True)

    
    elif check_mouse(1000, 600,50,150):
        pygame.draw.rect(screen,"#00ff00", (1000,600,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            new_find_path(Bfs(), True)

    elif check_mouse(1000, 700,50,150):
        pygame.draw.rect(screen,"#00ff00", (1000,700,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            new_find_path(Gbfs())

    elif check_mouse(1200, 400,50,150):
        pygame.draw.rect(screen,"#00ff00", (1200,400,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            new_find_path(Gbfs(), True)
    elif check_mouse(1200, 500,50,150):
        pygame.draw.rect(screen,"#00ff00", (1200,500,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            new_find_path(Astar())
    elif check_mouse(1200, 600,50,150):
        pygame.draw.rect(screen,"#00ff00", (1200,600,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            new_find_path(Astar(), True)

    ##### gen  new maze
    elif check_mouse(1000,200,50,150):
        start = True
        pygame.draw.rect(screen,"#00ff00", (1000,200,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            generate()

    elif check_mouse(1000, 100,50,150):
        pygame.draw.rect(screen,"#00ff00", (1000,100,150,50),width=3)
        if pygame.mouse.get_pressed()[0] == 1:
            running = False

        
    if not True:
        font2 = pygame.font.SysFont('Arial',20)
        
    pygame.display.update()