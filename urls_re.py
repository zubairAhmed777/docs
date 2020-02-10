import re

urls='''
http://www.google.com
http://www.google.edu
https://www.google.net
https://www.fb.com
http://www.ind.gov
HTTP://www.sk.com
'''

#########--------findall method
pattern=re.compile(r'[a-zA-Z]+://[a-zA-Z.]+\.[a-z]+')

matches_all=pattern.findall(urls)

for match in matches_all:
	print(match)

#####-------finditer method

matches_iter=pattern.finditer(urls)

for match in matches_iter:
	s=match.start()
	e=match.end()
	print(urls[s:e])
