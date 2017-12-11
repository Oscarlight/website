import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Get Google Count.')
parser.add_argument('word', help='word to count')
args = parser.parse_args()

r = requests.get('http://www.google.com/search',
                 params={'q':'"'+args.word+'"',
                         "tbs":"li:1"}
                )

soup = BeautifulSoup(r.text, 'lxml')
# print soup
print len(soup.find_all("span",{"class":"st"})) + len(soup.find_all("div",{"class":"s"}))
# print data = [b.string for b in main_div.findAll('b')]
print soup.find('div',{'id':'resultStats'}).text
