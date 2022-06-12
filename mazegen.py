import random


class Maze:
	def __init__(self,row=None,col=None):
		self.maze =[
		]
		self.wall ="#"
		self.space = " "
		if row and col:
			self.generate_maze(row, col)	
	
	def generate_maze(self,row,col):
		self.maze =[[Cell([i,j]) for j in range(col)]for i in range(row) ]
		self.maze_array =[[0 for j in range(3*col)]for i in range(3*row) ]
		self.dfs()
		self.convert_array()
	
	
	def dfs(self):
		self.visited_cells =[]
		self.visited_index = []	
		for i in range(len(self.maze)):
			for j in range(len(self.maze[0])):
				obj = self.maze[i][j]
				if obj not in self.visited_cells and [i,j] not in self.visited_index:
					self.visited_cells.append(obj)	
					self.visited_index.append([i,j])	
					#print(i,j)
					next_cell= self.connect_cell(obj)
					next_cell_obj = self.maze[next_cell[0]][next_cell[1]]
					next_cell_obj.wall[obj.op[next_cell[2]]]=False
					obj.wall[next_cell[2]]=False
				
					self._dfs(obj,self.maze[next_cell[0]][next_cell[1]])
				
	
	def _dfs(self,pre_cell,current_cell):
		self.visited_cells.append(current_cell)
		#print(current_cell.index_)
		self.visited_index.append(current_cell.index_)
		next_cell= self.connect_cell(current_cell)
		pre_cell.wall[next_cell[2]]=False
		current_cell.wall[current_cell.op[next_cell[2]]]=False
		if self.maze[next_cell[0]][next_cell[1]] not in self.visited_cells:
			self._dfs(current_cell,self.maze[next_cell[0]][next_cell[1]])
		return 		
		

	def connect_cell(self,cell_to_connect):
		next_cells = []
		for cell in self.get_index(cell_to_connect.index_):
				if cell not in self.visited_index:
					#print("cell",cell)
					next_cells.append(cell)
		return random.choice(next_cells)
		
			
		
		
	def print(self,custom_maze=None):
		for cells in self.maze_array:
			for cell in cells:
				print(cell,end="")
			print(end='\n')

	def get_index_of(self,node):
		for i,x in enumerate(self.maze):
			for j,y in enumerate(x):
				if y==node:
					return [i,j]
			
					
	def get_index(self,index):
		list_of_index=[]
		row_range=len(self.maze)
		col_range=len(self.maze[0])
		if index[0]+1<row_range:#down
				#if self.maze[index[0]+1][index[1]]==self.wall or self.maze[index[0]+1][index[1]]==self.stop:
					list_of_index.append([index[0]+1,index[1],"bottom"])
					#print(index,"bottom")
		
		if index[1]-1>=0:##left
			#if self.maze[index[0]][index[1]-1]== self.wall or self.maze[index[0]][index[1]-1]==self.stop: 
					#print(index,"left")
					list_of_index.append([index[0],index[1]-1,"left"])
					
		
		if index[0]-1>=0:#up
			#if self.maze[index[0]-1][index[1]]== self.wall or self.maze[index[0]-1][index[1]]==self.stop:
					list_of_index.append([index[0]-1,index[1],"top"])
					#print(index,"up")

		if index[1]+1<col_range:#right
			#if self.maze[index[0]][index[1]+1]==self.wall  or self.maze[index[0]][index[1]+1]==self.stop:
					list_of_index.append([index[0],index[1]+1,"right"])
					#print(index,"right")
									
		return list_of_index

	def convert_array(self):
		self.maze_array = []
		for index,cells in enumerate(self.maze):
			row = [self.wall for i in range(len(self.maze[0])*3)]
			row2 = [self.wall for i in range(len(self.maze[0])*3)]
			row3 = [self.wall for i in range(len(self.maze[0])*3)]
			for index2,cell in enumerate(cells):
				start = index2*3
				end = index2*3 +3
				mid = int((start+end)/2)
				
				row2[mid] = self.space
				self.remove_wall(start,mid,cell,row,row2,row3)
			self.maze_array.append(row)
			self.maze_array.append(row2)
			self.maze_array.append(row3)


	def remove_wall(self,start,mid,cell,row,row2,row3):
		if not cell.wall["left"]:

			row2[start]=self.space
		if not cell.wall["right"]:
			row2[start+2]=self.space
		if not cell.wall["top"]:
			row[mid]=self.space
		if not cell.wall['bottom']:
			row3[mid] =self.space

	
	def start(self,start,index):
		self.start = start
		self.maze_array[index[0]][index[1]] = self.start 

	def stop(self,stop,index):
		self.stop = stop
		self.maze_array[index[0]][index[1]] = self.stop
	
	def get_maze(self):
		return self.maze_array
	
	def load_maze_csv(self):
		with open("maze.csv","w+") as file:
			for cells in self.maze_array:
				for cell in cells:
					file.write(cell)
				file.write("\n")
		
		


				



			


class Cell:
	def __init__(self,index):
		self.x= index[0]
		self.y = index[1]
		self.index_ =index
		self.wall={
			"left":True,
			"right":True,
			"top":True,
			"bottom":True
		}	
		self.op={
			"left":"right",
			"right":"left",
			"top":"bottom",
			"bottom":"top"
		}			
						
								
												
		
#maze = Maze()
#maze.generate_maze(7,30)
#maze.print()
#maze.


##for cells in maze.maze:
##	for cell in cells:
##		print(cell.wall)