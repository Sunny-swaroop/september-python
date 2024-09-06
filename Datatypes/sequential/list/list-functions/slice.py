#slice function
#A slice object is used to specify how to slice a sequence.
#You can specify where to start the slicing, and where to end. You can also specify the step.
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list1)
print(type(list1))
#syntax for slice() is [start:stop:step]
print(list1[0:9])
    #here start() is 0 , stop() is 9
    #start():it indicates the index value, where it has to start.
    #stop():it indicates the index,where it has to end
print(list1[0:10:2])
    #here step() is 2
    #step() : it indicates the increment value
