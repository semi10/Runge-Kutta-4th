from Tkinter import *
from  ODESolver import *
from numpy import zeros, asarray
from scitools.std import pi, linspace

class Menu:
    def __init__(self, parent):
        self.m = DoubleVar()
        self.beta = DoubleVar()
        self.k = DoubleVar()
        self.g = DoubleVar()
        self.u0 = DoubleVar() 
        self.u1 = DoubleVar()
        self.m.set(1.)
        self.beta.set(0.)
        self.k.set(1.)
        self.g.set(0.)
        self.u0.set(1.)
        self.u1.set(0.)
        
        self.label_1 = Label(parent, text="Mass:")
        self.label_1.grid(row=0, column=0)
        self.entry_1 = Entry(parent, width=8, textvariable=self.m)
        self.entry_1.grid(row=1, column=0)
        
        self.label_2 = Label(parent, text="Damping:")
        self.label_2.grid(row=0, column=1)
        self.entry_2 = Entry(parent, width=8, textvariable=self.beta)
        self.entry_2.grid(row=1, column=1)  
        
        self.label_3 = Label(parent, text="Spring:")
        self.label_3.grid(row=0, column=2)
        self.entry_3 = Entry(parent, width=8, textvariable=self.k)
        self.entry_3.grid(row=1, column=2)
        
        self.label_4 = Label(parent, text="Gravity:")
        self.label_4.grid(row=0, column=3)
        self.entry_4 = Entry(parent, width=8, textvariable=self.g)
        self.entry_4.grid(row=1, column=3)
        
        self.calculate_bt = Button(parent, text="Calculate", command=self.calculate)
        self.calculate_bt.grid(row=2, column=4, padx=20)
        
        self.label_5 = Label(parent, text="Initial Conditions:")
        self.label_5.grid(columnspan=4,row=2,column=0, sticky=S)

        self.label_6 = Label(parent, text="Stretch:")
        self.label_6.grid(row=3,column=0)
        self.entry_5 = Entry(parent, width=8, textvariable=self.u0)
        self.entry_5.grid(row=3, column=1)
        
        self.label_7 = Label(parent, text="Velocity:")
        self.label_7.grid(row=3,column=2)
        self.entry_6 = Entry(parent, width=8, textvariable=self.u1)
        self.entry_6.grid(row=3, column=3)
        
    def calculate(self):    
        
        m, beta, k, g, u0, u1 = \
        self.m.get(), self.beta.get(), self.k.get(), self.g.get(), self.u0.get(), self.u1.get()
        
        u_init = [u0, u1]    # initial condition
        solver = ODESolver(u_init, m, beta, k, g)
    
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
        
              
root = Tk()
root.wm_title("Spring Mass")
gui = Menu(root)
root.mainloop()