from vpython import *
g=9.8
size=0.25
height=15

scene=canvas(width=800,height=800,center=vec(0,height/2,0),background=vec(0.5,0.5,0))
floor=box(length=30,height=0.01,width=10,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=True,trail_radius=0.05)
msg=text(text='Projectile',pos=vec(-10,5,0))

ball.pos=vec(-15,5,0)
ball.v=vec(6,8,0)
initial=vec(-15,5,0)
a1=arrow(color=color.green,shaftwidth=0.05)
time=0
path=0
dt=0.001
while ball.pos.y>=size:
    rate(1000)
    
    ball.pos=ball.pos+ball.v*dt
    ball.v.y=ball.v.y-g*dt
    a1.pos=ball.pos
    a1.axis=ball.v*0.5
    time+=dt
    path+=((ball.v.x*dt)**2+(ball.v.y*dt)**2)**0.5
    
displacement=((ball.pos.x-initial.x)**2+(ball.pos.y-initial.y)**2)**0.5

msg.visible=False
msg=text(text='disp=',pos=vec(0,0,0))
msg=text(text=str(displacement),pos=vec(4,0,0))
print(displacement)
msg=text(text='time=',pos=vec(0,3,0))
msg=text(text=str(time),pos=vec(4,3,0))
print(time)
msg=text(text='path=',pos=vec(0,6,0))
msg=text(text=str(path),pos=vec(4,6,0))
print(path)
