#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from GoogleScraper import scrape_with_config, GoogleSearchError
import os

'''
    1. In core.py, scrape_with_config(), if don't want the result in stdout,
        set return_result = False;
    2. In core.py, main() returns scraper_search, which is a ScraperSearch object
        in database.py.
    3. serp is SearchEngineResultsPage object, in database.py.
        a. num_results_for_query -> string e.g. About 2,720,000 results (0.41 seconds)
        b. effective_query -> if it return back the query in string, means no result is found.
        c. no_results -> True means no result
        d. 

    !!! Unlike html file, it seems there is no clear way to get all the sentence, 
        and find which one has no punctration in it. !!!

    V1.0: just return the search counts: if no, return 0.01
        and ONLY SEARCH ONE sentence once!
'''
def scraper():
    os.remove("google_scraper.db")

    config = {
        'use_own_ip': True,
        'keyword_file': 'sent.txt',
        # 'bing_search_url' : 'http://www.bing.com/?mkt=zh-CN',
        'search_engines': ['google'],
        # 'search_engines': ['bing'],
        'num_pages_for_keyword': 1,
        'scrape_method': 'selenium',
        # 'scrape_method': 'http-async',
        #'sel_browser': 'firefox', # uncomment one when using selenium mode
        'sel_browser': 'chrome',
        'do_caching': False,
        'clean_cache_files' : False,
        'print_results' : 'summarize',
        # 'output_filename': 'out.csv', # added for async mode
        # 'google_sleeping_ranges' : { \
        #     1:  (2, 3), \
        #     5:  (3, 5), \
        #     30: (10, 20), \
        #     127: (30, 50), \
        #     }
    }

    try:
        search = scrape_with_config(config)
    except GoogleSearchError as e:
        print(e)

    num_result = []
    for serp in search.serps:
        # print("-------------------------------------------------------")
        if not serp.effective_query:
        # if serp.no_results == False: # not work for bing
            num_result.append(serp.num_results_for_query)
        else:
            num_result.append("0") # no result
#     print(serp.num_results_for_query)
#     print(serp.effective_query)
#     print(serp.no_results)

    return num_result
    # if the original query yielded some results and thus was found by google.
    # if not serp.effective_query:
    #     print('Found plagiarized content: "{}"'.format(serp.query))