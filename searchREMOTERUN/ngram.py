# not been used

from google_ngram_downloader import readline_google_store

word = "china"

count = 0
fname, url, records = next(readline_google_store(ngram_len=1, indices=word[0]))
 
try:
	record = next(records)
 
	while record.ngram != word:
		record = next(records)
 
	while record.ngram == word:
		count = count + record.match_count
		record = next(records)
		
	print count

except StopIteration:
	pass