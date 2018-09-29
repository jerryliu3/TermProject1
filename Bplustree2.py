import sys
import bisect
import os.path
import time
import numpy
import csv

class Node:
	#based on the value of d
	min = 0
	max = 0
	def __init__(self):
		self.keys = list()
		self.values = list()
		self.size = 0
		self.leaf = True
		self.connection = None
		
	def __init__(self, min, max):
		self.min = min
		self.max = max
		
	def add(self, key, value):
		for x in range(0, len(self.keys)):
			if(key[0] < self.keys[x][0]):
				self.keys.insert(x, key)
				temp = list()
				temp.append(value)
				self.values.insert(x, temp)
			if(key[0] == self.keys[x][0]):
				for y in range(x, len(self.keys)):
					if(key[1] <= self.keys[x][1]):
						if(key[0] == self.keys[x][0] && key[1] == self.keys[x][1]):
							temp = self.values[y]
							for z in range(0, len(temp)):
								if(value < temp[z]):
									self.values[y].insert(z, value)
									return 0
							self.values[y].append(z, value)
							return 0
						else:
							self.keys.insert(y, key)
							temp = list()
							temp.append(value)
							self.values.insert(y, temp)
							return 0
				if(x < len(self.keys)-1):
					self.keys.insert(x+1, key)
					temp = list()
					temp.append(value)
					self.values.insert(x+1, temp)
					return 0
			
		self.keys.append(key)
		temp = list()
		temp.append(value)
		self.values.append(temp)
			
		return 0

class BPlusTree:

	root = None
	d = 0
	table = list()
	
	#currently setting up to be exactly like the example so that functions can be tested
	#current keys are rating and date
	key1 = 3
	key2 = 4
	
	def __init__(self):
		
		self.d = 3 #3 or 4
		table = list()
		#root node must have 1 to d-1 key value pairs
		#other nodes must have d/2 - 1 to d-1 key value pairs

	def load(self, filename, tid1, tid2):
	
		with open(filename) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				print(row)
				self.table.append(row)
				#for x in row:
				#print(x)
		for x in range(tid1, tid2 + 1):
			#self.insert(self.table[x][0])
			return 0
	
	def printTree(self):
		#just use a queue that goes through the node's children
		return 0
	def printTable(self):
		for x in self.table:
			#print(x)
			for y in x:
				#print("test", end = '')
				#print(self.table[x][y], end = '')
				print(y, end = ', ')
			print()
		return 0
	def insert(self, tid):
		key = [self.table[tid][key1], self.table[tid][key2]]
		value = tid
		stack = list()
		current = self.root
		#added this but not sure if this is required or already taken into consideration
		if(current == None):
			Node n = Node(1, self.d-1)
			n.add(key, value)
			root = n
			return 0
		while(!current.leaf):
			stack.append(current)
			q = current.keys
			first = 0
			last = len(q)-1
			if(key[0] < q[first][0] || key[0] == q[first][0] && key[1] <= q[first][1]):
				current = current.values[first]
			elif(key[0] > q[last][0] || key[0] == q[last][0] && key[1] <= q[last][1]):
				current = current.values[last+1]
			else:			
				for x in range(1, len(q)):
					#not fully optimized, but written this way for clearer organization
					if(key[0] > q[x-1][0]):
						if(key[0] < q[x][0] || key[0] == q[x][0] && key[1] <= q[x][1]):
							current = current.values[x]
					elif(key[0] == q[x-1][0] && key[1] > q[x-1][1]):
						if(key[0] < q[x][0] || key[0] == q[x][0] && key[1] <= q[x][1]):
							current = current.values[x]
		keys = current.keys
		values = current.values
		size = len(keys)
		for x in range(0, size):
			if(key[0] == keys[x][0] && key[1] == keys[x][1]):
				if(value not in values[x]):
					if(current.size < current.max):
						current.add(key, value)
					else:
						#split
				
		#create new key and value
		if(current.size < current.max):
			current.add(key, value)
		else:
			temp = current
			temp.add(key, value)
			newNode = Node(1, self.d-1)
			newNode.connection = current.connection
			j = (self.d+1)/2
			for(x in range(0, j)):
				#insert into current
			current.connection = newNode
			for(x in range(j, temp.size())):
				#insert into temp??
			key = current.keys[j-1]
			finished = False
			while(!finished):
				depth = len(stack)
				if(depth == 0):
					
					#no parent node, create root 
					finished = True
				else:
					current = stack.pop()
					if(current.size < current.max):
						current.add(key, value)
						finished = True
					else:
						temp = current
						temp.add(key, value)
						newNode = Node(1, self.d-1)
						newNode.connection = current.connection
						j = (self.d+1)/2
						for(x in range(0, j)):
							#insert into current
						current.connection = newNode
						for(x in range(j, temp.size())):
							#insert into temp??
						key = current.keys[j-1]
					
		return 0
	def delete(self, tid):
		return 0

	def search(self, key):
		all_keys = []
		all_values = []
		start_leaf = self.tree_search_for_query(key, self.root)
		keys, values, next_node = self.get_data_in_key_range(key, key, start_leaf)
		all_keys += keys
		all_values += values
		while next_node:
			keys, values, next_node = self.get_data_in_key_range(key, key, Node(next_node.filename))
			all_keys += keys
			all_values += values
		return all_keys, all_values
		
		# Function: search (k)
  # return tree_search (k, root);
 
# Function: tree_search (k, node)
  # if node is a leaf then
    # return node;
  # switch k do
  # case k ≤ k_0
    # return tree_search(k, p_0);
  # case k_i < k ≤ k_{i+1}
    # return tree_search(k, p_{i+1});
  # case k_d < k
    # return tree_search(k, p_{d});

	def range_search(self, keyMin, keyMax):
		all_keys = []
		all_values = []
		start_leaf = self.tree_search_for_query(keyMin, self.root)
		keys, values, next_node = self.get_data_in_key_range(keyMin, keyMax, start_leaf)
		all_keys += keys
		all_values += values
		while next_node:
			keys, values, next_node = self.get_data_in_key_range(keyMin, keyMax, Node(next_node.filename))
			all_keys += keys
			all_values += values
		return all_keys, all_values
		
def main():
	tree = BPlusTree()
	while(1):
		choice = input("What do you want to do: ")
		if(choice == "load"):
			filename = input ("File name: ")
			tid1 = int(input ("First tuple id: "))
			tid2 = int(input ("Second tuple id: "))
			tree.load(filename, tid1, tid2)
		if(choice == "print table"):
			tree.printTree()
			#print the table
		elif(choice == "print"):
			tree.printTable()
		elif(choice == "quit"):
			break

if __name__ == "__main__": main()