
# Name : Insertion Sort Animation
# Author : Soroush Javed Sulehri
# Liscence : MIT Liscence 
# Sorting Series Part 3(b)
# Email : soroushjaved@gmail.com

import turtle
import random
import time


# Inital Screen Setup
screen = turtle.Screen()
# Defining Screen Size
screen.setup(2000,2000)
# Complicated Argument mostly means that the turtle should not show every step of animation
screen.tracer(10,10)
screen.title('Insertion Sort')
turtle.speed(0)
turtle.hideturtle()

# Taking number of bars as input
n = int(input("Enter the number of elements you want in the array : "))
l = [0] * n
# Random Generation of list 
for i in range(n):
    l[i] = random.randint(50,600)

# Bar Drawing Function
def draw_bar(x,y,w,h):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

# Multiple bars drawing and Updating Function 
def draw_bars(l, n):
    w = 500/n
    x = -400
    for i in range(len(l)):
        if i == c : turtle.fillcolor("red")
        elif i == c2: turtle.fillcolor("gold")
        else:turtle.fillcolor('Gray')
        draw_bar(x,-350,w,l[i])
        x = x + w
    screen.update()

# Main Function and Sorting 
def insertion_sort(l):
     global c
     global c2
     global c3
     for i in range( n ):
        value = l[i]
        hole = i
        c = 0
        c2 = 0
        while (hole>0 and l[hole -1] > value):
            l[hole] = l[hole -1]
            c = i
            hole = hole -1
            c2 = hole
        l[hole] = value
        print(l)
        turtle.clear()
        draw_bars(l,n)
        screen.update()
        time.sleep(0.1) #time dealy added for sake for animation 


# Function Call 
insertion_sort(l)

    


   


    
            



