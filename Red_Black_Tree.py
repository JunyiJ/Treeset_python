# RED: 0, BLACK:1, doubleBlack:2
class Node(object):

	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.color = 0
		self.left = None
		self.right = None
		self.parent = None
		
	def get_uncle(self):
		if not self.parent or not self.parent.parent:
			return None
		uncle = self.parent.parent.right
		if self.parent is uncle:
			uncle = self.parent.parent.left
		'''
		if uncle:
			print "uncle of %d is %d" %(self.key, uncle.key)
		else:
			print "uncle of %d is None" %(self.key)
		'''
		return uncle
		
	def printnode(self):
		color = "R"
		if self.color:
			color = "B"
		print str(self.key)+"("+color+")",
		
class RedBlackTree(object):

	def __init__(self):
		self.root = None
		
	def _search_insert(self, treenode, key, val):
		# normal BST insert
		# Return newnode if balancing is needed
		# Otherwise, return None
		if key == treenode.key:
			treenode.val = val
			return None
		if key < treenode.key:
			if treenode.left:
				return self._search_insert(treenode.left, key, val)
			else:
				newnode = Node(key, val)
				treenode.left = newnode
				newnode.parent = treenode
				return newnode
		else:
			if treenode.right:
				return self._search_insert(treenode.right, key, val)
			else:
				newnode = Node(key, val)
				treenode.right = newnode
				newnode.parent = treenode
				return newnode
				
	def insert(self, key, val):		
		if not self.root:
			self.root = Node(key, val)
			self.root.color = 1			
			return
		newnode = self._search_insert(self.root, key, val)
		if newnode.parent is self.root:
			return
		if newnode is not None:
			self.balance(newnode)
			
	def balance(self, node):
		while node is not self.root and node.color == 0 and node.parent.color == 0:
			uncle = node.get_uncle()
			if uncle and not uncle.color:
				# uncle is red
				node = self._recolor(node)
			else:
				node = self._rotation(node)
			self.root.color = 1
			
	def _recolor(self, node):
		#print "recolor", node.val
		uncle = node.get_uncle()
		node.parent.color = 1
		if uncle:
			uncle.color = 1
		node.parent.parent.color = 0
		return node.parent.parent
		
	def left_rotate_p(self, node):
		'''
		left rotate p
					g                g
				   / \              / \
				  p   u            x   u
				 / \       -->    / \
				T1  x             p  T3
				   / \           / \
				   T2 T3        T1  T2
		'''
		x, g, p= node.right, node.parent, node
		T2 = x.left
		g.left = x
		x.parent = g
		x.left = p
		p.parent = x
		p.right = T2
		if T2:
			T2.parent = p		
		
	def right_rotate_g(self, node):
		'''
		right rotate g
					g                p
				   / \              /  \
				  p   u            x    g
				 / \       -->    / \   /\
			     x  T3           T1 T2 T3 u
				/ \           
			   T1 T2        
		'''
		p, g, x = node.left, node, node.left.left
		T3 = p.right
		p.right = g
		g.left = T3
		if T3:
			T3.parent = g
		pg = g.parent
		if pg:
			if pg.left is g:
				pg.left = p
			else:
				pg.right = p
		p.parent = pg
		g.parent = p
		if g is self.root:
			self.root = p
		
	def right_rotate_p(self, node):
		'''
		right rotate p
			    g                g
			   / \              / \
			  u   p            u   x 
				 / \       -->    / \
			     x  T5           T3  p
				/ \                 / \
			   T3 T4               T4  T5
		'''
		x, p, g = node.left, node, node.parent
		T4 = x.right
		g.right = x
		x.parent = g
		x.right = p
		p.parent = x
		p.left = T4
		if T4:
			T4.parent = p
		
	def left_rotate_g(self, node):
		'''
		left rotate g
				g                p
			   / \              / \
			  u    p            g   x 
			 / \  / \  -->     / \
		    T1 T2 T3 x        u   T3
				             / \
				            T1  T2
		'''
		g, p, x = node, node.right, node.right.right
		T3 = p.left
		p.left = g
		g.right = T3
		if T3:
			T3.parent = g
		if g.parent:
			if g.parent.left is g:
				g.parent.left = p
			if g.parent.right is g:
				g.parent.right = p
		p.parent = g.parent
		g.parent = p
		if g is self.root:
			self.root = p
			
	def _rotation(self, node):
		# left left case: p is left kid of g and x is left kid of p
		if node.parent is node.parent.parent.left and node is node.parent.left:
			self.right_rotate_g(node.parent.parent)
			node.parent.color, node.parent.right.color = node.parent.right.color, node.parent.color
			return node.parent
		# left right case: p is left kid of g and x is right kid of p
		elif node.parent is node.parent.parent.left and node is node.parent.right:
			self.left_rotate_p(node.parent)
			self.right_rotate_g(node.parent)
			node.color, node.parent.color = node.parent.color, node.color
			return node
		# right right case
		elif node.parent is node.parent.parent.right and node is node.parent.right:
			self.left_rotate_g(node.parent.parent)
			node.parent.color, node.parent.left.color = node.parent.left.color, node.parent.color
			return node.parent
		# right left case
		elif node.parent is node.parent.parent.right and node is node.parent.left:
			self.right_rotate_p(node.parent)
			self.left_rotate_g(node.parent)
			node.color, node.parent.color = node.parent.color, node.color
			return node
			
	def _search(self, node, key):
		if not node:
			return None
		if node.key == key:
			return node
		if key < node.key:
			return self._search(node.left, key)
		else:
			return self._search(node.right, key)
			
	def delete_key(self, key):
		node = self._search(self.root, key)
		if not node:
			print "key %d not found" %(key)
			return 
		predecessor = node.left		
		while predecessor and predecessor.right:
			predecessor = predecessor.right	
		pnode = node
		if predecessor:
			pnode = predecessor.parent
		if predecessor:
			node.key = predecessor.key
			node.val = predecessor.val
			if predecessor.parent.left is predecessor:
				predecessor.parent.left = None
			else:
				predecessor.parent.right = None
		else:
			pnode = node.parent
			if node.parent.left is node:
				node.parent.left = None
			else:
				node.parent.right = None
		if (not predecessor or predecessor.color) and node.color:
			# double black case
			self.reduce_double_black(None, pnode)
			
	def reduce_double_black(self, node, pnode):	
		if node is self.root:
			return
		s = pnode.left
		if s is node:
			s = pnode.right	
		if s and ((s.left and s.left.color == 0) or (s.right and s.right.color == 0)):
			self.del_rotation_black(s)
		elif not s or s.color == 1:			
			self.del_recolor(s, pnode)
		else:
			self.del_rotation_red(s)
			
	def del_rotation_black(self, s):
		if s is s.parent.right:
			# Right Right Case
			if (s.left and s.right and s.left.color == 0 and s.right.color == 0) or (s.right and s.right.color == 0):
				self.left_rotate_g(s.parent)
				s.right.color = 1
				s.left.color = 1
			else:
				# Right Left Case
				self.right_rotate_p(s)
				s.color = 0
				s.parent.color = 1
				self.print_tree()
				self.left_rotate_g(s.parent.parent)
				s.parent.color = 1
				s.color = 1		
				
		else:
			if (s.left and s.right and s.left.color == 0 and s.right.color == 0) or (s.left and s.left.color == 0):
				self.right_rotate_g(s.parent)
				s.left.color = 1
				s.right.color = 1
			else:
				self.left_rotate_p(s)
				self.right_rotate_g(s.parent.parent)
				s.parent.color = 1
				s.color = 1
				
	
	def del_recolor(self, s, ps):
		
		if s:
			s.color = 0
		if ps.color:
			self.reduce_double_black(ps, ps.parent)
		else:
			ps.color = 1
	
	def del_rotation_red(self, s):
		if s is s.parent.left:
			self.right_rotate_g(s.parent)
			s.color = 1
			s.right.color = 0
			self.del_recolor(s.right.left)			
		else:
			self.left_rotate_g(s.parent)
			s.color = 1
			s.left.color = 0
			self.del_recolor(s.left.right)
			
			
	def print_tree_bfs(self):
		queue = [self.root]
		while queue:
			tmp = []
			for node in queue:
				node.printnode()
				if node.left:
					tmp.append(node.left)
				if node.right:
					tmp.append(node.right)
			print "\n"
			queue = tmp
			
			
	
tree = RedBlackTree()
		
		
		
		
		
		
		
	