#https://youtu.be/mZRombe4pXE


from vpython import*
size, m = 0.02, 0.2
L, k = 0.2 , 20
omega = [0.1*i + 0.7*sqrt(k/m) for i in range(1, int(0.5*sqrt(k/m)/0.1))]
b = 0.05 * m * sqrt(k/m)

power = graph(width = 800, xtitle = 'omega_d', ytitle = 'steady_power', background = vec(0.5, 0.5, 0))
p = gcurve(color = color.cyan, graph = power)
class obj: pass
wall_left, ball, spring = obj(), obj(), obj()

count = 0
a = []
c = []
for omega_d in omega:
    T = 2*pi/omega_d
    ball.pos = vec(L, 0, 0)
    ball.v = vec(0, 0, 0)
    ball.m = m
    spring.pos = vec(0, 0, 0)
    P = 0
    t, dt =0, 0.001
    while True:
        spring.axis = ball.pos - spring.pos
        spring_force = -k*(mag(spring.axis) - L)*norm(spring.axis)
        f = -b*ball.v
        F = 0.1*sin(omega_d*t)*vec(1, 0, 0)
        ball.a = (spring_force + f + F) / ball.m
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        t += dt
        P += dot(F, ball.v)*dt
        if t > 70:
            p.plot(omega_d, P/T)
            a.append(omega_d)
            c.append(P/T)
            break
for i in range(len(a)):
    if count == 0 and i > 2 and (c[i] - c[i-1]) < 0 and (c[i-1] - c[i-2]) > 0:
        print(a[i-1])
        count = 1
        break