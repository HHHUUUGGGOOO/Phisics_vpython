from vpython import*
import numpy as np

size, m = 0.02, 0.2
L, k, K = 0.2, 20, 5
amplitude = 0.03
b1 = 0.05 * m * sqrt(k/m)
b2 = 0.0025 * m * sqrt(k/m)
omega_d = sqrt((k+K)/m)
T = 2*pi/omega_d

scene = canvas(width = 300, height = 400, fov = 0.03, center = vec(0.3, 0, 0), align = 'left', background = vec(0.5, 0.5, 0))
wall_left = box(pos = vec(0, 0, 0), length = 0.005, width = 0.3, height = 0.3, color = color.blue)
wall_right = box(pos = vec(3*L, 0, 0), length = 0.005, width = 0.3, height = 0.3, color = color.blue)
ball_1 = sphere(radius = size, color = color.red)
ball_2 = sphere(radius = 0.015, color = color.red)
spring_1 = helix(radius = 0.015, thickness = 0.01)
spring_2 = helix(radius = 0.015, thickness = 0.01)
spring_3 = helix(radius = 0.005, thickness = 0.001)
oscillation1 = graph(width = 300, align = 'right', xtitle = 't', ytitle = 'x', background = vec(0.5, 0.5, 0))
x = gcurve(color = color.red, graph = oscillation1)
oscillation2 = graph(width = 300, align = 'right', xtitle = 't', ytitle = 'average_power', background = vec(0.5, 0.5, 0))
p = gdots(color = color.cyan, graph = oscillation2)

ball_1.pos, ball_2.pos = vec(L, 0, 0), vec(2*L, 0, 0)
ball_1.v, ball_2.v = vec(0, 0, 0), vec(0, 0, 0)
ball_1.m, ball_2.m = m, m
spring_1.pos,spring_2.pos= wall_left.pos, wall_right.pos
work = 0
n = 1
t, dt = 0, 0.001
while True:
    rate(1000)
    spring_1.axis = ball_1.pos - spring_1.pos
    spring_3.pos = ball_1.pos
    spring_2.axis = ball_2.pos - spring_2.pos
    spring_3.axis = ball_2.pos - ball_1.pos
    spring_force_1 = -k*(mag(spring_1.axis) - L)*norm(spring_1.axis)
    spring_force_2 = -k*(mag(spring_2.axis) - L)*norm(spring_2.axis)
    spring_force_3 = -K*(mag(spring_3.axis) - L)*norm(spring_3.axis)
    f1 = -b1 * ball_1.v
    f2 = -b2 * ball_2.v
    F1 = 0.1*sin(omega_d*t)*norm(spring_1.axis)
    ball_1.a = (spring_force_1 + f1 + F1 - spring_force_3) / ball_1.m
    ball_2.a = (spring_force_2 + f2 + spring_force_3) / ball_2.m 
    ball_1.v += ball_1.a*dt
    ball_2.v += ball_2.a*dt
    ball_1.pos += ball_1.v*dt
    ball_2.pos += ball_2.v*dt
    x.plot(pos = (t, ball_1.pos.x))
    work += dot(F1, ball_1.v)*dt
    t += dt
    if t / T > n:
        p.plot(pos = (t, work/T))
        n += 1
        work = 0