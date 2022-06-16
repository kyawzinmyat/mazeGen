

from maze import Maze	



class Node:

	def __init__(self,parent,index,state):
		self.parent = parent
		self.index = index
		self.state = state
		



class Dfs:
	

	def __init__(self,maze = None):
		self.frointer=[]
		self.maze = Maze()
		self.visited=[]
		self.nodelist =[]
		self.mark="*"
		
		

		

	def traverse(self,fill):

		self.frointer = [self.maze.get_index_of(self.maze.start)]

		self.nodelist.append(Node(None,self.maze.get_index_of(self.maze.start),self.maze.start))  # append start node		

		while self.frointer:

			current_index = self.frointer.pop()  # is in list form 

			self.visited.append(current_index) 

			if self.check_is_end(current_index,fill):
				return True
			
				

			for adj_index in self.maze.get_index(current_index):

				if  adj_index not in self.visited and adj_index not in self.frointer:

					self.nodelist.append(Node(current_index,adj_index,"_"))	

					self.frointer.append(adj_index)
		return False

	def set_maze(self,new_maze):

		self.maze.maze=new_maze				
					

	def check_is_end(self,current_index,fill):
		#print(self.maze.maze[current_index[0]][current_index[1]])
		if  self.maze.maze[current_index[0]][current_index[1]] ==self.maze.stop:## [0] is x [1] is y
			print("found")
			return self.get_path(fill)			

		return False
		

	def solve(self,show_full=False,fill=True):

		return self.traverse(fill)

		if show_full:

			print("_________")

			self.get_full()

			print("_________")
			
	
					

	## find the actual path and make a list of index of that path

	def  get_path(self,fill):
		current=[]

		parent =None

		end = self.maze.get_index_of(self.maze.stop)		

		k = self.extract_index()

		for node in reversed(k):

			if node[0] == end:

				current.append(node[0])
				if not parent:

					parent= node[1]

			elif node[0] == parent:

				current.append(node[0])

				parent = node[1]

		return self.fill_path(current,fill)

	

	## node list store node obj its has current and parent index and return the list of that pair		
	def extract_index(self):

		k=[]
		for node in self.nodelist:

			k.append([node.index,node.parent])

		return k
				
	

	# take the list of index of actual path and fill with char	

	def fill_path(self,index_list,fill):
		if fill:
			for i in index_list:

				if self.maze.maze[i[0]][i[1]]==self.maze.blank:

					self.maze.maze[i[0]][i[1]]=self.mark
		#self.maze.print()
		return True
	

	# its show all the space explored

	def get_full(self):
		temp = self.maze.maze[:]

		for i in self.visited:

			temp[i[0]][i[1]]="☆"
		self.maze.print(temp)
			
		
			

#			

#d = Dfs()

#d.traverse()

#d.get_full()

