#slice
#same as in list, it is used to specify how to slice a sequence.
#You can specify where to start the slicing, and where to end. You can also specify the step.
#example
t=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(t)
#syntax for slice() is [start:stop:step]
print(t[0:9])
    #here start() is 0 , stop() is 9
    #start():it indicates the index value, where it has to start.
    #stop():it indicates the index,where it has to end
print(t[0:10:2])
    #here step() is 2
    #step() : it indicates the increment value
                            
