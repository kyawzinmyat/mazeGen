from findpath import Dfs,Bfs, Gbfs
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
    
    maze = get_maze_list("maze2.csv")
    bfs = Bfs()
    bfs.set_maze(maze)
    bfs.solve(True, True)


    maze = get_maze_list("maze2.csv")
    dfs = Dfs()
    dfs.set_maze(maze)
    dfs.solve(False, True)

    maze = get_maze_list("maze2.csv")
    test = Gbfs()
    test.set_maze(maze)
    test.solve(False, True)

    #solve_maze()

    


