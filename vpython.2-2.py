# Question2

from vpython import *
import math
g=9.8
size=0.25
C_drag=0.9
theta=math.pi/4

scene=canvas(width=450,center=vec(0,5,0),align='left',background=vec(0.5,0.5,0))
floor=box(length=30,height=0.01,width=4,color=color.blue,align='left')
ball=sphere(align='left',radius=size,color=color.red,make_trail=True,trail_radius=size/3)
ball.pos=vec(-15,size,0)
ball.v=vec(20*cos(theta),20*sin(theta),0)
oscillation = graph(width = 450, align = 'right')
func = gcurve(graph = oscillation, color=color.blue, width=4)
t=0
dt=0.001

k=0
a=[]
while True:
    rate(1000)
    ball.v += vec(0,-g,0)*dt-C_drag*ball.v*dt
    if ball.pos.y <= size and ball.v.y < 0:
        k += 1
        ball.v.y=-ball.v.y
    elif k == 3:
        break

    ball.pos += ball.v*dt
    a.append(ball.pos.y)
    
    t = t+dt  
    func.plot(pos=(t,ball.v.mag))
        
displacement = math.hypot((ball.pos.x+15),(ball.pos.y-0.25))
h_h=max(a)
              
msg = text(text = 'displacement = '+ str(displacement), pos = vec(-10, 15, 0))
msg = text(text = 'highest height = '+ str(h_h), pos = vec(-10, 18, 0))
              

