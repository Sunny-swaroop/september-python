# write a program to find the execution time of a program

import time

start_time=time.time()

for x in range(1,10):
    if x%2==0:
        print(x)
    
    
    
end_time=time.time()

execution_time = start_time - end_time

print(f"the execution time of the given program is:{execution_time}")
