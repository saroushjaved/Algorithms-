
# Name : Selection Sort Animation
# Author : Soroush Javed Sulehri
# Liscence : MIT
# Sorting Series : Part 1(b)
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
screen.title('Selection Sort')
turtle.speed(0)
turtle.hideturtle()

# Taking number of bars as input
n = int(input("Enter the number of bars to randomly distribute (10-100) : "))
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
        elif i == c2: turtle.fillcolor("turquoise")
        else:turtle.fillcolor('Gray')
        draw_bar(x,-350,w,l[i])
        x = x + w
    screen.update()

# Main Function and Sorting 
def Sort(l):
    for i in range(len(l)):
        global c
        global c2
        c = i
        for j in range(i+1, len(l)):
            c2 = j
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
        screen.update()
        turtle.clear()
        draw_bars(l,n)
        screen.update()
        time.sleep(0.3)
    

# Function Call 
Sort(l)

    


   


    
            



