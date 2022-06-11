import random


class Maze:
	def __init__(self):
		self.maze =[
		]
		self.wall ="■"	
		
	
	def generate_maze(self,row,col):
		self.maze =[[Cell([i,j]) for j in range(col)]for i in range(row) ]
		self.dfs()
	
	
	def dfs(self):
		self.visited_cells =[]	
		for i in range(len(self.maze)):
			for j in range(len(self.maze[0])):
				obj = self.maze[i][j]
				if obj not in self.visited_cells:
					self.visited_cells.append(obj)	
					#try:	
					next_cell= self.connect_cell(obj)
					next_cell_obj = self.maze[next_cell[0]][next_cell[1]]
					next_cell_obj.wall[obj.op[next_cell[2]]]=False
					obj.wall[next_cell[2]]=False
				
					self._dfs(obj,self.maze[next_cell[0]][next_cell[1]])
			#		except:
				#		pass
				
	
	def _dfs(self,pre_cell,current_cell):
		self.visited_cells.append(current_cell)
		next_cell= self.connect_cell(current_cell)
		pre_cell.wall[next_cell[2]]=False
		current_cell.wall[current_cell.op[next_cell[2]]]=False
		if self.maze[next_cell[0]][next_cell[1]] not in self.visited_cells:
			self._dfs(current_cell,self.maze[next_cell[0]][next_cell[1]])
		return 		
		

	def connect_cell(self,cell_to_connect):
		next_cell= random.choice(self.get_index(cell_to_connect.index_))
		return next_cell
		
			
		
		
	def print(self,custom_maze=None):
		maze = self.maze
		if custom_maze:
			maze = custom_maze
		
		for i in maze:
			k=""
			for j in i:
				k+="".join(j)
			print(k)
			
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
					print(index,"bottom")
		
		if index[1]-1>=0:##left
			#if self.maze[index[0]][index[1]-1]== self.wall or self.maze[index[0]][index[1]-1]==self.stop: 
					print(index,"left")
					list_of_index.append([index[0],index[1]-1,"left"])
					
		
		if index[0]-1>=0:#up
			#if self.maze[index[0]-1][index[1]]== self.wall or self.maze[index[0]-1][index[1]]==self.stop:
					list_of_index.append([index[0]-1,index[1],"top"])
					print(index,"up")
		if index[1]+1<col_range:#right
			#if self.maze[index[0]][index[1]+1]==self.wall  or self.maze[index[0]][index[1]+1]==self.stop:
					list_of_index.append([index[0],index[1]+1,"right"])
					print(index,"right")
									
		return list_of_index

		
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
						
								
												
		
maze = Maze()
maze.generate_maze(4,4)
#maze.

for i in maze.maze:
	k = [j.wall for j in i]
	print(k)


