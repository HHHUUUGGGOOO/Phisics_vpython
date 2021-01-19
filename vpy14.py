from vpython import *
from numpy import *

N = 100
R, lamda = 1.0, 500E-9
d = 100E-6
c = 299792458
k = 2*pi/lamda

dx, dy = d/N, d/N
scene1 = canvas(align = 'left', height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene2 = canvas(align = 'right', x=600, height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene1.lights, scene2.lights = [], []
scene1.ambient, scene2.ambient = color.gray(0.99), color.gray(0.99)
side = linspace(-0.01*pi, 0.01*pi, N)
x,y = meshgrid(side,side)

E_field = 0 
# change this to calculate the electric field of diffraction of the aperture
for i in range(N):
    for j in range(N):
        X, Y = (i-N/2)*dx, (j-N/2)*dx
        if X**2 + Y**2 <= (d/2)**2:
                E_field += cos(k*x*X/R+k*y*Y/R)/R

Inte = abs(E_field) ** 2   #intensity
maxI = amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas = scene1, pos=vector(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
            color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))

rad = 0
for i in range(int(N/2), N):
        if Inte[int(N/2), i] < maxI*0.01:
                theta = (i-N/2)*0.01*2*pi/N   #side length
                rad = (i-N/2)*0.01/N
                break


Inte = abs(E_field)
maxI = amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas = scene2, pos=vector(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
            color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))

print(f'radius = {rad}')
print(f'real theta = {theta}')
print(f'rayleigh criterion = {1.22*lamda/d}')
