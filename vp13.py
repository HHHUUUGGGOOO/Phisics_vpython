from vpython import*

f_d = 120    #120(Hz)
w = 2*pi*f_d
R = 30   #30(ohm)
C = 20*10**(-6)   #20(uF)
L = 0.2   #200(mH)
T = 1/f_d
#(parameter here)

t = 0
dt = 1/(f_d*5000)   #5000simulation points per cycle

scene1 = graph(align='left', xtitle='t', ytitle='i(A):blue, v(100V):red', background=vector(0.2, 0.6, 0.2))
scene2 = graph(align='left', xtitle='t', ytitle='Energy(J)', background=vector(0.2, 0.6, 0.2))

i_t = gcurve(color=color.blue, graph=scene1)
v_t = gcurve(color=color.red, graph=scene1)
E_t = gcurve(color=color.red, graph=scene2)

count, time, E_decay = 0, 0, 0   #time = decay time after 12T
max_i, max_v = 0, 0
t_v, t_i, min_i, amp_i = 0, 0, 0, 0
Z_real, Z_ima = R, (w*L-1/(w*C))
theo_amp = 36/((Z_real**2 + Z_ima**2)**0.5)
theo_phi = atan(Z_ima/Z_real)*180/pi
Q, i = 0, 0
while t <= 20*T:
    rate(f_d*5000)
    t += dt
    
    #(1)solve the circuit numerically
    if 0 <= t <= 12*T:
        v = 36*sin(w*t)
    else:
        v = 0
    v_c, v_r = Q/C, i*R
    di = (v-v_c-v_r)*dt/L
    i += di
    Q += i*dt
    
    #(2)plot
    v_t.plot(pos=(t/T, v/100))
    i_t.plot(pos=(t/T, i))
    E_t.plot(pos=(t/T, (C*v_c**2/2+L*i**2/2)))

    #(3)At 9T, amplitude & phase constant
    if 9*T <= t <= 10*T:
        if i > max_i:
            max_i = i
            t_i = t
        if i < min_i:
            min_i = i
        if v > max_v:
            max_v = v
            t_v = t
        amp_i = (max_i - min_i)/2
    
    #(4)after 12T , decay
    if t >= 12*T:
        if E_decay == 0:
            E_decay = C*v_c**2/2+L*i**2/2
        time += dt
        if (C*v_c**2/2+L*i**2/2) <= 0.1*E_decay and count == 0:
            print(f'real amplitude = {amp_i}')
            print(f'real phase constant = {(t_i-t_v)/T*360}')
            print(f'theoretical amplitude = {theo_amp}')
            print(f'theoretical phase constant = {theo_phi}')
            print(f'decay time = {time}')
            count = 1
