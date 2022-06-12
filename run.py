from findpath import Dfs
from mazegen import Maze

maze = Maze(7,30)


#maze.print()

# you need to change through maze.csv

#maze.load_maze_csv()
#maze = maze.get_maze()

from csvtolist import get_maze_list


maze = get_maze_list()





dfs = Dfs()
dfs.set_maze(maze)
dfs.solve()
dfs.maze.print()

