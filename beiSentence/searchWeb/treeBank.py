#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Queue import *
from tree import findLevelOfWord
from tree import findParentsOfWord
from tree import sentenceWithPOS

def contains(w, lst):
	if w in lst:
		return lst.index(w)
	return None

class TreeBank(object):
	# static list
	verbList = ['VA', 'VC', 'VE', 'VV']
	nounList = ['NR', 'NT', 'NN']
	localizerList = ['LC']
	pronounList = ['PN']
	det_numList = ['DT', 'CD', 'OD']
	measureList = ['M']
	adverbList = ['AD']
	prepoList = ['P']
	conjunList = ['CC', 'CS']
	particleList = ['DEC', 'DEG', 'DER', 'DEV', 'AS', 'SP', 'ETC', 'MSP']
	beiList = ['LB', 'SB']

	''' input word are (posTag word) '''
	def isVerb(self, pos_word):
		return contains(pos_word.split()[0], self.verbList)

	def isBeiConstruction(self, pos_word):
		return contains(pos_word.split()[0], self.beiList)

	def isNoun(self, pos_word):
		return contains(pos_word.split()[0], self.nounList)

	def isPronoun(self, pos_word):
		return contains(pos_word.split()[0], self.pronounList)

	def isAdverb(self, pos_word):
		return contains(pos_word.split()[0], self.adverbList)


def deleteAdv(lst):
	''' input a lst of pos-word pair,
		drop out certain non-essential part
			1) drop all adverb word
			2) drop the tree contains de5 DEG (done in other function) 
	'''
	result = []
	tB = TreeBank()
	for wp in lst:
		if tB.isAdverb(wp) == None:
			result.append(wp)
	return result

def deleteToListWithPOS(node, pair):
	''' input a node, if don't have "DEG 的" then just 
		output the sentenceWithPOS
		if it has "DEG 的", delete the whole tree has "DEG 的"
		output the sentenceWithPOS
	'''
	lst = []
	pList = findParentsOfWord(node, pair, [], node)
	if pList == []: # no "DEG 的"
		return sentenceWithPOS(node, lst)
	else:
		return __deleteHelper__(node, pList, lst)

def __deleteHelper__(root, pList, lst):
	if root.children == []:
		lst.append(root.data)
	for child in root.children:
		if isinstance(pList, list):
			if contains(child, pList) != None:
				__deleteHelper__(child, pList, lst)
		elif pList != child:
			__deleteHelper__(child, pList, lst)
	return lst


def findNPOrNoun(lst):
	'''' input a list of Node object
		if at the top level, there is pos/word pair, and pos is noun/pronoun
		return this node, else return all NP node 
		Return a list of top-level word pair list and a list of all NP nodes'''
	tB = TreeBank()
	tl = [] # top level word list
	nl = []	# NP node list
	for node in lst:
		if len(node.data.split()) == 2:
			if tB.isNoun(node.data) != None or tB.isPronoun(node.data) != None:
				tl.append(node)
		elif node.data == "NP":
			nl.append(node)
	return [tl,nl]

def highestNoun(lst):
	''' input a lst of Node object, 
		find the smallest level Noun/pronoun
		Node list -> String list '''
	wordLevelList = []
	for node in lst:
		nl = BFS(node)
		for n in nl:
			level = findLevelOfWord(node, 0, n, [])
			if isinstance(level, list): # multiply words, select the smallest level one
				minLevel = min(level)
				wordLevelList.append([n, minLevel])
			wordLevelList.append([n, level])

	# for all the word, we have to keep their order correct,
	# must test to see whether order is preserved
	## sort the wordLevelList
	qs(wordLevelList, 0, len(wordLevelList) - 1)
	smallestLevel = wordLevelList[0][1]
	resultList = []
	for w in wordLevelList:
		if w[1] == smallestLevel:
			resultList.append(w[0])
	return resultList




def BFS(node):
	''' do a BFS to find all noun in 
		the sub-tree rooted at input node'''
	tB = TreeBank()
	nl = [] # noun/pronoun list
	visited = []
	q = Queue()
	q.put(node)
	while (not q.empty()):
		u = q.get()
		if u not in visited:
			visited.append(u)
			if tB.isNoun(u.data) != None or tB.isPronoun(u.data) != None:
				nl.append(u.data)
			for child in u.children:
				q.put(child)
	return nl


def partition(lst, h, k):
	''' costumized for wordLevelList '''
	j = h
	t = k
	while ( j < t ):
		if ( lst[j + 1][1] <= lst[j][1]):
			temp = lst[j + 1]
			lst[j + 1] = lst[j]
			lst[j] = temp
			j = j + 1
		else:
			temp = lst[j + 1]
			lst[j + 1] = lst[t]
			lst[t] = temp
			t = t - 1
	return j

def qs(lst, h, k):
	if (len(lst[h:k]) < 2 or k < 0): 
	## when k = -1, len(lst[0:-1]) = len(a) - 1, not as expected
		return 
	j = partition(lst, h, k)
	qs(lst, h, j - 1)
	qs(lst, j + 1, k)

