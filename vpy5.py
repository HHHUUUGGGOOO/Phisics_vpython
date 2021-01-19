#https://youtu.be/x7kaWpdvsuw


from vpython import *
import numpy as np

def G_force(s1,s2):
    return -G*s1.m*s2.m/mag2(s1.pos-s2.pos)*(s1.pos-s2.pos).norm()

G = 6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun': 1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun': 6.95E8*10} 
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi / 180.0

scene = canvas(width = 800, height = 800, center = vec(0,0,0),background=vec(0,0,0))
earth = sphere(canvas = scene,m = mass['earth'],radius = radius['earth'],texture = {'file':textures.earth})
moon = sphere(canvas = scene,m = mass['moon'],radius = radius['moon'],color = color.white)

ini_earth = moon_orbit['r']*(mass['moon']/(mass['earth'] + mass['moon']))
ini_moon = moon_orbit['r']*(mass['earth']/(mass['earth'] + mass['moon']))
earth.pos = vec(earth_orbit['r'] - ini_earth*cos(theta),-ini_earth*sin(theta),0)
moon.pos = vec(earth_orbit['r'] + ini_moon*cos(theta),ini_moon*sin(theta),0)
earth.v = vec(0,0,moon_orbit['v']*(mass['moon']/(mass['earth'] + mass['moon']))-earth_orbit['v'])
moon.v = vec(0,0,-moon_orbit['v']*(mass['earth']/(mass['earth'] + mass['moon'])) - earth_orbit['v'])

sun = sphere(canvas = scene,pos = vec(0,0,0),m = mass['sun'], r = radius['sun'], color = color.orange, emissive = True)
scene.lights = []
local_light(pos = vec(0,0,0))
angular = arrow(color = color.orange, shaftwidth = radius['moon'])

t = 0
t1 = 0
b = 0
dt = 60*60
while True:
    rate(24*365/2)
    ini = norm(cross(moon.pos - earth.pos, moon.v - earth.v)).x
    moon.a = (G_force(moon,earth) + G_force(moon,sun))/moon.m
    earth.a = (G_force(earth,moon) + G_force(earth,sun))/earth.m
    
    moon.v +=  moon.a*dt
    moon.pos += moon.v*dt
    
    earth.v += earth.a*dt
    earth.pos += earth.v*dt
    
    angular.pos = earth.pos
    angular.axis = cross(moon.pos - earth.pos, moon.v - earth.v) / 3000
    fin = norm(cross(moon.pos - earth.pos, moon.v - earth.v)).x
    scene.center = earth.pos
    t += dt
    
    if fin - ini > 0 and fin * ini < 0 and b == 1:
        print("The period of the moon's precession is\t" + str((t - t1)/(86400*365)) + "\tyears")
        break
    if fin - ini > 0 and fin * ini < 0 and b == 0:
        t1 = t
        b = 1
    
