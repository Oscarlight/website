#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
from tree import *
from treeBank import *
from variation import *
from count import *


## Read into the arguments
# parser = argparse.ArgumentParser(description='analysis based on google search')
# parser.add_argument('parseTree', help='parse tree from StanfordNLP parser')
# args = parser.parse_args()
# pT = args.parseTree

## For test only
# pT = "(ROOT (IP (NP (PN 我)) (VP (ADVP (AD 已经)) (VP (LB 被) (IP (NP (PN 你)) (VP (VV 爱) (NP (NN 过了))))))))"
# ----------------------
pT = "(ROOT \
  (IP \
    (NP (PN 他)) \
    (VP (SB 被) \
      (VP (VV 猎头)\
        (NP\
          (CP\
            (IP\
              (VP (VV 进)\
                (NP (NR 美国))))\
            (DEC 的))\
          (NP (NN 银行)))))))"
# ----------------------
# pT = "(ROOT \
#   (NP \
#     (CP \
#        (IP \
#         (NP (NR 中国)) \
#         (VP (SB 被) \
#           (VP (VV 污染)))) \
#       (DEC 的)) \
#     (NP (NN 树)))) "
# ----------------------
# pT = "(ROOT \
#   (IP \
#     (NP (PN 我)) \
#     (VP (LB 被) \
#       (IP \
#         (NP \
#           (DNP \
#             (ADJP (JJ 美丽)) \
#             (DEG 的)) \
#           (NP (NR 中国))) \
#         (VP (VV 感动) (AS 了))))))"

## Display str lsit
disList = []

## Create a tree
root = createTree(pT)

## Create treeBank instance
tB = TreeBank()

## Find the pos/word pair(s) of bei
beiPairList = pairOfWord("被", root)
if beiPairList == []:
	## for communication with php
	print json.dumps(["No 被 in the sentence, don't want to waste our time... Bye!", \
		"Result: No 被 in the sentence"]) # the latter one for display final information
	raise SystemExit("No bei error")
else:
	i = 0 # counter
	index = -1 
	for p in beiPairList:
		if  tB.isBeiConstruction(p) != None:
			i = i + 1
			index = contains(p, beiPairList)
	if i > 1:
		disList.append("More than one 被 in bei-Construction, please seperate them into its own sentence.")
		disList.append("Result: More than one 被 in bei-Construction, please seperate them into its own sentence.")
		print json.dumps(disList)
		raise SystemExit("Too much 被 error")
	if i == 0:
		disList.append("No 被 in bei-Construction")
		disList.append("Result: No 被 in bei-Construction.")
		print json.dumps(disList)
		raise SystemExit("No bei-Construction")
	# i = 1
	beiPair = beiPairList[index]

## Exclude bei structure used as Adj.
# in "被污染的树", is (IP (被污染) (的)), delete de will delete the bei too,
# the above example is NOT a bei-construction, even bei is tagged as BS
# in above beiConst = ..., we delete the de structure, here we check whether bei still exist.
if contains("被", pairList2WordList(deleteToListWithPOS(root, "DEC 的"))) == None:
	disList.append("Result: This sentence is incorrect: Not a bei sentence: 被...的 structure")
	disList.append("Result: This sentence is incorrect: Not a bei sentence: 被...的 structure")
	print json.dumps(disList)
	raise SystemExit("Not bei sentence Error")

# disList.append("The tree node containing 被 is: " + beiPair + "\n")

## Find the level of bei, precondition, only ONE beiPair
beiLevel = findLevelOfWord(root, 0, beiPair, [])
# disList.append("被 is at level " + str(beiLevel) + " in the parsing tree.\n") 
# print json.dumps([ostr0, ostr1, ostr2])

## Find the list of cousins of bei's parent node
beiParentCousinList = findCousinsAtLevel(root, 0, beiLevel-1, [])
# if bei parents don't have cousin, we may 1) look up grandparents, 2) declare structure error
if len(beiParentCousinList) == 1:
	disList.append("The parent of 被 don't have any cousin.")
	disList.append("Result: This sentence is incorrect: Sentence Structure Error")
	print json.dumps(disList)
	raise SystemExit("No parent cousin Error")

