import csv

def get_maze_list(maze_file = None):


	maze_file_ = "maze.csv"
	if maze_file:
		maze_file_ = maze_file
	with open(maze_file_,"r") as file:
		read = csv.reader(file)
		new =[]
		for line in read:				
			j= list(line[0])
			new.append(j)
	return new
