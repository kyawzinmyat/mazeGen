import random
from collections import deque
from csvtolist import get_maze_list
from findpath import Dfs

class Maze:
	def __init__(self,row=None,col=None):
		self.maze =[
		]
		self.wall ="#"
		self.space = " "
		self.visited_cells =[]
		self.visited_index = []	
		if row and col:
			self.generate_maze(row, col)
		self.dfs = Dfs()
		
	
	def generate_maze(self,row,col,seed = None , end = None,fill = True):
		self.maze =[[Cell([i,j]) for j in range(col)]for i in range(row) ]
		self.maze_array =[[0 for j in range(3*col)]for i in range(3*row) ]
		self.dfs2(seed,end)
		self.convert_array()
		counter = 0
		if seed and end:
			self.maze_array[seed[0]*3+1][seed[1]*2+1] = 'A'
			self.maze_array[(end[0])*3-1][end[1]*3-2] = 'E'
			self.dfs.set_maze(self.maze_array[:])
			while not self.dfs.solve(fill=False):		
				self.dfs2(seed,end)
				self.convert_array()
				self.maze_array[seed[0]*3+1][seed[1]*2+1] = 'A'
				self.maze_array[(end[0])*3-1][end[1]*3-2] = 'E'
				counter +=1
				if counter > 100:
					break
		
		return
	
	
	def dfs1(self):
		for i in range(len(self.maze)):
			for j in range(len(self.maze[0])):
				obj = self.maze[i][j]
				if obj not in self.visited_cells and [i,j] not in self.visited_index and [i,j] not in self.visited_index:
					self.visited_cells.append(obj)	
					self.visited_index.append([i,j])	
					#print("current cell",i,j)
					next_cell= self.connect_cell(obj)
					next_cell_obj = self.maze[next_cell[0]][next_cell[1]]
					obj.wall[next_cell[2]]=False
					next_cell_obj.wall[obj.op[next_cell[2]]]=False
					#print(obj.wall)
				
					self._dfs(obj,next_cell_obj)
				
	
	def _dfs(self,pre_cell,current_cell):
		self.visited_cells.append(current_cell)
		#print("current cell",current_cell.index_)
		self.visited_index.append(current_cell.index_)
		next_cell= self.connect_cell(current_cell)
		pre_cell.wall[next_cell[2]]=False
		current_cell.wall[current_cell.op[next_cell[2]]]=False
		#print(current_cell.wall)
		if self.maze[next_cell[0]][next_cell[1]] not in self.visited_cells and next_cell not in self.visited_index:
			self._dfs(current_cell,self.maze[next_cell[0]][next_cell[1]])
			#print("next cell",next_cell)
		return 		
		

	def connect_cell(self,cell_to_connect):
		next_cells = []
		for cell in self.get_index(cell_to_connect.index_):
				if cell not in self.visited_index:
					#print("cell",cell)
					next_cells.append(cell)
		return random.choice(next_cells)

	def get_neigh(self,cell_to_connect):
		cells = []
		for cell in self.get_index(cell_to_connect.index_):
				if cell not in self.visited_index:
					#cells.append(cell)
		#random.shuffle(cells)
		#for cell in cells:
		#		print(cell)			
					self.stack.appendleft(cell)

		

	def dfs2(self,seed = None,end=None):
		self.stack = deque()
		self.stack.appendleft([0,0,None])
		if seed:
			seed.append(None)
			self.stack.popleft()
			self.stack.appendleft(seed)
		self.visited_index=[]
		self.visited_cells = []
		prev =None
		while self.stack:
			current_index = self.stack.popleft()
			current_cell = self.maze[current_index[0]][current_index[1]]
			if end and  current_index[0] == end[0] and current_index[1] == end[1]:
				self.dfs2()
				break
			if current_cell not in self.visited_cells: #and current_index not in self.visited_index:
				#print(current_index)
				self.visited_cells.append(current_cell)
				self.visited_index.append(current_index)
				if current_index[2]:
					current_cell.wall[current_cell.op[current_index[2]]] = False
				if prev:
					prev.wall[current_index[2]]= False
				self.get_neigh(current_cell)
				prev=current_cell

				
			



			



		
			
		
		
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
									
		random.shuffle(list_of_index)
		return list_of_index


	def convert_array(self):
		self.maze_array = [[self.wall for i in range(len(self.maze[0]*3))]]
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
	
	def load_maze_csv(self,filename = None):
		
		if not filename:
			filename = "MAZE.CSV"
		with open(filename,"w+") as file:
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
						
								
												
##		

#maze.


##for cells in maze.maze:
##	for cell in cells:
##		print(cell.wall)