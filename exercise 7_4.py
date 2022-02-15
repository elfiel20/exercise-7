#This is the code for exercise 7 question 4
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

#This is the code for the darkgrey square
side = height/4
square_x = width//2-side//2
square_y=height//2-side//2
pygame.draw.rect(win, color.darkgray, (square_x, square_y,
       side, side))


#this is the code for the blue square beside it
square_x2 =square_x+side
square_y2 =square_y
pygame.draw.rect(win, color.blue, (square_x2, square_y2,
       side, side))


pygame.display.update()

pygame_helper.wait_for_click()



