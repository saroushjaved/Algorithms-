# Name : Selection Sort Code
# Author : Soroush Javed Sulehri
# Liscence : MIT Liscence 
# Sorting Series Part 1(a)
# Email : soroushjaved@gmail.com

import random
import time

n = int(input(" Enter Number of Element in a random row : "))
l = [0] * n
# Random Generation of list 
for i in range(n):
    l[i] = random.randint(50,600)
sort_type = int(input(" Enter 1 for ascending and 2 for decending sort : "))

if sort_type == 1:
    a = time.time()
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    b = time.time()

else:
    a = time.time()
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] < l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp

    b = time.time()


print(l)
print()
print("The Runtime for this program is aproxx : {}".format((b-a)))
