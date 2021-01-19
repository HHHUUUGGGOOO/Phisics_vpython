# Question2

from vpython import *
import math
g=9.8
size=0.25
C_drag=0.3

scene=canvas(width=450,center=vec(0,5,0),align='left',background=vec(0.5,0.5,0))
ball=sphere(align='left',radius=size,color=color.red,make_trail=True,trail_radius=size)
ball.pos=vec(-10,10,0)
ball.v=vec(0,0,0)
initial=vec(0,0,0)
oscillation = graph(width = 450, align = 'right')
func = gcurve(graph = oscillation, color=color.blue, width=4)
t=0
dt=0.001

while True:
    rate(1000)
    initial=ball.v
    ball.v += vec(0,-g,0)*dt-C_drag*ball.v*dt
    ball.pos += ball.v*dt
    t = t+dt  
    if ball.v.mag-initial.mag < 0.0001:
        msg = text(text = 'terminal speed = '+ str(ball.v.mag), pos = vec(-15, 15, 0))
        break
    func.plot(pos=(t,ball.v.mag))
print(ball.v.mag)
              