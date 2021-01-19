#https://youtu.be/LE1qGozbaFs

from vpython import * 
from diatomic import * #use the module in "diatomic.py" created by myself
 
N = 20    #numbers of particles   
L = ((24.4E-3/(6E23))*N)**(1/3.0)/50  #center(0,0,0),the space ranges from (-L,0,0) to (L,0,0)
m = 14E-3/6E23   #average mass of CO  
k, T = 1.38E-23, 298.0     #coefficient of elasticity & temperature
initial_v = (3*k*T/m)**0.5   
 
scene = canvas(width = 400, height =400, align = 'left', background = vec(1, 1, 1)) 
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.4, color = color.yellow )  
energies = graph(width = 600, align = 'left', ymin=0) 
c_avg_com_K = gcurve(color = color.green) 
c_avg_v_P = gcurve(color = color.red) 
c_avg_v_K = gcurve(color = color.purple) 
c_avg_r_K = gcurve(color = color.blue) 
 
COs=[] 
 
for i in range(N):     #randomly produce these vectors
    O_pos = vec(random()-0.5, random()-0.5, random()-0.5)*L  
    CO = CO_molecule(pos=O_pos, axis = vector(1.0*d, 0, 0)) 
    CO.C.v = vector(initial_v*random(), initial_v*random(), initial_v*random())
    CO.O.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) 
    COs.append(CO)    

total_com_K = 0  #set some parameters
total_v_K = 0
total_v_P = 0
total_r_K = 0
times = 0       
dt = 5E-16 
t = 0 
while True:     
    rate(3000) 
    t += dt
    for CO in COs:         
        CO.time_lapse(dt)           
        for i in range(N-1):        
            for j in range(i+1,N): #the condition to check if a collision happens
                if mag(COs[i].C.pos-COs[j].C.pos)<=2*size and dot(COs[i].C.pos-COs[j].C.pos, COs[i].C.v-COs[j].C.v)<=0:
                    COs[i].C.v, COs[j].C.v = collision(COs[i].C, COs[j].C)
                if mag(COs[i].C.pos-COs[j].O.pos)<=2*size and dot(COs[i].C.pos-COs[j].O.pos, COs[i].C.v-COs[j].O.v)<=0:
                    COs[i].C.v, COs[j].O.v = collision(COs[i].C, COs[j].O)
                if mag(COs[i].O.pos-COs[j].C.pos)<=2*size and dot(COs[i].O.pos-COs[j].C.pos, COs[i].O.v-COs[j].C.v)<=0:
                    COs[i].O.v, COs[j].C.v = collision(COs[i].O, COs[j].C) 
                if mag(COs[i].O.pos-COs[j].O.pos)<=2*size and dot(COs[i].O.pos-COs[j].O.pos, COs[i].O.v-COs[j].O.v)<=0:
                    COs[i].O.v, COs[j].O.v = collision(COs[i].O, COs[j].O)
                
    for CO in COs: 
        if L-abs(CO.C.pos.x)<=size:
            CO.C.v.x = (-1)*CO.C.v.x  
        if L-abs(CO.C.pos.y)<=size:
            CO.C.v.y = (-1)*CO.C.v.y            
        if L-abs(CO.C.pos.z)<=size:
            CO.C.v.z = (-1)*CO.C.v.z            
        if L-abs(CO.O.pos.x)<=size:
            CO.O.v.x = (-1)*CO.O.v.x            
        if L-abs(CO.O.pos.y)<=size:
            CO.O.v.y = (-1)*CO.O.v.y            
        if L-abs(CO.O.pos.z)<=size:
            CO.O.v.z = (-1)*CO.O.v.z
        
        total_com_K += CO.com_K()
        total_v_K += CO.v_K()
        total_v_P += CO.v_P()
        total_r_K += CO.r_K()
    
    times += 1
    avg_com_K = total_com_K/times
    avg_v_K = total_v_K/times
    avg_v_P = total_v_P/times
    avg_r_K = total_r_K/times

    c_avg_com_K.plot(times,avg_com_K)
    c_avg_v_P.plot(times,avg_v_P)
    c_avg_v_K.plot(times,avg_v_K)
    c_avg_r_K.plot(times,avg_r_K)
     
 
