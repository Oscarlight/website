#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scraper import scraper


class Search(object):
	''' use GoogleScraper to search a counts of a sentence 
		keep consistent with count.py '''
	counts = []

	def processData(self):
		# write the sentence in sent.txt
		# self.__writeIntoFile__(sentence)
		rawcountList = []
		# find counts from scraper
		rawcountList = scraper()
		# print(rawcountList)
		for rawcounts in rawcountList:
			freshcounts = 0.01  ## !!! Can cause some problem
			if rawcounts != "0":
				# print rawcounts
				''' Google style '''
				if len(rawcounts.split()) == 5: # About 88,300 results (0.59 seconds)
					freshcounts = int(rawcounts.split()[1].replace(',', ''))

				if len(rawcounts.split()) == 4: # 7 results (0.59 seconds)
					freshcounts = int(rawcounts.split()[0].replace(',', ''))

				''' Bing style '''
				if len(rawcounts.split()) == 2: # 88,300 results
					freshcounts = int(rawcounts.split()[0].replace(',', ''))

				# no further process now:
				self.counts.append(freshcounts)

			# print(self.counts)
