#!/usr/bin/env python
# coding= utf-8
nums = [1, 2, 3, 4, 5]
print (x * x for x in nums) #-><generator object <genexpr> at 0x00000000006E7990>
s = sum(x * x for x in nums)
print (s)


import os
#默认加载当前文件夹下的所有文件的名字
files = os.listdir()
if any(name.endswith(".py") for name in files):
	print("There be python!")
else:
	print('Sorry, no python.')


s = ("ACME", 50, 123.45)
print(",".join(str(x) for x in s)) #->ACME,50,123.45

portfolio = [
	{'name':'GOOG', 'shares': 50},
	{'name':'YHOO', 'shares': 75},
	{'name':'AOL', 'shares': 20},
	{'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

from operator import itemgetter
min_prot = min(portfolio, key=itemgetter('shares'))  
print(min_prot) #->{'name': 'AOL', 'shares': 20}



