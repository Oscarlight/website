class Node(object):
	''' Tree to store parsed sentence '''
	def __init__(self, data):
		self.data = data
		self.children = []

	def add_child(self, obj):
		self.children.append(obj)

	def __repr__(self, level = 0):
		ret = "\t"*level+ self.data + "\n"
		# print self.data
		for child in self.children:
			ret += child.__repr__(level+1)
		return ret


class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)


def createTree(parseTree):
	''' parseTree use parenthesis notation for tree '''
	
	pStack = Stack() # parenthesis stack
	wStack = Stack() # word stack
	newParseTree = parseTree
	for s in parseTree:
		newParseTree = newParseTree[1:]
		if s == "(":
			pStack.push(s)

			# push word into word stack
			word = ""
			nPT = newParseTree
			for c in newParseTree:
				if c == "(" or c == ")":
					wStack.push( Node(word.strip()) ) 
					# print "add node: " + wStack.peek().data
					break
				word += c 
				nPT = nPT[1:]

		elif s == ")":
			pStack.pop()
			if wStack.size() == 1:
				root = wStack.pop()
			else:
				child = wStack.pop()
				parent = wStack.peek()
				parent.add_child(child)
				# print "current str: " + newParseTree + "; parent node: " \
				# 	+ parent.data + "; added child: " + child.data 
	return root


def sentenceWithPOS(root, lst):
	''' return the (part of) sentence look down from
		a root,
		return a list of pos-word pair string '''
	if root.children == []:
		lst.append(root.data)
	for child in root.children:
		sentenceWithPOS(child, lst)
	return lst

def pairOfWord(word, root):
	''' give a word, get the word pos pair '''
	list = sentenceWithPOS(root, [])
	lst = []
	for s in list:
		if s.split()[1] == word:
			lst.append(s)
	return lst

def findParentsOfWord(node, pair, lst, parent):
	''' node: is the root (i.e. starting point);
		pair: i.e. POS_tag word;
		lst: contain the parent(s) of all the words (there may be more than one);
		parent: remember the parent of a child, set to root initially
		Return: lst, [] is not found'''
	if node.data == pair:
		lst.append(parent)
	for child in node.children:
		findParentsOfWord(child, pair, lst, node)
	return ( lst[0] if len(lst) == 1 else lst )  
 
def findLevelOfWord(node, clevel, pair, lst):
	''' Given a pair, return its level in the tree
		level count from 0, 0 is define at input "node" '''
	if node.data == pair:
		lst.append(clevel) # why lst = clevel not work!
	for child in node.children:
		findLevelOfWord(child, clevel + 1, pair, lst)
	return ( lst[0] if len(lst) == 1 else lst )

def findCousinsAtLevel(node, clevel, rlevel, lst):
	''' Find all cousins and brothers at the same level '''
	if clevel == rlevel:
		lst.append(node)
	for child in node.children:
		findCousinsAtLevel(child, clevel + 1, rlevel, lst)
	return lst

def pairList2WordList(lst):
	''' input a list of words/pos pair
		get a pure list of words 
		string list -> string list'''
	l = []
	for w in lst:
		if len(w.split()) == 2:
			l.append(w.split()[1])
	return l

def nodeList2WordList(lst):
	''' input a list of words/pos pair
		get a pure list of words 
		Node list -> string list'''
	l = []
	for w in lst:
		if len(w.data.split()) == 2:
			l.append(w.data.split()[1])
	return l

def hasChildWithWord(lst, word):
	''' find the index of the node in the list,
		whose child is the input word/pair'''
	for i in range(len(lst)):
		for child in lst[i].children:
			if child.data == word:
				return i

def list2String(lst):
	''' return a string has all list element
		seperated by | 
		Precondition: list of Node object 
		Node list -> string list'''
	str = ""
	for w in lst:
		str = str + " | " + w.data
	str = str + " | "
	return str

def stringList2String(lst):
	''' return a string has all list element
		seperated by | 
		Precondition: list of Node object 
		Node list -> string list'''
	str = ""
	for w in lst:
		str = str + " | " + w
	str = str + " | "
	return str


