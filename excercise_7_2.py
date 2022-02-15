#This is the code for exercise 7 question 2
#The firs step is to import the proper modules etc.
import color

import pygame

import pygame_helper

#The following is the code to prepare to
#and then open up a graphics window with the given dimensions color etc..


#graphics window preperation
pygame.init()

#establishment of variables for the size of the graphics window
width = 400

height = 300

#window dispay information
win = pygame.display.set_mode((width, height))

#dictates the fill color of the window
win.fill(color.lightgray)

#math to make the rectangle 1/3 of the window's height and 1/2 of the length
rect_width = width//2
rect_height = height//3
rect_x =width//2-rect_width//2
rect_y =height//3-rect_height//3
pygame.draw.rect(win, color.darkgray, (rect_x, rect_y, rect_width, rect_height))


#code to create a blue rectangle with the same height and position but different width
#relative to the grey rectangle
blue_width = width//2
blue_height = rect_height
blue_x =  rect_x*1.75
blue_y = rect_y
pygame.draw.rect(win, color.blue, (blue_x, blue_y,
       blue_width, blue_height))




pygame.display.update()



pygame_helper.wait_for_click()