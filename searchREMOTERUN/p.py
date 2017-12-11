#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from countGoogleScraper import *
import json
import math

disList = []

## reconstruct from file
## !!! from php ssh2_exec: if missing  encoding="utf-8" , it won't run
length = []
with open("/home/oscar/Documents/AptanaStudio3Workspace/searchREMOTERUN/length.txt",  encoding="utf-8") as f:
	# print(f.readlines())
	for s in f.readlines():
		length.append(int(s.replace('\n','')))


sent = []
with open("/home/oscar/Documents/AptanaStudio3Workspace/searchREMOTERUN/sent.txt",  encoding="utf-8") as f:
	for s in f.readlines():
		sent.append(s.replace('\n',''))

# print(json.dumps(["IHateit", "NoIloveit"]))

coreSenStr = sent[0]
beiConstStr = sent[1]


orderList = []
counter = 1
for i in range(length[0]):
	counter = counter + 1
	orderList.append(sent[counter])

addOneList = []
for i in range(length[1]):
	counter = counter + 1
	addOneList.append(sent[counter])

deleteOneList = []
for i in range(length[2]):
	counter = counter + 1
	deleteOneList.append(sent[counter])

#print(json.dumps(["I Hate it", "No I love it"]))

# print("works")
## search
s = Search()
# !!
s.processData()
# !!
cSCount = s.counts[0]
bCCount = s.counts[1]
# print("works")


## Generate Counts
# 1) eliminate punctuation
# 2) remember the best choice
# Orignal Sentence:
disList.append("\n<strong>基准线为 (Baselines are):</strong> \n")
# disList.append("Baselines" + " --> "+ "Count" + "\n")

cSCount = s.counts[0]
disList.append(coreSenStr + "-------- 出现次数(count): "+ str(cSCount) + "\n")
# time.sleep(random.uniform(10, 30))

bCCount = s.counts[1]
disList.append(beiConstStr + "-------- 出现次数(count): "+ str(bCCount) + "\n")
# time.sleep(random.uniform(10, 30))

perScoreList = []
disList.append("\n<strong>部分词序组合为 (Partial Permutation of derived sentences are) :</strong> \n")
# disList.append("Possible candidate" + " --> "+ "Score" + "\n")
i = 1
for order in orderList:
	i = i + 1
	score = math.log10(s.counts[i]/cSCount)
	# print order; print score
	perScoreList.append(score)
	disList.append(order + "-------- 指数可能性 (log likelihood): "+ str(score) + "\n")

addScoreList = []
disList.append("\n<strong>添加一个字的可能情况 (Derived sentences with one wild card are):</strong> \n")
# disList.append("Possible candidate" + " --> "+ "Score" + "\n")
for addOne in addOneList:
	i = i + 1
	score = math.log10(s.counts[i]/bCCount)
	score = score - 0.05 
	# print addOne; print score
	addScoreList.append(score)
	disList.append(addOne + "-------- 指数可能性 (log likelihood): "+ str(score) + "\n")

delScoreList = []
disList.append("\n<strong>删除被字的情况为 (Derived sentences with bei deleted are):</strong> \n")
# disList.append("Possible candidate" + " --> "+ "Score" + "\n")
for deleteOne in deleteOneList:
	i = i + 1
	score = math.log10(s.counts[i]/cSCount)
	score = score - 2.6 # threshold
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
	disList.append("<strong>语序错误</strong>  (修改建议： " + orderList[pmaxi] + ")")
	print(json.dumps(disList))
	raise SystemExit("End")
if tmaxi == 1 and amax > 0 :
	disList.append("<strong>缺词错误</strong>  (修改建议： " + addOneList[amaxi] + ")")
	print(json.dumps(disList))
	raise SystemExit("End")
if tmaxi == 2 and dmax > 0 :
	disList.append("<strong>被字多余</strong>")
	print(json.dumps(disList))
	raise SystemExit("End")	

disList.append("<strong>无可识别错误</strong>")
print(json.dumps(disList))
raise SystemExit("End")



