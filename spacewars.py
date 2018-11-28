# SpaceWar by @TokyoEdTech / Written in Python 2.7
# Part II: Player Class / Moving the Player

import pygame
pygame.init()
import os
import random

# Import the Turtle module
import turtle

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    print("America!")
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

# Required by MacOSX to show the window
turtle.fd(0)
# Set the animations speed to the maximum
turtle.speed(0)
# Change the background color
turtle.bgcolor("black")
# Hide the default turtle
turtle.ht()
# This saves memory
turtle.setundobuffer(1)
# This speeds up drawing
turtle.tracer(1)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)


class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


# Create my sprites
player = Player("triangle", "white", 0, 0)

# Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

#controller


# Main game loop
while True:
    player.move()
    if joystick_count != 0:
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)
        print my_joystick.get_button(3)
