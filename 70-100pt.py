##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
#my first beautiful window
rectangle = drawpad.create_rectangle(260,200,410,540, fill = 'indian red')
window = drawpad.create_rectangle(280,250,330,320, fill = 'light sky blue')
#vertical line
line = drawpad.create_line(280,285,330,285)
#horizontal line
line = drawpad.create_line(305,250,305,320)
#my second beautiful window
rectangle = drawpad.create_rectangle(350,360,400,440, fill = 'light sky blue')
#vertical line
line = drawpad.create_line(375,360,375,440,)
#horizontal line
line = drawpad.create_line(350,400,400,400)
#-------roof------#
#left side
line = drawpad.create_line(260,200,330,90)
#right side
line = drawpad.create_line(410,200,330,90)
#chimeny
line = drawpad.create_line(370,145,370,110)
line = drawpad.create_line(370,110,390,110)
line = drawpad.create_line(390,170,390,110)
#door
rectangle = drawpad.create_rectangle(320,500,350,540, fill = 'sandy brown')
#doornob
circle = drawpad.create_oval(323,520,325,525, fill = 'brown') 
#grass
rectangle = drawpad.create_rectangle(0,540,800,700, fill = 'lawn green')
root.mainloop()

