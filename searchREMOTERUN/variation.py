#!/usr/bin/env python
# -*- coding: utf-8 -*-

def list2SimpleString(lst):
    string = ""
    for w in lst:
            string = string + w
    return string

def swapList(lst, i, j):
	temp = lst[i]
	lst[i] = lst[j]
	lst[j] = temp
	return lst

def customOrder(lst):
	''' order by need:
		 1. if there is only one word before bei, switch it with the one after bei
	'''
	result = []
	beiIndex = lst.index("被")
	# beiIndex >= 1
	result.append(list2SimpleString(swapList(lst, beiIndex -1 , beiIndex + 1))) # N受”与“N施”位置颠倒
	swapList(lst, beiIndex - 1, beiIndex + 1)

	result.append(list2SimpleString(swapList(lst, beiIndex , beiIndex + 1))) # 否定词位置颠倒
	swapList(lst, beiIndex, beiIndex + 1)
	

	return result


def ordering(lst):
	''' input a list of word string
		output a list of sentence of string 
		To keep the time complexisity to be O(n^2)
		Only shift each word'''
	result = []
	for i in range(0, len(lst)): # for each word in sentence
		sentence = list(lst)
		word = sentence.pop(i)
		for j in range(0, len(lst)):
			if j != i:
				tempSent = list(sentence)
				tempSent.insert(j, word)
				result.append(list2SimpleString(tempSent))
	return list(set(result))


def permu(lst):
	permuList = __permu__(lst)
	result = []
	for sentence in permuList:
		sentStr = list2SimpleString(sentence)
		result.append(sentStr)
	return result

def partialPermu(originLst):
	''' keep the position of bei,
		include the original sentence, the first one'''
	beiIndex = originLst.index("被")
	lst = list(originLst)
	lst.pop(beiIndex)
	result = []
	partial = __permu__(lst)
	for sentence in partial:
		sentence.insert(1, "被")
		sentStr = list2SimpleString(sentence)
		result.append(sentStr)
	return result

def __permu__(xs):
    if xs:
        r , h = [],[]
        for x in xs:
            if x not in h:
                ts = xs[:]; ts.remove(x)
                for p in __permu__(ts):
                    r.append([x]+p)
            h.append(x)
        return r
    else:
        return [[]]

def addWildCard(lst):
	''' input a list, insert "*" at every 
		output a list of sentence of string '''
	return addOne(lst, "*")


def addOne(lst, word):
	''' input the CORE SENTENCE, 
		output a list of modified sentence following this rule:
		(W: a chinese character)
		Input: SUBJUECT BEI W W W:
		Output:	BEI * W W W
				BEI W * W W
				BEI W W * W
				( no BEI W W W *, because it makes not different in google search)
		'''
	result = []
	for i in range(1, len(lst)):
		sentence = list(lst) # copy a new list
		sentence.insert(i, word)
		result.append(list2SimpleString(sentence))
		
	return result

def deleteOne(lst):
	''' input a list, delete each elements in the list once
		output a list of sentence of string '''
	result = []
	for i in range(0, len(lst)):
		sentence = list(lst)
		sentence.pop(i)
		result.append(list2SimpleString(sentence))

	return result

def deleteOneGiven(originLst, word):
	''' given the word you want to delete '''
	result = []
	beiIndex = originLst.index("被")
	lst = list(originLst)
	lst.pop(beiIndex)
	result.append(list2SimpleString(lst))
	return result


def saveList2File(filename, lst):
	with open(filename, 'wt') as f:
	    for sent in lst:
        	f.write('\"' + sent + '\"\n')

def saveList2FileNoQ(filename, lst):
	outfile = open(filename, 'w')
	for sent in lst:
		outfile.write(sent + '\n')
	outfile.close()
	# with open(filename, 'wt') as f:
	#     for sent in lst:
 #        	f.write(sent + '\n')

def saveList2FileNum(filename, lst):
	outfile = open(filename, 'w')
	for sent in lst:
		outfile.write(str(sent) + '\n')
	outfile.close()
	# with open(filename, 'wt') as f:
	#     for sent in lst:
 #        	f.write(str(sent) + '\n')
