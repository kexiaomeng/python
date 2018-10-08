import re


line = 'sun,   meng; meng'

list = re.split(r'[;,\s]\s*', line)   #re.split可以指定匹配规则  正则表达式[]表示不捕获分割符，（）表示捕获分隔符

list1 = re.split(r'(;|,|\s)\s*', line)
print(list)
print(list1)