from vpython import *         
g = 9.8
N,NN,size = 3,5,0.2
m = 0.5
theta = 30*pi/180
L,k = 2,15000
dt = 0.001
scene = canvas(width = 500,height = 500,center = vec(0.5,-0.4,0),background = vec(0.5,0.5,0))
ceiling = box(pos = vec(0.4,0,0),length = 5,height = 0.005,width = 5,color = color.blue)
position_spring = [vec(0.4-4*size,0,0),vec(0.4-2*size,0,0),vec(0.4,0,0),vec(0.4+2*size,0,0),vec(0.4+4*size,0,0)]
position = [vec(0.4-4*size,-2-m*g/k,0),vec(0.4-2*size,-2-m*g/k,0),vec(0.4,-2-m*g/k,0),vec(0.4+2*size,-2-m*g/k,0),vec(0.4+4*size,-2-m*g/k,0)]
velocity = [vec(0,0,0),vec(0,0,0),vec(0,0,0),vec(0,0,0),vec(0,0,0)]

balls = []
springs = []
for i in range(NN):
    if i < N:
        position[i] -= vec(L*sin(theta),-L*(1-cos(theta)),0) 
    ball = sphere(radius = size,color = color.red)
    ball.pos = position[i]
    ball.v = velocity[i]
    balls.append(ball)
for i in range(NN):
    spring = cylinder(radius = 0.005)
    spring.pos = position_spring[i]
    spring.k = k
    spring.axis = balls[i].pos-position_spring[i]
    springs.append(spring)

def af_col_v(m1, m2, v1, v2, x1, x2): 
    v1_prime =  v1*((m1-m2)/(m1+m2)) + v2*((2*m2)/(m1+m2))
    v2_prime =  v1*((2*m1)/(m1+m2)) + v2*((m2-m1)/(m1+m2))
    return (v1_prime, v2_prime)    
    
t = 0
while True:
    rate(1000)
    t = t + dt
    for i in range(NN):
        springs[i].axis = balls[i].pos-springs[i].pos
        springs_force = -k*(mag(springs[i].axis)-L)*springs[i].axis.norm()
        balls[i].a = vec(0,-g,0)+springs_force/m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        if i < NN-1:
            if (mag(balls[i].pos - balls[i+1].pos) <= 2*size and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0): 
                 (balls[i].v, balls[i+1].v) =  af_col_v ( m, m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)