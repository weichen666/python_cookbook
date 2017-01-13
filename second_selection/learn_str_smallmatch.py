#!/usr/bin/env python

import re
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'

resval = str_pat.findall(text1)
print(resval) #->['no.']

text2 = 'Computer says "no." Phone says "yes."'
resval = str_pat.findall(text2) 
print(resval) #->['no." Phone says "yes.']
 
"""
非贪婪模式:
	可以在模式中的*|+操作符后面加上?修饰
"""
str_pat_small = re.compile(r'\"(.*?)\"')
text2 = 'Computer says "no." Phone says "yes."'
resval = str_pat_small.findall(text2) 
print(resval) #->['no.', 'yes.']