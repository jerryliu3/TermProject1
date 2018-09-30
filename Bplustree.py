import sys
import bisect
import os.path
import time
import numpy
import csv
import copy
class Node:
	#based on the value of d
	min = 0
	max = 0
	def __init__(self):
		self.keys = list()
		self.values = list()
		self.leaf = True
		self.connection = None
		
	def __init__(self, min, max):
		self.min = min
		self.max = max
		self.keys = list()
		self.values = list()
		self.leaf = True
		self.connection = None
		
	def add(self, key, value):
		for x in range(0, len(self.keys)):
			if(key[0] < self.keys[x][0]):
				self.keys.insert(x, key)
				temp = list()
				temp.append(value)
				self.values.insert(x, temp)
				return 0
			elif(key[0] == self.keys[x][0]):
				for y in range(x, len(self.keys)):
					if(key[1] < self.keys[x][1]):
						self.keys.insert(y, key)
						temp = list()
						temp.append(value)
						self.values.insert(y, temp)
					elif(key[1] == self.keys[x][1]):
						temp = self.values[y]
						for z in range(0, len(temp)):
							if(value < temp[z]):
								self.values[y].insert(z, value)
								return 0
							elif(value == temp[z]):
								print(value)
								print(temp[z])
								print("already exists")
								return 0
						self.values[y].append(value)
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
		
	def remove(self, x, key, value):
		self.values[x].remove(value) #make sure it is removing the value and not that index
		if(len(self.values[x]) == 0):
			self.keys.pop(x)
			self.values.pop(x)
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
		self.table.append(['tid','thing','thing','thing','thing'])
		with open(filename) as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				print(row)
				self.table.append(row)
				#for x in row:
				#print(x)
		for x in range(tid1, tid2 + 1):
			print("test")
			print(x)
			self.insert(x)
		return 0
	
	def printTree(self):
		queue = list()
		level = list()
		current = self.root
		print(current)
		print("testing print")
		if(current == None):
			return 0
		#print keys of root #MAKE NOTE THAT REMOVE AND POP ARE DIFFERENT IN THE LIST MAKE SURE TO NOT CONFUSE ANYWHERE
		queue.append(current)
		level.append(1)
		previousLevel = 0
		while(len(queue) > 0):
			current = queue.pop(0)
			currentLevel = level.pop(0)
			if(currentLevel != previousLevel):
				print()
				print("Level " + str(currentLevel) + ": ", end = '')
				previousLevel = currentLevel
			if(not current.leaf):
				q = current.keys
				for x in range(0, len(q)):
						print("  ", end = '')
						print(q[x], end = '')
						print("  ", end = '')
						queue.append(current.values[x])
						if(x == len(q) - 1):
							queue.append(current.values[x+1])
							level.append(currentLevel+1)
						level.append(currentLevel+1)
			else:
				keys = current.keys
				values = current.values
				size = len(keys)
				for x in range(0, size):
					print(keys[x], end = '')
					print(" ", end = '')
					print(values[x], end = '')
					if(x == size -1 and len(queue) > 0):
						print(" --> ", end = '')

		print()				
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
		print("the tid is")
		print(tid)
		key = [self.table[tid][self.key1], self.table[tid][self.key2]]
		print(key)
		value = tid
		stack = list()
		current = self.root
		#added this but not sure if this is required or already taken into consideration
		if(current == None):
			n = Node(1, self.d-1)
			n.add(key, value)
			self.root = n
			print("Added root")
			return 0
		while(not current.leaf):
			print("interesting")
			print(current.values)
			print(current.values[0])
			print(current.values[0].values)
			stack.append(current)
			q = current.keys
			first = 0
			last = len(q)-1
			if(key[0] < q[first][0] or (key[0] == q[first][0] and key[1] <= q[first][1])):
				print("should be this one")
				current = current.values[first]
			elif(key[0] > q[last][0] or (key[0] == q[last][0] and key[1] <= q[last][1])):
				current = current.values[last+1]
			else:			
				for x in range(1, len(q)):
					#not fully optimized, but written this way for clearer organization
					if(key[0] > q[x-1][0]):
						if(key[0] < q[x][0] or (key[0] == q[x][0] and key[1] <= q[x][1])):
							current = current.values[x]
					elif(key[0] == q[x-1][0] and key[1] > q[x-1][1]):
						if(key[0] < q[x][0] or (key[0] == q[x][0] and key[1] <= q[x][1])):
							current = current.values[x]
		print(current.keys)
		print(current.values)
		print("wtf")
		keys = current.keys
		values = current.values
		size = len(keys)
		for x in range(0, size):
			if(key[0] == keys[x][0] and key[1] == keys[x][1]):
				if(value not in values[x]):
					current.add(key, value)
					return 0
				#not sure if this else is needed, means it already exists inside
				else:
					print("entry already exists in the tree")
					return 0
		print("creating a new key and value")
		#create new key and value
		if(size < current.max):
			print("direct")
			current.add(key, value)
			return 0
		else:
			print("trying to do some splitting")
			temp = copy.deepcopy(current)
			temp.add(key, value)
			newNode = Node(self.d/2-1, self.d-1)
			newNode.connection = current.connection
			j = int((self.d)/2)
			print("j is")
			print(j)
			print(len(temp.keys))
			print(len(temp.values))
			current.keys.clear()
			current.values.clear()	
			#double check this entire part, seems like the +1 additional value may not be correct for this part
			for x in range(0, j):
				current.keys.append(temp.keys[x])
				current.values.append(temp.values[x])	
			for x in range(j, len(temp.keys)):
				newNode.keys.append(temp.keys[x])
				newNode.values.append(temp.values[x])
			current.connection = newNode
			key = temp.keys[j] #make sure this is correct
			#insert key into parent internal node in the right location, which I think is what is done below?
			finished = False
			while(not finished):
				depth = len(stack)
				if(depth == 0):
					n = Node(1, self.d-1)
					n.leaf = False
					n.keys.append(key)
					n.values.append(current)
					n.values.append(newNode)
					self.root = n
					finished = True
					print("Created root")
				else:
					current = stack.pop()
					if(len(current.keys) < current.max):
						current.add(key, value)
						finished = True
					else:
						temp = copy.deepcopy(current)
						temp.add(key, value)
						newNode = Node(self.d/2-1, self.d-1)
						j = int((self.d)/2)
						current.keys.clear()
						current.values.clear()	
						for x in range(0, j):
							current.keys.append(temp.keys[x])
							current.values.append(temp.values[x])	
						current.values.append(temp.values[j])
						for x in range(j+1, len(temp.keys)):
							newNode.keys.append(temp.keys[x])
							newNode.values.append(temp.values[x])
						newNode.values.append(temp.values[len(temp.keys)])
						key = temp.keys[j-1]
						print(key)
						print("key is above")
		print("Insertion has finished")
		return 0
		
	def delete(self, tid):
		key = [self.table[tid][self.key1], self.table[tid][self.key2]]
		value = tid
		stack = list()
		current = self.root
		#added this but not sure if this is required or already taken into consideration
		if(current == None):
			print("No deletion could be made.")
			return 0
		while(not current.leaf):
			stack.append(current)
			q = current.keys
			first = 0
			last = len(q)-1
			if(key[0] < q[first][0] or key[0] == q[first][0] and key[1] <= q[first][1]):
				temp = current.values[first]
				if(last > first and len(temp.keys) == temp.min):
					if(len(current.values[first+1].keys) >= temp.min + 2):
						temp.keys.append(current.keys.pop(first))
						temp.values.append(current.values.pop(first))
						current.keys.insert(0, current.values[first+1].keys.pop(0))
						current.values.insert(0, current.values[first+1].values.pop(0))
						#borrow
					else:
						temp.keys.append(current.keys.pop(first))
						for x in range(0, len(current.values[first+1].keys)):
							temp.keys.append(current.values[first+1].keys.pop(0))
							temp.values.append(current.values[first+1].values.pop(0))
						current.values.pop(first+1)
						#combine
				current = current.values[first]
			elif(key[0] > q[last][0] or key[0] == q[last][0] and key[1] <= q[last][1]):
				temp = current.values[last].values
				if(first < last and len(temp) == temp.min):
					if(len(current.values[last-1].keys) >= temp.min + 2):
						temp.keys.append(current.keys.pop(last))
						temp.values.append(current.values.pop(last))
						current.keys.append(current.values[last-1].keys.pop(0))
						current.values.append(current.values[last-1].values.pop(0))
						#borrow
					else:
						temp.keys.append(current.keys.pop(last))
						for x in range(0, len(current.values[last-1].keys)):
							temp.keys.append(current.values[last-1].keys.pop(0))
							temp.values.append(current.values[last-1].values.pop(0))
						current.values.pop(last-1)
						#combine			
				current = current.values[last+1]
			else:			
				for x in range(1, len(q)):
					#not fully optimized, but written this way for clearer organization
					if(key[0] > q[x-1][0]):
						if(key[0] < q[x][0] or key[0] == q[x][0] and key[1] <= q[x][1]):
						#double check below
							temp = current.values[x]
							if(x < len(q)-1 and len(temp.keys) == temp.min):
								if(len(current.values[x+1].keys) >= temp.min + 2):
									temp.keys.append(current.keys.pop(x))
									temp.values.append(current.values.pop(x))
									current.keys.insert(0, current.values[x+1].keys.pop(0))
									current.values.insert(0, current.values[x+1].values.pop(0))
									#borrow
								else:
									temp.keys.append(current.keys.pop(x))
									for x in range(0, len(current.values[x+1].keys)):
										temp.keys.append(current.values[x+1].keys.pop(0))
										temp.values.append(current.values[x+1].values.pop(0))
									current.values.pop(x+1)
									#combine	
						current = current.values[x]
					elif(key[0] == q[x-1][0] and key[1] > q[x-1][1]):
						if(key[0] < q[x][0] or key[0] == q[x][0] and key[1] <= q[x][1]):
							temp = current.values[x]
							if(x < len(q) and len(temp.keys) == temp.min):
								if(len(current.values[x+1].keys) >= temp.min + 2):
									temp.keys.append(current.keys.pop(x))
									temp.values.append(current.values.pop(x))
									current.keys.insert(0, current.values[x+1].keys.pop(0))
									current.values.insert(0, current.values[x+1].values.pop(0))
									#borrow
								else:
									temp.keys.append(current.keys.pop(x))
									for x in range(0, len(current.values[x+1].keys)):
										temp.keys.append(current.values[x+1].keys.pop(0))
										temp.values.append(current.values[x+1].values.pop(0))
									current.values.pop(x+1)
									#combine
						current = current.values[x]
		keys = current.keys
		values = current.values
		size = len(keys)
		for x in range(0, size):
			if(key[0] == keys[x][0] and key[1] == keys[x][1]):
				if(value in values[x]):		
					if(size > current.min):
						current.remove(x, key, value)
						break
		print("Deletion has finished.")
		return 0
		
	def search(self, key):
		current = self.root
		if(current == None):
			return 0
		while(not current.leaf):
			q = current.keys
			first = 0
			last = len(q)-1
			if(key[0] < q[first][0] or key[0] == q[first][0] and key[1] <= q[first][1]):
				current = current.values[first]
			elif(key[0] > q[last][0] or key[0] == q[last][0] and key[1] <= q[last][1]):
				current = current.values[last+1]
			else:			
				for x in range(1, len(q)):
					#not fully optimized, but written this way for clearer organization
					if(key[0] > q[x-1][0]):
						if(key[0] < q[x][0] or key[0] == q[x][0] and key[1] <= q[x][1]):
							current = current.values[x]
					elif(key[0] == q[x-1][0] and key[1] > q[x-1][1]):
						if(key[0] < q[x][0] or key[0] == q[x][0] and key[1] <= q[x][1]):
							current = current.values[x]
			
		keys = current.keys
		values = current.values
		size = len(keys)
		for x in range(0, size):
			if(key[0] == keys[x][0] and key[1] == keys[x][1]):	
				answer = values[x]
				print("Found tuple IDs : ", end = '')
				print(answer)
				print("Attributes are : ", end = '')
				print(self.table[0])
				for y in answer:
					print(self.table[y])
		return 0

	def range_search(self, keyMin, keyMax):
		queue = list()
		current = self.root
		if(current == None):
			return 0
		queue.append(current)
		print("Attributes are : ", end = '')
		print(self.table[0])
		while(len(queue) > 0):
			current = queue.pop(0)
			if(not current.leaf):
				q = current.keys
				for x in range(0, len(q)):	
					if((keyMin[0] < q[x][0] or (keyMin[0] == q[x][0] and keyMin[1] <= q[x][1])) and (keyMax[0] > q[x][0] or (keyMax[0] == q[x][0] and keyMax[1] >= q[x][1]))):
						queue.append(current.values[x])
						#double check this
						if(x == len(q)-1):
							queue.append(current.values[x+1])
			else:
				keys = current.keys
				values = current.values
				size = len(keys)
				for x in range(0, size):
					if((keyMin[0] < keys[x][0] or keyMin[0] == keys[x][0] and keyMin[1] <= keys[x][1]) and (keyMax[0] > keys[x][0] or keyMax[0] == keys[x][0] and keyMax[1] >= keys[x][1])):
						answer = values[x]
						print("Found tuple IDs : ", end = '')
						print(answer)
						for y in answer:
							print(self.table[y])
		
		return 0
		
def main():
	tree = BPlusTree()
	while(1):
		choice = input("What do you want to do: ")
		if(choice == "1"):
			filename = input ("File name: ")
			tid1 = int(input ("First tuple id: "))
			tid2 = int(input ("Second tuple id: "))
			tree.load(filename, tid1, tid2)
		if(choice == "2"):
			tree.printTree()
		elif(choice == "print"):
			tree.printTable()
		elif(choice == "3"):
			tid = int(input ("Which tid would you like to insert: "))
			tree.insert(tid)
		elif(choice == "4"):
			tid = int(input("Which tid to delete: "))
			tree.delete(tid)
			#delete
		elif(choice == "5"):
			key1 = input("First key: ")
			key2 = input("Second key: ")
			key = [key1, key2]
			tree.search(key)
		elif(choice == "6"):
			key1 = input("First key: ")
			key2 = input("Second key: ")
			key3 = input("Third key: ")
			key4 = input("Fourth key: ")
			key5 = [key1, key2]
			key6 = [key3, key4]
			tree.range_search(key5, key6)		
		elif(choice == "7"):
			break

if __name__ == "__main__": main()