## Find where bei's parent in the list	
beiParentIndex = hasChildWithWord(beiParentCousinList, beiPair)
# disList.append("The parent generation of 被 is: " + list2String(beiParentCousinList) + \
		# "  And the direct parent of 被 is at index :" + str(beiParentIndex) + "\n")

## Delete all node after bei's parent's node 
# (* open for question, maybe good enough for typical bei sentence *)
beiParentCousinList = beiParentCousinList[0:(beiParentIndex + 1)]
# disList.append("Ignore everything come after the parent of 被, the new list is" + \
	# list2String(beiParentCousinList) + "\n")

## Find the subject of bei-construction, and generate core sentence
# if there is a pos/word pair which is noun at parent cousin's level, use it
# else find the NP, find the first (smallest level) noun
nounNPList = findNPOrNoun(beiParentCousinList)
# disList.append("The noun word at the parent level of 被 is " + list2String(nounNPList[0]) + "\n")
# disList.append("The NP node at the parent level of 被 is " + list2String(nounNPList[1]) + "\n")
coreSen = [] # core sentence 
beiConst = pairList2WordList(deleteAdv(deleteToListWithPOS(beiParentCousinList[beiParentIndex], "DEG 的"))) # bei subtree


if len(nounNPList[0]) > 0:
	# generate core sentence directly
	subList = nodeList2WordList(nounNPList[0])
	## OPEN to Question: only to pick the closest one to bei
	coreSen = subList[-1:] + beiConst
elif len(nounNPList[1]) > 0:
	# find smallest level noun
	subList = pairList2WordList(highestNoun(nounNPList[1]))
	## OPEN to Question: only to pick the closest one to bei
	coreSen = subList[-1:] + beiConst
else:
	disList.append("被 sentence lask subject.")
	disList.append("Result: This sentence is incorrect: Sentence lack subject")
	print json.dumps(disList)
	raise SystemExit("No noun Error")

disList.append("<strong>核心句为：(The core sentence is:) </strong>" + stringList2String(coreSen) + "\n")

## KEY: to generate variation from core sentence:
# 1) change orders (with subject)
# 2) insert * (without subject)
# 3) delete words (more details below)
coreSenStr = list2SimpleString(coreSen) # original sentence
beiConstStr = list2SimpleString(beiConst) # orignal bei-Construction

orderList = partialPermu(coreSen) # ordering (i.e. only move one word at a time)
disList.append("Permutation of derived sentences are: \n" + stringList2String(orderList) + "\n")

addOneList = addWildCard(beiConst)
disList.append("Derived sentences with one wild card are: \n" + stringList2String(addOneList) + "\n")

# OPEN for questions, I feel that delete very elements is not very useful
# opt for test delete bei only
# deleteOneList = deleteOne(coreSen)
deleteOneList = deleteOneGiven(coreSen, "被")
disList.append("Derived sentences with one deleted are: \n" + stringList2String(deleteOneList) + "\n")

## Generate Counts
# 1) eliminate punctuation
# 2) remember the best choice
# for order in orderList:
# 	print order
# 	s = Search()
# 	s.processData(order)
# 	print s.counts

# for addOne in addOneList:
# 	print addOne
# 	s = Search()
# 	s.processData(addOne)
# 	print s.counts

disList.append("<strong>Derived sentences with one deleted are</strong>: \n")

print json.dumps(disList)
# for word in list:
# 	print word

# print pair
# print findParentsOfWord(root, pair, [], root)
# print findCousinsAtLevel(root, 0, 3, [])
# print findLevelOfWord(root, 0, pair, [])
# print findCousinsAtLevel(root, 0, findLevelOfWord(root, 0, pair, []), [])


## for communication with php
#print json.dumps([root.__repr__()])

# r = requests.get('http://www.google.com/search',
#                  params={'q':'"'+args.word+'"',
#                          "tbs":"li:1"}
#                 )

# soup = BeautifulSoup(r.text, 'lxml')
# # print soup
# print len(soup.find_all("span",{"class":"st"})) + len(soup.find_all("div",{"class":"s"}))
# # print data = [b.string for b in main_div.findAll('b')]
# print soup.find('div',{'id':'resultStats'}).text
