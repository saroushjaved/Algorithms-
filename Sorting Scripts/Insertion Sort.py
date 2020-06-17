
# Name : Insertion Sort 
# Author : Soroush Javed Sulehri
# Liscence : MIT Liscence 
# Sorting Series Part 3(a)
# Email : soroushjaved@gmail.com


import random

n = int(input(" Enter the number of elements in random array : "))

l = [0]*n
for i in range(n):
    l[i] = random.randint(1,100)

print(l)


for i in range( n ):
    value = l[i]
    hole = i
    while (hole>0 and l[hole -1] > value):
        l[hole] = l[hole -1]
        hole = hole -1
    l[hole] = value
    print(l)
