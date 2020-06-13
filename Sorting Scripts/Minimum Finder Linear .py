import time

l = [4,5,6,6,7,3,2,11,2,3,4,66,7,7,8,9,3,4,5,6,6]

minimum = l[0]


def minimum_finder(l):
    global minimum
    for i in range(len(l)):
        if l[i] < minimum:
            minimum = l[i]
    return minimum

print(minimum_finder(l))

