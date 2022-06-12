import csv

def get_maze_list():
	with open("maze.csv","r") as file:
		read = csv.reader(file)
		new =[]
		for line in read:				
			j= list(line[0])
			new.append(j)
	return new
