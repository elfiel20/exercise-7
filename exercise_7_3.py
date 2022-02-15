#This is the code for exercise 7 question 3
#The firs step is to import the proper modules etc.
import color

import pygame

import pygame_helper

#The following is the code to prepare to
#and then open up a graphics window with the given dimensions color etc..

pygame.init()

width = 400

height = 300

win = pygame.display.set_mode((width, height))

win.fill(color.lightgray)


#This is the code to have pygame draw a centered grey square with sides 1/4 the height of the window
side = height/4
square_x = width//2-side//2
square_y=height//2-side//2
pygame.draw.rect(win, color.darkgray, (square_x, square_y,
       side, side))


pygame.display.update()

pygame_helper.wait_for_click()
