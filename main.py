from display import *
from draw import *

screen = new_screen()
color=[255, 203, 53]
#color = [ 0, 0, 255 ]

draw_line(250,280,230,320, screen, color) #Octant 7/3
draw_line(230,320,210,280, screen, color) #Octant 2/6  
draw_line(210,280,160,280, screen, color) #Horizontal Line: Slope 0
draw_line(160,280,130,270, screen, color) #Octant 1/5
draw_line(120,260,130,270, screen, color) #Slope 1
draw_line(120,260,140,250, screen, color) #Octant 8/4
draw_line(140,250,120,240, screen, color)
draw_line(120,240,160,230, screen, color)
draw_line(160,230,170,200, screen, color)
draw_line(170,200,190,180, screen, color)
draw_line(190,180,190,240, screen, color) #Vertical Line: Slope undefined
draw_line(190,240,210,220, screen, color) #Slope -1
draw_line(260,220,210,220, screen, color)
draw_line(260,220,280,210, screen, color)
draw_line(290,230,280,210, screen, color)
draw_line(290,230,350,240, screen, color)
draw_line(380,230,350,240, screen, color)
draw_line(380,230,370,250, screen, color)
draw_line(380,280,370,250, screen, color)
draw_line(380,280,390,300, screen, color)
draw_line(340,260,390,300, screen, color)
draw_line(340,260,280,270, screen, color)
draw_line(250,280,280,270, screen, color)

display(screen)
save_extension(screen, 'img.png')
