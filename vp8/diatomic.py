from vpython import * 
size, m_o, m_c, k_bond = 31E-12, 16.0/6E23, 12.0/6E23, 18600.0    
d = 2.5*size  
dt = 1E-16 
 
class CO_molecule:     
    def __init__(self, pos, axis):         
        self.O = sphere(pos = pos, radius = size, color = color.red)         
        self.C = sphere(pos = pos+axis, radius = size, color = color.blue)         
        self.bond = cylinder(pos = pos, axis = axis, radius = size/2.0, color = color.white)         
        self.O.m = m_o         
        self.C.m = m_c         
        self.O.v = vector(0, 0, 0)         
        self.C.v = vector(0, 0, 0)         
        self.bond.k = k_bond 
 
    def bond_force_on_O(self):          
        return self.bond.k*(mag(self.bond.axis)-d)*norm(self.bond.axis) 
 
    def time_lapse(self, dt):       
        self.C.a = - self.bond_force_on_O() / self.C.m         
        self.O.a = self.bond_force_on_O() / self.O.m         
        self.C.v += self.C.a * dt         
        self.O.v += self.O.a * dt         
        self.C.pos += self.C.v * dt          
        self.O.pos += self.O.v * dt                
        self.bond.axis = self.C.pos - self.O.pos         
        self.bond.pos = self.O.pos              
    
    def com(self):    #apply the formula of COM
        return (self.O.pos*self.O.m + self.C.pos*self.C.m)/(self.O.m + self.C.m)
 
    def com_v(self):    
        return (self.O.v*self.O.m + self.C.v*self.C.m)/(self.O.m + self.C.m)              
    
    def v_P(self):     
        return self.bond.k*(mag(self.bond.axis)-d)**2/2
 
    def v_K(self): #the horizontal component of velocity
        temp_O = self.O.v - self.com_v()
        temp_C = self.C.v - self.com_v()
        cos_O = dot(temp_O, norm(self.O.pos-self.C.pos))
        cos_C = dot(temp_C, norm(self.C.pos-self.O.pos))
        return cos_O**2*self.O.m/2 + cos_C**2*self.C.m/2
 
    def r_K(self): #the vertical component of velocity
        temp_O = self.O.v - self.com_v()
        temp_C = self.C.v - self.com_v()
        sin_O = mag(cross(temp_O, norm(self.O.pos-self.C.pos)))
        sin_C = mag(cross(temp_C, norm(self.C.pos-self.O.pos)))
        return sin_O**2*self.O.m/2 + sin_C**2*self.C.m/2
 
    def com_K(self):    
        return (self.O.m+self.C.m)*(mag2(self.com_v()))/2

def collision(a1, a2):   #elastic collision  
    v1prime = a1.v - 2 * a2.m/(a1.m+a2.m) *(a1.pos-a2.pos)  * dot (a1.v-a2.v, a1.pos-a2.pos) / mag(a1.pos-a2.pos)**2     
    v2prime = a2.v - 2 * a1.m/(a1.m+a2.m) *(a2.pos-a1.pos)  * dot (a2.v-a1.v, a2.pos-a1.pos) / mag(a2.pos-a1.pos)**2     
    return v1prime, v2prime 
 
if __name__ == '__main__':     
    a = CO_molecule(pos=vector(0, 0, 0), axis = vector(2.6*size, 0, 0))     
    a.O.v = vector(1.0, 1.0, 0)     
    a.C.v = vector(2.0, -1.0, 0)     
    a.time_lapse(dt)     
    print(a.bond_force_on_O(), a.com(), a.com_v(), a.v_P(), a.v_K(), a.r_K(), a.com_K()) 
