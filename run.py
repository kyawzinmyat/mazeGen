from findpath import Dfs
from mazegen import Maze



from csvtolist import get_maze_list

## generate maze
def gen_maze():
    maze = Maze()
    maze.generate_maze(10,10,[0,1],[1,10])
    maze.load_maze_csv()
    #maze.print()
    return maze.get_maze()



def solve_maze(): 
    gen_maze()
    maze = get_maze_list('maze.csv')
    dfs = Dfs()
    dfs.set_maze(maze)
    dfs.solve()
    dfs.maze.print()
    print(dfs.copy)
    return dfs.maze.maze





#if __name__ == '__main__':
    
    #gen_maze()
    #solve_maze()

    


