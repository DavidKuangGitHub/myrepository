import re
#learn_RegularExpression_import_re.py 

#was bad now it is fixed by put a space between , and ' 
m = re.search('(?<=abc)def', 'abcdef')
#m = re.search('(?<=abc)def', 'abcdef')
#m = re.search(r'(?<=-)\w+', 'spam-egg')
#print(m.group(0))
print(m)
