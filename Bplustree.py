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
	children = None
	def __init__(self):
		self.keys = list()
		self.values = list()
		self.size = 0
		
	def __init__(self, min, max):
		self.min = min
		self.max = max
		
	def add(self, key, value):
		for x in range(0, self.keys.size()):
			if(key[0] <= self.keys[x][0]):
				for y in range(x, self.keys.size()):
					if(key[1] <= self.keys[x][1]):
						if(key[0] == self.keys[x][0] && key[1] == self.keys[x][1]):
							self.values.pop(y).insert(value)
						self.values.insert(y, value)
						#missing cases if there's too many items
						#missing case handling if already exists and similar stuff for other functions
						
		return 0
	
	def splitNode(self):
		global filecounter
		newNode = Node()
		newNode.filename = str(filecounter)
		filecounter = filecounter+1
		if self.is_leaf:
			newNode.is_leaf = True
			mid = len(self.keys)/2
			midKey = self.keys[mid]
			# Update sibling parameters
			newNode.keys = self.keys[mid:]
			newNode.children = self.children[mid:]
			# Update node parameters
			self.keys = self.keys[:mid]
			self.children = self.children[:mid]
			# Update next node pointers
			newNode.next = self.next
			self.next = newNode.filename
		else:
			newNode.is_leaf = False
			mid = len(self.keys)/2
			midKey = self.keys[mid]
			# Update sibling parameters
			newNode.keys = self.keys[mid+1:]
			newNode.children = self.children[mid+1:]
			# Update node parameters
			self.keys = self.keys[:mid]
			self.children = self.children[:mid + 1]
		self.updateNode()
		newNode.updateNode()
		return midKey, newNode

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
		if(self.root == None):
			Node n = Node(1, self.d-1)
			n.add(key, value)
			root = n
		#find the right node to insert into
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