#https://youtu.be/HhZnQlUyH3Q

#There is a trivial mistake in the vedio,that is ,I forgot to transfer the unit from cm to meter.

#mutual inductance
from vpython import*
import numpy as np

zr, zR = 0.10, 0
r, R = 0.06, 0.10
u = 4*pi*10**(-7)
m, n = 200, 200
current = 1

pos_r = list(vec(r*cos(2*pi*i/n), r*sin(2*pi*i/n), zr) for i in range(n+1))
pos_R = list(vec(R*cos(2*pi*i/n), R*sin(2*pi*i/n), zR) for i in range(n+1))
pos_r, pos_R = np.array(pos_r), np.array(pos_R)

flux_r = 0
for i in range(m):
    dist = np.array(list(vec(r*i/m, 0, zr) for t in range(n))) - pos_R[:-1]  #m rings with point p in x-axis
    flux = vec(0, 0, 0)
    for j in range(n):
        ds = pos_R[j+1] - pos_R[j]
        ds_r = cross(ds, dist[j])
        dr = (dot(dist[j], dist[j]))**0.5
        flux += (u*current/(4*pi))*(ds_r/(dr**3))  #Biot-Savart's law
    flux_r += 2*pi*(r*i/m)*(r/m)*flux.z
print(flux_r)

flux_R = 0
for i in range(m):
    dist = np.array(list(vec(R*i/m, 0, zR) for t in range(n))) - pos_r[:-1]  #m rings with point p in x-axis
    flux = vec(0, 0, 0)
    for j in range(n):
        ds = pos_r[j+1] - pos_r[j]
        ds_R = cross(ds, dist[j])
        dR = (dot(dist[j], dist[j]))**0.5
        flux += (u*current/(4*pi))*(ds_R/(dR**3))
    flux_R += 2*pi*(R*i/m)*(R/m)*flux.z
print(flux_R)