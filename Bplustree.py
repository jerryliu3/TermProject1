import sys
import bisect
import os.path
import time
import numpy
import csv

class Node:
	values  = 0
	def __init__(self):
		values = 0
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
	root = None;
	d = 0;
	table = list();
	
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
		for x in range(tid1, tid2): #need to add one to this
			#self.insert(self.table[x][0])
			return 0
	
	def printTree(self):
		return 0
	
	def insert(self, key, value):
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
		elif(choice == "quit"):
			break

if __name__ == "__main__": main()