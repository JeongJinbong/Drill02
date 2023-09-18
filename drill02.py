from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

a= True

x= 0
y=90
r=200
theta = 0
while(1):
 if(a):   
  if(y==90 and x==0):
     while (x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x= x+2
        delay(0.01)
  if(y== 90 and x==800):
     while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y= y+2
        delay(0.01)
  if(y== 600 and x==800):
     while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x= x-2
        delay(0.01)
  if(y== 600 and x== 0):
     while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.01)
        a= False
  if(a ==False):
     x= 300
     y= 200
     for theta in range (0,5):
         clear_canvas_now()
         grass.draw_now(400,30)
         x= x+r* math.cos(theta)
         y= y+r * math.sin(theta)
         character.draw_now(x,y)
         delay(0.1)
         if(theta==5-1):
           a=True
           x=0
           y=90

    


     
    
