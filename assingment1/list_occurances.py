#Given a list, find the most frequent element in it. If there are multiple elements that appear maximum number of times, print any one of them. 

from collections import Counter
list1=[1,2,3,4,1,2,3,4,2,3,2,3]

counter = Counter(list1)

most_frequent = counter.most_common(1)[0]

print(f"the most frequent element in the list is: {most_frequent[0]} and it occured:{most_frequent[1]} times")
