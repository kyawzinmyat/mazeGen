from findpath import Dfs
from mazegen import Maze


from csvtolist import get_maze_list

## generate maze
def gen_maze():
    maze = Maze()
    maze.generate_maze(20,20,[0,1],[20,10])
    maze.load_maze_csv()
    #maze.print()



def solve_maze(): 
    gen_maze()
    maze = get_maze_list('maze.csv')
    dfs = Dfs()
    dfs.set_maze(maze)
    dfs.solve()

if __name__ == '__main__':
    solve_maze()


