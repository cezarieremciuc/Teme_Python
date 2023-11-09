class Stack :
	def __init__(self):
		self.elements = []
	
	def isEmpty(self):
		return len(self.elements) == 0
		
	def push(self,item):
		self.elements.append(item)		
		
	def pop(self):
		return self.elements.pop()
		
	def peek(self):
		return self.elements[len(self.elements)-1]
	
	def size(self):
		return len(self.elements)
