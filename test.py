from findpath import Dfs,Bfs, Gbfs, Astar
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
    
    print("A*")
    test = Astar()
    test.set_maze(maze)
    test.solve(False, True)

    print("BFS")
    bfs = Bfs()
    bfs.set_maze(maze)
    bfs.solve(False, True)


    print("DFS")
    dfs = Dfs()
    dfs.set_maze(maze)
    dfs.solve(False, True)

    print("GBFS")
    gbfs = Gbfs()
    gbfs.set_maze(maze)
    gbfs.solve(False, True)

    #solve_maze()

    
if __name__ == "__main__":
    solve_maze()

