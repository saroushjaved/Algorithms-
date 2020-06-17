
# Name : Linear Search Minimum Finder 
# Author : Soroush Javed Sulehri
# Liscence : MIT
# Minmax Series
# Email : soroushjaved@gmail.com


import time

l = [4,5,6,6,7,3,2,11,2,3,4,66,7,7,8,9,3,4,5,6,6,97,98,99]

maximum = l[0]


def maximum_finder(l):
    global maximum
    for i in range(len(l)):
        if l[i] > maximum:
            maximum = l[i]
    return maximum

print(maximum_finder(l))

