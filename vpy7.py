#https://youtu.be/rVL8fOBR_uk
#sorry for the mistake in the video, for the break of the loop, it is 1/4*period not 1/2*period

import numpy as np
from vpython import*

A, N = 0.10, 50
size, m, k, d = 0.06, 0.1, 10.0, 0.4
unit_K = 2*pi/(N*d)
scene = graph(title='Phonon Dispersion Relationship', width=800, height=300, background=vec(0.5,0.5,0), center=vec((N-1)*d/2,0,0), xtitle = 'wavenumber', ytitle = 'omega')
p = gcurve(color = color.cyan, graph = scene)

for n in range(1, N//2):
    wavevector = n*unit_K
    phase = wavevector*np.arange(N)*d
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d 
    T, count, t, dt = 0, 0, 0, 0.0003
    while True:
        t += dt
        spring_len[:-1] = ball_pos[1:] - ball_pos[:-1]  
        spring_len[-1] = ball_pos[0] + N*d -ball_pos[-1]  
        ball_v[1:] += (-(spring_len[:-1]-d)+(spring_len[1:]-d))*k/m*dt 
        ball_v[0] += ((spring_len[0]-d)-(spring_len[-1]-d))*k/m*dt
        ball_pos += ball_v*dt
        
        if (ball_pos[1] - d) < 0:  
            T = t
            p.plot(wavevector, pi/(T*2))  
            break
