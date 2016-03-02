from scitools.std import pi

class RungeKutta4th:
    def __init__(self, s_init, v_init, m, beta, k, g): 
        self.s_init, self.v_init, self.m, self.beta, self.k, self.g = float(s_init) ,float(v_init), float(m), float(beta), float(k), float(g)
        
    def f_s(self, u1):
        return u1
    
    def f_v(self, u0, u1):
        return 1./self.m*(self.g - self.beta*u1 - self.k*u0)
    

    def solve(self, total_time, dt):
        f_s = self.f_s
        f_v = self.f_v
        
        N = int(total_time/dt)   #N - Steps to make
        S = [0.0]*(N+1)          #S - Empty list of spring stretch
        V = [0.0]*(N+1)          #V - List of spring velocity
        T = [0.0]*(N+1)          #T - Time points
        
        S[0] = self.s_init
        V[0] = self.v_init
                
        #Time loop
        for i in range(N):
            k1_s = dt*f_s(V[i])
            k1_v = dt*f_v(S[i], V[i])
            
            k2_s = dt*f_s(V[i]+0.5*k1_v)
            k2_v = dt*f_v(S[i]+0.5*k1_s, V[i]+0.5*k1_v)
            
            k3_s = dt*f_s(V[i]+0.5*k2_v)
            k3_v = dt*f_v(S[i]+0.5*k2_s, V[i]+0.5*k2_v)
            
            k4_s = dt*f_s(V[i]+k3_v)
            k4_v = dt*f_v(S[i]+k3_s, V[i]+k3_v)
            
            S[i+1] = S[i] + (1/6.0)*(k1_s + 2*k2_s + 2*k3_s + k4_s)
            V[i+1] = V[i] + (1/6.0)*(k1_v + 2*k2_v + 2*k3_v + k4_v)
            T[i+1] = dt*(i+1)
        return S, V, T
        

# Test case: u = cos(t) 
if __name__ == '__main__':
    solver = RungeKutta4th(s_init=1, v_init=0, m=1, beta=0, k=1, g=0)
    
    nperiods = 3     # no of oscillation periods
    total_time = 2*pi*nperiods
    dt = pi/10
    
    S, V, T = solver.solve(total_time, dt)
    
    print 'Time(sec):   \t\tPosition(m):\t Velocity(m/sec):'
    for i, j, k in zip(T, S, V):
        print '%18.15f %18.15f %19.15f' % (i, j, k)   