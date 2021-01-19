from vpython import*

g=9.8
size,m=0.05,0.2
L,k=0.5,[15,12,17]
v=[1,2,2.2]
d=[-0.06,0,-0.1]

scene=canvas(width=300,height=400,center=vec(0.4,0.2,0),align='left',background=vec(0.5,0.5,0))
floor=box(pos=vec(0.4,0,0),length=0.8,height=0.005,width=0.8,color=color.blue)
wall=box(pos=vec(0,0.05,0),length=0.01,height=0.1,width=0.8)
dt=0.001
t=0

oscillation1=graph(width=300,align='right')
func1=gcurve(graph=oscillation1,color=color.blue,width=2)
func2=gcurve(graph=oscillation1,color=color.red,width=2)
oscillation2=graph(width=300,align='right')
func3=gcurve(graph=oscillation2,color=color.blue,width=2)
func4=gcurve(graph=oscillation2,color=color.red,width=2)

balls=[]
springs=[]
for i in range(3):
    ball=sphere(pos=vec(L+d[i],size,(i-1)*3*size),radius=size,color=color.red)
    ball.v=vec(v[i],0,0)
    balls.append(ball)
for i in range(3):
    spring=helix(pos=vec(0,size,(i-1)*3*size),radius=0.02,thickness=0.01)
    spring.k=k[i]
    spring.axis=balls[i].pos-spring.pos
    springs.append(spring)

a=[]
b=[]
while True:
    rate(1000)
    t = t + dt
    E=0
    U=0
    for i in range(3):
        springs[i].axis=balls[i].pos-springs[i].pos
        springs_force=-springs[i].k*(mag(springs[i].axis)-L)*springs[i].axis.norm()
        balls[i].a=springs_force/m
        balls[i].v+=balls[i].a*dt
        balls[i].pos+=balls[i].v*dt
        E += 0.5*m*(mag(balls[i].v)**2)
        U += 0.5*springs[i].k*((mag(springs[i].axis)-L)**2)
        a.append(E)
        b.append(U)
    func1.plot(t,sum(a)/(t*1000))
    func2.plot(t,sum(b)/(t*1000))
    func3.plot(t,E)
    func4.plot(t,U)
    