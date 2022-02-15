#This is the code for exercise 1 question 1
#The firs step is to import the proper modules etc.
import color

import pygame

import pygame_helper

#The following is the code to prepare to
#and then open up a graphics window with the given dimensions color etc..

pygame.init()

#Below are the dimensions (in pixels) of the graphic window
width = 400

height = 300

win = pygame.display.set_mode((width, height))

win.fill(color.lightgray)


#this is the code for the rectangle to be half the width of the full window and a third the height
#after establishing the dimensions with variable name there is then the command for pygame to draw the rectangle
rect_width = width//2
rect_height = height//3
rect_x =width//2-rect_width//2
rect_y =height//3-rect_height//3
pygame.draw.rect(win, color.darkgray, (rect_x, rect_y, rect_width, rect_height))



#this (below) tells pygame to display the changes to the window
pygame.display.update()

#This (below) tells pygame to wait for the user to click before closing the window
pygame_helper.wait_for_click()