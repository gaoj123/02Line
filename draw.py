from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    if x0==x1:  ##Vertical Line
        smallY=min(y0,y1)
        bigY=max(y0,y1)
        for i in range(smallY,bigY+1):
            plot(screen,color,x0,i)
    else:
        m=(A+0.0)/(-B) ##Calculate slope if not undefined
        if y0==y1:  ##Horizontal Line
            smallX=min(x0,x1)
            bigX=max(x0,x1)
            for i in range(smallX,bigX+1):
                plot(screen,color,i,y0)
        elif m>0 and m<1:  ##Octant 1
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
        elif m<0 and m>-1:  ##Octant 8
            d=2*A-B
            while x<=x1:
                plot(screen,color,x,y)
                if d<0:
                    y-=1
                    d-=2*B
                x+=1
                d+=2*A
        elif m<-1:
            d=A-2*B
            while y>=y1:
                plot(screen,color,x,y)
                if d<0:
                    x+=1
                    d+=2*A
                y-=1
                d-=2*B
            
            


