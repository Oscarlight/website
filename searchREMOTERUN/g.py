#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Core sentence 
		Version 1: if find NN at bei uncle's level, use it. If not
				   find the highest level NN in NP
				   If multiple word in subject, use the one closest to bei

		Version 2: find both NN at bei uncle's level and the last NN in NP

	Google: query google webpage.
'''
import argparse
import json
from tree import *
from treeBank import *
from variation import *
from count import *
import time
import random
import math


## Read into the arguments
parser = argparse.ArgumentParser(description='analysis based on google search')
parser.add_argument('parseTree', help='parse tree from StanfordNLP parser')
args = parser.parse_args()
pT = args.parseTree

## For test only
# pT = "(ROOT (IP (NP (PN 我)) (VP (ADVP (AD 已经)) (VP (LB 被) (IP (NP (PN 你)) (VP (VV 爱) (NP (NN 过了))))))))"
# ----------------------
# pT = "(ROOT (IP \
#     (ADVP (AD 所以)) \
#     (NP \
#       (DNP \
#         (NP (NR 中国)) \
#         (DEG 的)) \
#       (NP (NN 美丽))) \
#     (VP (LB 被) \
#       (IP \
#         (NP (PN 我)) \
#         (VP \
#           (ADVP (AD 越来越)) \
#           (VP (VV 吸引))))))) "
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

# pT = "(ROOT \
#   (IP \
#     (NP \
#       (DP (DT 这) \
#         (CLP (M 件))) \
#       (NP (NN 事))) \
#     (NP (PN 她)) \
#     (VP (SB 被) \
#       (VP (VV 后悔) (AS 了)))))"

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
noDeSent = pairList2WordList(deleteToListWithPOS(root, ["DEG 的", "DEC 的"]))
if contains("被", noDeSent) == None:
	# disList.append("After delete de: " + stringList2String(noDeSent))
	# disList.append("Result: This sentence is incorrect: Not a bei sentence: 被...的 structure")
	disList.append("无法确认与被字对应的名词或名词短语。")
	disList.append("主语缺失或受事对象不明")
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
	# disList.append("The parent of 被 don't have any cousin.")
	# disList.append("Result: This sentence is incorrect: Sentence Structure Error")
	disList.append("无法确认与被字对应的名词或名词短语。")
	disList.append("主语缺失或受事对象不明")
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
# (* V1.0 if there is a pos/word pair which is noun at parent cousin's level, use it
# else find the NP, find the first (smallest level) noun *)
# (* V2.0 (updated 03/19) 1. put both NP and Noun in the same list;
# subList include all parent consin's level Noun and the frist noun (smallest level and 
# closest to bei.))
# nounNPList = findNPOrNoun(beiParentCousinList) # (V1.0)
nounNPList = findNPAndNoun(beiParentCousinList) # (V2.0)

# disList.append("The noun word at the parent level of 被 is " + list2String(nounNPList[0]) + "\n")
# disList.append("The NP node at the parent level of 被 is " + list2String(nounNPList[1]) + "\n")
coreSen = [] # core sentence 
beiConst = pairList2WordList(deleteDetNum(\
							deleteAdv(\
							deleteToListWithPOS(\
							beiParentCousinList[beiParentIndex], ["DEG 的", "DEC 的"])))) # bei subtree

# (* V1.0 *)
# if len(nounNPList[0]) > 0:
# 	# generate core sentence directly
# 	subList = nodeList2WordList(nounNPList[0])
# 	## OPEN to Question: only to pick the closest one to bei
# 	coreSen = subList[-1:] + beiConst
# elif len(nounNPList[1]) > 0:
# 	# find smallest level noun
# 	subList = pairList2WordList(highestNoun(nounNPList[1]))
# 	## OPEN to Question: only to pick the closest one to bei
# 	coreSen = subList[-1:] + beiConst
# else:
# 	disList.append("被 sentence lask subject.")
# 	disList.append("Result: This sentence is incorrect: Sentence lack subject")
# 	print json.dumps(disList)
# 	raise SystemExit("No noun Error")
# (* V1.0 *)

# (* V2.0 *)
if len(nounNPList) > 0:
	subList = []
	for node in nounNPList:
		if node.data == "NP":
			npList = pairList2WordList(highestNoun([node]))
			subList.append(npList[-1])
		else:
			subList.append(node.data.split()[1])
	coreSen = subList + beiConst
else:
	disList.append("无法确认与被字对应的名词或名词短语。")
	disList.append("主语缺失或受事对象不明")
	print json.dumps(disList)
	raise SystemExit("No noun Error")
# (* V2.0 *)	

disList.append("<strong>核心句为：(The core sentence is:) </strong>" + stringList2String(coreSen) + "\n")

## KEY: to generate variation from core sentence:
# 1) change orders (with subject)
# 2) insert * (without subject)
# 3) delete words (more details below)
coreSenStr = list2SimpleString(coreSen) # original sentence
beiConstStr = list2SimpleString(beiConst) # orignal bei-Construction

# (* Version 1: orderList = ordering(coreSen) (i.e. only move one word at a time) *)
# orderList = partialPermu(coreSen) # (* Version 2:  *)
orderList = customOrder(coreSen)
# disList.append("Permutation of derived sentences are: \n" + stringList2String(orderList) + "\n")

addOneList = addWildCard(beiConst)
# disList.append("Derived sentences with one wild card are: \n" + stringList2String(addOneList) + "\n")

# OPEN for questions, I feel that delete very elements is not very useful
# opt for test delete bei only
# deleteOneList = deleteOne(coreSen)
deleteOneList = deleteOneGiven(coreSen, "被")
# disList.append("Derived sentences with one deleted are: \n" + stringList2String(deleteOneList) + "\n")


# ## Save them to two file
# # length.txt and sent.txt
# totalList = [coreSenStr, beiConstStr]
# totalList = totalList + orderList + addOneList + deleteOneList
# lengthList = [len(orderList), len(addOneList), len(deleteOneList)]
# saveList2FileNum("length.txt", lengthList)
# saveList2File("sent.txt", totalList)

## Generate Counts
# 1) eliminate punctuation
# 2) remember the best choice
# Orignal Sentence:
disList.append("\n<strong>基准线为 (Baselines are):</strong> \n")
# disList.append("Baselines" + " --> "+ "Count" + "\n")

s = Search()
s.processData(coreSenStr)
# print coreSenStr; print s.counts
cSCount = s.counts
disList.append(coreSenStr + "-------- 出现次数(count): "+ str(cSCount) + "\n")
time.sleep(random.uniform(10, 30))

s = Search()
s.processData(beiConstStr)
# print beiConstStr; print s.counts
bCCount = s.counts
disList.append(beiConstStr + "-------- 出现次数(count): "+ str(bCCount) + "\n")
time.sleep(random.uniform(10, 30))

perScoreList = []
disList.append("\n<strong>部分词序组合为 (Partial Permutation of derived sentences are) :</strong> \n")
# disList.append("Possible candidate" + " --> "+ "Score" + "\n")
for order in orderList:
	s = Search()
	s.processData(order)
	time.sleep(random.uniform(20, 30))
	score = math.log10(s.counts/cSCount)
	# print order; print score
	perScoreList.append(score)
	disList.append(order + "-------- 指数可能性 (log likelihood): "+ str(score) + "\n")

addScoreList = []
disList.append("\n<strong>添加一个字的可能情况 (Derived sentences with one wild card are):</strong> \n")
# disList.append("Possible candidate" + " --> "+ "Score" + "\n")
for addOne in addOneList:
	s = Search()
	s.processData(addOne)
	time.sleep(random.uniform(20, 30))
	score = math.log10(s.counts/bCCount)
	score = score - 0.05 
	# print addOne; print score
	addScoreList.append(score)
	disList.append(addOne + "-------- 指数可能性 (log likelihood): "+ str(score) + "\n")

delScoreList = []
disList.append("\n<strong>删除被字的情况为 (Derived sentences with bei deleted are):</strong> \n")
# disList.append("Possible candidate" + " --> "+ "Score" + "\n")
for deleteOne in deleteOneList:
	s = Search()
	s.processData(deleteOne)
	time.sleep(random.uniform(20, 30))
	score = math.log10(s.counts/cSCount)
	score = score - 2 # threshold
	# print deleteOne; print score
	delScoreList.append(score)
	disList.append(deleteOne + "-------- 指数可能性 (log likelihood): "+ str(score) + "\n")

# disList.append("\n<strong> (--> 指数可能性得分 (--> indicates log likelihood score) ) </strong>\n")

## Judge
pmax = max(perScoreList)
pmaxi = perScoreList.index(pmax)
amax = max(addScoreList)
amaxi = addScoreList.index(amax)
dmax = max(delScoreList)
dmaxi = delScoreList.index(dmax)

tmaxList = [pmax, amax, dmax]
tmaxi = tmaxList.index(max(tmaxList))
if tmaxi == 0 and pmax > 0 :
	disList.append("<strong>语序错误 | Word order error </strong>  (修改建议 | Suggestion： " + orderList[pmaxi] + ")")
	print json.dumps(disList)
	raise SystemExit("End")
if tmaxi == 1 and amax > 0 :
	disList.append("<strong>缺词错误 | Missing word error </strong>  (修改建议 | Suggestion： " + addOneList[amaxi] + ")")
	print json.dumps(disList)
	raise SystemExit("End")
if tmaxi == 2 and dmax > 0 :
	disList.append("<strong>被字多余 | Redundant bei </strong>")
	print json.dumps(disList)
	raise SystemExit("End")	

disList.append("<strong>无可识别错误 | No error detected </strong>")
print json.dumps(disList)
raise SystemExit("End")

## Output to php
# disList.append("FLAG:TRUE") # indicate no error is found in the sentence, do the possibility part
# print json.dumps(disList)
