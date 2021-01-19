from vpython import *
'''
something that convey to the next comrades who might concern:

convert each part of the program to a function or method as possible as you can
the main program just contain every function to form the whole progrom
this will help dealing with general states of balls!!

'''


#natural constants
g = 9.8*vec(0,-1,0)   
t , dt = 0 , 0.001    
CM , air_d ,eta = 1.23 , 1.20  , 0.018


#settings about scene and wall
scene = canvas(width=800,height=400,center=vec(10,0,0),background=vec(0.5,0.5,0)) 
d = 18.37    
wall = box(pos=vec(d,0.65,0),length=0.05,height=0.65,width=0.435,color=color.white)
ground = box(pos=vec(d/2,0,0), length=20,height=0.05,width=10,color=color.blue)

#plot:F-t,v-t,y-x,z-x
force_t = graph(width=450, xtitle='Time(s)', ytitle='Force(N)')
func_1 = gcurve(graph=force_t, color=color.blue, width=4)

velocity_t = graph(width=450, xtitle='Time(s)', ytitle='Velocity(m/s)')
func_2 = gcurve(graph=velocity_t, color=color.blue, width=4)

y_x = graph(width=450, xtitle='x_displacement(m)', ytitle='y_displacement(m)')
func_3 = gcurve(graph=y_x, color=color.blue, width=4)

z_x = graph(width=450, xtitle='x_displacement(m)', ytitle='z_displacement(m)')
func_4 = gcurve(graph=z_x, color=color.blue, width=4)


################################################################################################################################
###class ball

class ball(sphere):
    #common datas for class ball
    size, m = 0.035, 0.145
    A = pi*size**2

    
    #method calculating the acceleration from magnus force
    def magnus_a(self):
        global CM , air_d
        return 0.5*self.CM()*air_d*self.A*mag2(self.v)*norm(cross(self.w,self.v))/self.m
    
    def CM(self):
        self.s = 0.035*mag(self.w)/mag(self.v)
        return 1.5*self.s if self.s <= 0.1 else (0.09 + 0.6*self.s)
        
    #method calculating the acceleration from resistant force
    def resistant_a(self):
        global eta , air_d
        return (-0.5*0.3*air_d*self.A*mag2(self.v))*norm(self.v)/self.m

    #method executing the motion of the defined balls
    def motion(self):
        global g, total_a
        total_a = g + self.magnus_a() + self.resistant_a()
        self.v += total_a * dt
        self.pos += self.v * dt
################################################################################################################################
###collections(we generate new types of ball from this database)
fastball_data = {'v':150/3.6,'theta_xz':pi/180,'theta_xy':2*pi/180,'w':vec(0,0,20*pi),'py':2.05,'pz':0.30}
curvedball_data = {'v':125/3.6,'theta_xz':0,'theta_xy':-2*pi/180,'w':vec(0,0,-60*pi),'py':2.05,'pz':0.0}
sinker_data = {'v':145/3.6,'theta_xz':3*pi/180,'theta_xy':pi/180,'w':vec(0,-40*pi,0),'py':2.05,'pz':0.50}
slider_data = {'v':130/3.6,'theta_xz':0,'theta_xy':0,'w':vec(0,140*pi/3,0),'py':2.05,'pz':0.50}

################################################################################################################################
###functions

#function determining if strike or ball
def isstr(ball):
    if ball.pos.y < wall.height/2 or ball.pos.y > 3*wall.height/2 or abs(ball.pos.z)-wall.width/2 > 0:
        return 'ball'
    else:
        return 'strike'

#giving the data of a ball , create a test ball for simulation
def test_ball(data):
    test = ball(pos=vec(0,data['py'],0),radius=0.035,color=color.red,make_trail=True,trail_radius=0.05)   
    test.v = data['v'] * vec(cos(data['theta_xy']), sin(- data['theta_xy']),0)
    test.w = data['w']
    return test

class obj:
    pass

switch = 0
#keyinput
def keyinput(evt):
    global fastball_data , curvedball_data , sinker_data , slider_data , Ball , switch
    choice = {'f':fastball_data,'c':curvedball_data,'s':sinker_data,'d':slider_data}
    if evt.key in choice and switch == 0:
        Ball = test_ball(choice[evt.key])
        switch = 1
scene.bind('keydown', keyinput)

#main program to run the simulation
while True:
    while switch == 1:
        t += dt
        rate(1/(dt*10))
        Ball.motion()
        scene.center = Ball.pos
        func_1.plot(t, mag(total_a)*0.145)
        func_2.plot(t, mag(Ball.v))
        func_3.plot(Ball.pos.x, Ball.pos.y)
        func_4.plot(Ball.pos.x, Ball.pos.z)
        if Ball.pos.x >= d or Ball.pos.y <= ground.height/2 :
            print(f'{isstr(Ball)}')
            switch = 10
    if switch == 10:
        #settings about scene and wall
        scene = canvas(width=800,height=400,center=vec(10,0,0),background=vec(0.5,0.5,0)) 
        d = 18.37    
        wall = box(pos=vec(d,0.65,0),length=0.05,height=0.65,width=0.435,color=color.white)
        ground = box(pos=vec(d/2,0,0), length=20,height=0.05,width=10,color=color.blue)

        #plot:F-t,v-t,y-x,z-x
        force_t = graph(width=450, xtitle='Time(s)', ytitle='Force(N)')
        func_1 = gcurve(graph=force_t, color=color.blue, width=4)

        velocity_t = graph(width=450, xtitle='Time(s)', ytitle='Velocity(m/s)')
        func_2 = gcurve(graph=velocity_t, color=color.blue, width=4)

        y_x = graph(width=450, xtitle='x_displacement(m)', ytitle='y_displacement(m)')
        func_3 = gcurve(graph=y_x, color=color.blue, width=4)

        z_x = graph(width=450, xtitle='x_displacement(m)', ytitle='z_displacement(m)')
        func_4 = gcurve(graph=z_x, color=color.blue, width=4)
        switch = 0

#initial state:
#   1.fastball: v=150(km/hr)  theta=2*pi/180  omega=vec(0,0,20*pi)  (v=136~152(km/hr), rpm=1200)
#   2.curvedball: v=125(km/hr)  theta=-2*pi/180  omega=vec(0,0,-60*pi)  (v=112~128(km/hr), rpm=2000)
#   3.sinker:  v=145(km/hr)  theta=pi/180  omega=vec(0,-40*pi,0)  
#   4.slide ball:  v=130(km/hr) theta=0  omega=vec(0,140*pi/3,0)   (v=128~136(km/hr), rpm=1400)

