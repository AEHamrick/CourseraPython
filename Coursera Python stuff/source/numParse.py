import re

#fileHandle = open("regex_sum_42.txt")
fileHandle = open("regex_sum_306118.txt")

fileString = fileHandle.read()

numbers = re.findall("[0-9]+",fileString)
numbers = [int(i) for i in numbers]
#print int(numbers)
#print sum(numbers)
print sum([int(i) for i in re.findall("[0-9]+",open("regex_sum_306118.txt").read())])