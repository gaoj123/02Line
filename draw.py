from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    m=(A+0.0)/(-B)
    if m>0 and m<1:  ##Octant 1
        d=2*A+B
        while x<=x1:
            plot(screen,color,x,y)
            if d>0:
                y+=1
                d+=2*B
            x+=1
            d+=2*A
    elif m>1:  ##Octant 2
        d=A+2*B
        while y<=y1:
            plot(screen,color,x,y)
            if d<0:
                x+=1
                d+=2*A
            y+=1
            d+=2*B


