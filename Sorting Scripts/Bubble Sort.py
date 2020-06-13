
# Name : Bubble Sort Code
# Author : Soroush Javed Sulehri
# Liscence : MIT Liscence 
# Sorting Series Part 2(a)
# Email : soroushjaved@gmail.com

import random
import time

n = int(input("Enter number of elements in the array you want : "))
l = [0] * n
for i in range(n):
    l[i] = random.randint(0,10000)

t1 = time.time()
for i in range(n-1): 
    for j in range(0, n-i-1): 

        if l[j] > l[j+1] : 
            l[j], l[j+1] = l[j+1], l[j]
t2 = time.time()

print(l)
print()
print("The time for execution is : {} ".format((t2-t1)))
