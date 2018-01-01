from Red_Black_Tree import RedBlackTree

class TreeSet(object):
	def __init__(self):
		self.rbtree = RedBlackTree()
		
	def add(self, key, val):
		#add specified key, value to TreeSet
		self.rbtree.insert(key, val)
	
	def addAll(self, elements):
		# add all elements to the set
		for element in elements:
			if len(element) != 2:
				raise TypeError("element should be in (key, val) pair")
			key, val = element
			self.add(key, val)
			
	def remove(self, key):
		# delete key if exists
		self.rbtree.delete_key(key)
	
	def clear(self):
		#remove all elements
		self.rbtree = RedBlackTree()
	
	def contains(self, key):
		#return true if given key exists
		return self.rbtree.search(key) is not None
		
	def first(self):
		# return first element if exists else None
		if self.rbtree.isempty():
			return None
		node = self.rbtree.first()	
		return (node.key, node.val)
	
	def last(self):
		# return last element if exists else None
		if self.rbtree.isempty():
			return None
		node = self.rbtree.last()
		return (node.key, node.val)
	
	def headSet(self, tokey):
		# return elements which are less than tokey
		return self.subSet(-float("inf"), tokey)
		
	def tailSet(self, fromkey):
		# return elements which are greater or equal to fromkey
		return self.subSet(fromkey, float("inf"))
		
	def subSet(self, fromkey, tokey):
		# return elements within range [fromkey, tokey)
		res = self.rbtree.subSet(fromkey, tokey)
		return [(node.key, node.val) for node in res]
		
	def print_tree(self):
		self.rbtree.print_tree_bfs()
		

		


		
	