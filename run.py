from findpath import Dfs,Bfs
from mazegen import Maze



from csvtolist import get_maze_list

## generate maze
def gen_maze():
    maze = Maze()
    maze.generate_maze(20,20,[0,1],[1,10])
    maze.load_maze_csv("maze1.csv")
    #maze.print()
    return maze.get_maze()



def solve_maze(): 
    gen_maze()
    maze = get_maze_list('maze1.csv')
    dfs = Dfs()
    dfs.set_maze(maze)
    dfs.solve()
    dfs.maze.print()
    print(dfs.copy)
    return dfs.maze.maze





if __name__ == '__main__':
    
    maze = gen_maze()
    bfs = Bfs()
    bfs.set_maze(maze)
    bfs.solve()
    bfs.maze.print()
    #solve_maze()

    


