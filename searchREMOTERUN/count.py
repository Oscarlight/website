#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

class Search(object):

	url = 'http://www.google.com/search'
	counts = 0.01 # > 0 small number indicate no results
	sentList = []

	def __sendReq__(self, sentence):
		r = requests.get(self.url,
                  params={'q':'"'+ sentence +'"',
                          "tbs":"li:1"} )
		return BeautifulSoup(r.text, 'lxml')

	def processData(self, sentence):
		soup = self.__sendReq__(sentence)
		# print soup
		if soup.find('div',{'id':'resultStats'}) != None:
			rawcounts = soup.find('div',{'id':'resultStats'}).text
			# Nice, if no result, google display the counts as image so
			# no counts! Thank you google!
			if rawcounts != '':
				# print rawcounts
				if len(rawcounts.split()) == 3: # About 88,300 results
					freshcounts = int(rawcounts.split()[1].replace(',', ''))

				if len(rawcounts.split()) == 2: # 7 results
					freshcounts = int(rawcounts.split()[0].replace(',', ''))

				rawSentList = soup.find_all("b")
				freshSentList = [] # the real sentence in <b> tag
				try:
					correctLen = len(sentence.decode('utf-8')) # python2
				except:
					correctLen = len(sentence) # python3
				# print correctLen
				for rawSent in rawSentList:
					if rawSent.text == u'Search' or rawSent.text == u'Verbatim' or \
						rawSent.text == u'...' or rawSent.text == u'' or rawSent.text == u'1' \
						or len(rawSent.text) < correctLen:
						pass
					else:
						freshSentList.append(rawSent.text)
				
				if len(freshSentList) != 0: # in the case that freshSentList = []
					i = 0.0
					for freshSent in freshSentList:
						# print freshSent
						if len(freshSent) == correctLen:
							self.sentList.append(freshSent) # remember the result without punctutation
							i = i + 1.0

					totalNumFreshSent = len(freshSentList) 
					discount = (i + 0.01) / (totalNumFreshSent)
					# print discount
					self.counts = freshcounts * discount 
					# print freshcounts
					# print self.counts

		


