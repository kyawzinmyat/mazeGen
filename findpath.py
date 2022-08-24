
from collections import deque
from maze import Maze	
from heapq import heapify, heappop, heappush 


class Node:

	def __init__(self,parent,index,state):
		self.parent = parent
		self.index = index
		self.state = state
		

class StackFrointer:
	
	def __init__(self):
		self.frointer = []
	
	def push(self, node):
		self.frointer.append(node)
	
	def remove(self):
		return self.frointer.pop()
	

class QueueFrointer(StackFrointer):
	def __init__(self):
		self.frointer = deque()

	def remove(self):
		return self.frointer.popleft()


class PQueueFrointer(StackFrointer):

	def push(self, node):
		heappush(self.frointer, node)
	
	def remove(self):
		return heappop(self.frointer)



class Solve:
	

	def __init__(self, frointer, maze = None):
		self.frointer = frointer
		self.maze = Maze()
		self.visited=[]
		self.nodelist =[]
		self.mark="*"
		
		

	def traverse(self,fill, exp):
		self.explored = 0
		self.frointer.push(self.maze.get_index_of(self.maze.start))
		self.nodelist.append(Node(None,self.maze.get_index_of(self.maze.start),self.maze.start))  # append start node		
		while self.frointer:
			current_index = self.frointer.remove()  # is in list form 
			self.visited.append(current_index)
			if exp:
				self.explored += 1 
			if self.check_is_end(current_index,fill):
				if exp:
					print(self.explored)
				return True
			for adj_index in self.maze.get_index(current_index,shuffle = True):
				if  adj_index not in self.visited and adj_index not in self.frointer.frointer:

					self.nodelist.append(Node(current_index,adj_index,"_"))	

					self.frointer.push(adj_index)
		return False


	def set_maze(self,new_maze):

		self.maze.maze=new_maze		


	def set_maze_obj(self, new_maze_obj):
		self.maze = new_maze_obj	
					

	def check_is_end(self,current_index,fill):
		if  self.maze.maze[current_index[0]][current_index[1]] ==self.maze.stop:## [0] is x [1] is y
			return self.get_path(fill)			
		return False
		

	def solve(self,fill=True, exp = False):
		return self.traverse(fill, exp)
					

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
		self.index_list = index_list
		return True
	
	def get_indexlist(self):
		try:
			return self.index_list
		except:
			return False

	# its show all the space explored

	def get_full(self):
		temp = self.maze.maze[:]

		for i in self.visited:

			temp[i[0]][i[1]]="☆"




class Dfs(Solve):
	def __init__(self):
		super().__init__(StackFrointer())

class Bfs(Solve):
	def __init__(self):
		super().__init__(QueueFrointer())

class Gbfs(Solve):
	def __init__(self):
		super().__init__(PQueueFrointer())
		
	def traverse(self,fill, exp):
		self.stop_x, self.stop_y = self.maze.get_index_of(self.maze.stop)
		self.explored = 0
		self.frointer.push([0, self.maze.get_index_of(self.maze.start)])
		self.nodelist.append(Node(None,self.maze.get_index_of(self.maze.start),self.maze.start))  # append start node		
		while self.frointer:
			current_index = self.frointer.remove()  # is in [m_dis [x, y]]
			self.visited.append(current_index[1])
			if exp:
				self.explored += 1
			if self.check_is_end(current_index[1], fill):
				if exp:
					print(self.explored)
				return True
			for adj_index in self.maze.get_index(current_index[1],shuffle = False):
				if  adj_index not in self.visited:
					m_dis = abs(self.stop_x - adj_index[0]) + abs(self.stop_y - adj_index[1])
					if [m_dis, adj_index] not in self.frointer.frointer:
						self.nodelist.append(Node(current_index[1],adj_index,"_"))	
						self.frointer.push([m_dis, adj_index])
		return False

	
class Astar(Solve):
	def __init__(self):
		super().__init__(PQueueFrointer())
		
	def traverse(self,fill, exp):
		self.stop_x, self.stop_y = self.maze.get_index_of(self.maze.stop)
		self.explored = 0
		self.level = {tuple(self.maze.get_index_of(self.maze.start)) : 0}
		self.frointer.push([0, self.maze.get_index_of(self.maze.start)])
		self.nodelist.append(Node(None,self.maze.get_index_of(self.maze.start),self.maze.start))  # append start node		
		while self.frointer:
			current_index = self.frointer.remove()  # is in [m_dis [x, y]]
			self.visited.append(current_index[1])
			if exp:
				self.explored += 1
			if self.check_is_end(current_index[1], fill):
				if exp:
					print(self.explored)
				return True
			for adj_index in self.maze.get_index(current_index[1],shuffle = False):
				if  adj_index not in self.visited:
					# g_h = herustic + steps
					level = self.level[tuple(current_index[1])] + 1 #level is calculated based on the current node
					g_h = abs(self.stop_x - adj_index[0]) + abs(self.stop_y - adj_index[1]) + (level)
					if [g_h, adj_index] not in self.frointer.frointer:
						self.level[tuple(adj_index)] = level
						self.nodelist.append(Node(current_index[1],adj_index,"_"))	
						self.frointer.push([g_h, adj_index])
			heapify(self.frointer.frointer)
		return False
			
m = [
	["#"," "," "," "," "," "," "," "," "," "," ","E"],
	["#"," ","#","#","#","#","#","#","#","#","#"," "],
	["#"," ","#"," "," "," "," "," "," "," ","#"," "],
	["#"," ","#"," ","#","#","#","#","#"," ","#"," "],
	["#"," "," "," ","#"," "," "," "," "," ","#"," "],
	["#","#","#"," ","#"," ","#","#","#","#","#"," "],
	["A"," "," "," ","#"," "," "," "," "," "," "," "]
]



test = Astar()
test.set_maze(m)
test.solve(True, True)
print(test.level)
for i in test.maze.maze:
	print(i)