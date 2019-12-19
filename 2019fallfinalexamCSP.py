#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Alexus Crabtree
#Date
#12/19/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl
import random

#create turtle
Turtle = trtl.Turtle()

# Turtle.ht()
Turtle.speed(0)



#movement functions
def up():
    Turtle.setheading(90)
    Turtle.forward(10)

def down():
    Turtle.setheading(270)
    Turtle.forward(10)

def right():
    Turtle.setheading(0)
    Turtle.forward(10)

def left():
    Turtle.setheading(180)
    Turtle.forward(10)

#color/drawing functions
def clear():
    Turtle.clear()

#pensize
Turtle.pensize(10)


#create screen
wn = trtl.Screen()

#bind to keypresses
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(clear, "space")
#listen


#mainloop
wn.listen()
wn.mainloop()