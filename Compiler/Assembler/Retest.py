import re
str1 = "MDC=10"

str = re.match(".*?=",str1)
print(str.group())   #返回匹配的结果
print(str1.find(";"))