from numpy import zeros, asarray
from scitools.std import pi, linspace

class ODESolver:
    def __init__(self, u_init, m, beta, k, g): 
        u_init = asarray(u_init)
        self.u_init, self.m, self.beta, self.k, self.g = u_init, float(m), float(beta), float(k), float(g)
        
    def f(self, u):
        u0, u1 = u
        f = asarray([u1, 1./self.m*(self.g - self.beta*u1 - self.k*u0)])
        return f

    def solve(self, time_points):
        """Compute u for t values in time_points list."""
        self.t = asarray(time_points)
        n = self.t.size
        self.u = zeros((n, 2))
        # Assume self.t[0] corresponds to self.U0
        self.u[0] = self.u_init

        #Time loop
        for i in range(n-1):
            self.i = i
            self.u[i+1] = self.advance()
        return self.u, self.t

    def advance(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i+1] - t[i]
        K1 = dt*f(u[i])
        K2 = dt*f(u[i] + 0.5*K1)
        K3 = dt*f(u[i] + 0.5*K2)
        K4 = dt*f(u[i] + K3)
        u_new = u[i] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return u_new

# Test case: u = cos(t) 
if __name__ == '__main__':
    u_init = [1, 0]    # initial condition
    solver = ODESolver(u_init, m=1, beta=0, k=1, g=0)
    
    nperiods = 3     # no of oscillation periods
    T = 2*pi*nperiods
    npoints_per_period = 20
    n = npoints_per_period*nperiods
    t_points = linspace(0, T, n+1)
    
    u, t = solver.solve(t_points)
    
    # u is an array of [u0,u1] pairs for each time level,
    # get the u0 values from u for plotting
    u0_values = u[:, 0]
    u1_values = u[:, 1]
    
    print '    Second:     \tPosition:\t     Velocity:'
    for i,j,k in zip(t,u0_values, u1_values):
        print '%-19.15f %19.15f %19.15f' % (i,j, k)
    