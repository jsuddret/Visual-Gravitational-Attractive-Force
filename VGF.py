# by jake suddreth
from tkinter import *
import random
import time

# retrieve values from list as float
x = [float(line.strip()) for line in open('x_values.txt')]
y = [float(line.strip()) for line in open('y_values.txt')]
index = 0

# create window, set attributes
window = Tk()
h = 800
w = 1200
canvas = Canvas(window, width=w, height=h, background='black')
window.title('VGF')
canvas.pack()

# define radius of circle
R = 12.5
# draw ovals and corresponding text
fixed_object = canvas.create_oval(w/2-R-500, h/2-R, w/2+R-500, h/2+R, fill='white')
fixed_text = canvas.create_text(w/2-500, h/2, text='1kg')
orbiting_object = canvas.create_oval(w/2-R+500, h/2-R, w/2+R+500, h/2+R, fill='white')
orbiting_text = canvas.create_text(w/2+500, h/2, text='1kg')

while index < len(x) - 1:
    # move ovals and corresponding text with respect to the x and y coordinates
    canvas.move(fixed_object, -1 * (x[index + 1] - x[index]), -1 * (y[index + 1] - y[index]))
    canvas.move(fixed_text, -1 * (x[index + 1] - x[index]), -1 * (y[index + 1] - y[index]))
    canvas.move(orbiting_object, (x[index+1] - x[index]), (y[index+1] - y[index]))
    canvas.move(orbiting_text, (x[index+1] - x[index]), (y[index+1] - y[index]))
    # update canvas, increase index to iterate 
    window.update()
    index += 1

# project
window.mainloop()
