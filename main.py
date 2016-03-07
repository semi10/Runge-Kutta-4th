from Tkinter import *           #GUI Library
from  ODESolver import *        #Runge kutta solver
import matplotlib.pyplot as plt #Plot creation library
from scitools.std import *      #A static analysis tool (math functions)


class Menu:
    #Creation of TKinter widgets
    def __init__(self, parent):        
        #Allocation of text variables   
        self.m = DoubleVar()
        self.beta = DoubleVar()
        self.k = DoubleVar()
        self.g = DoubleVar()
        self.s_init = DoubleVar() 
        self.v_init = DoubleVar()
        self.total_time = DoubleVar()
        self.dt = DoubleVar()
        
        #Creation of Mass Label & Entry
        self.label_1 = Label(parent, text="Mass:")
        self.label_1.grid(row=0, column=0)
        self.entry_1 = Entry(parent, width=8, textvariable=self.m)
        self.entry_1.grid(row=1, column=0, sticky=N)
        
        #Creation of Damping Label & Entry
        self.label_2 = Label(parent, text="Damping:")
        self.label_2.grid(row=0, column=1)
        self.entry_2 = Entry(parent, width=8, textvariable=self.beta)
        self.entry_2.grid(row=1, column=1, sticky=N)  
        
        #Creation of Spring Label & Entry
        self.label_3 = Label(parent, text="Spring:")
        self.label_3.grid(row=0, column=2)
        self.entry_3 = Entry(parent, width=8, textvariable=self.k)
        self.entry_3.grid(row=1, column=2, sticky=N)
        
        #Creation of Gravity Label & Entry
        self.label_4 = Label(parent, text="Gravity:")
        self.label_4.grid(row=0, column=3)
        self.entry_4 = Entry(parent, width=8, textvariable=self.g)
        self.entry_4.grid(row=1, column=3, sticky=N)
        
        #Creation of Initial Condition Label
        self.label_5 = Label(parent, text="Initial Conditions:")
        self.label_5.grid(columnspan=4,row=3,column=0, sticky=S)

        #Creation of Stretch Label & Entry
        self.label_6 = Label(parent, text="Stretch:")
        self.label_6.grid(row=4,column=0, sticky=E)
        self.entry_5 = Entry(parent, width=8, textvariable=self.s_init)
        self.entry_5.grid(row=4, column=1)
        
        #Creation of Velocity Label & Entry
        self.label_7 = Label(parent, text="Velocity:")
        self.label_7.grid(row=4,column=2, sticky=E)
        self.entry_6 = Entry(parent, width=8, textvariable=self.v_init)
        self.entry_6.grid(row=4, column=3)
        
        #Creation of Time parameters Label
        self.label_8 = Label(parent, text ="Time parameters:")
        self.label_8.grid(columnspan=4, row=6, column=0, sticky=S)
        
        #Creation of Time Label & Entry
        self.label_9 = Label(parent, text="Time:")
        self.label_9.grid(row=7, column=0, sticky=E)
        self.entry_7 = Entry(parent, width=8, textvariable=self.total_time)
        self.entry_7.grid(row=7, column=1)
        
        #Creation of dt Label & Entry
        self.label_10 = Label(parent, text="dt:")
        self.label_10.grid(row=7, column=2, sticky=E)
        self.entry_8 = Entry(parent, width=8, textvariable=self.dt)
        self.entry_8.grid(row=7, column=3)
        
        #Creation of text widget
        self.text_1 = Text(parent, width=55, height=14, wrap=WORD) 
        self.text_1.grid(rowspan=9 ,row=0, column=4,sticky=S+N)
        scrl = Scrollbar(parent, command=self.text_1.yview)
        self.text_1.config(yscrollcommand=scrl.set)
        scrl.grid(rowspan=9, row=0, column=4, sticky=N+S+E)
        
        #Creation of Calculate Button
        self.calculate_bt = Button(parent, text="Calculate", command=self.calculate)
        self.calculate_bt.grid(columnspan=2, row=8, column=0, sticky=N+S+E+W, padx=15, pady=10)
        
        #Creation of Test Button
        self.test_bt = Button(parent, text="Test", command=self.test)
        self.test_bt.grid(columnspan=2, row=8, column=2, sticky=N+S+E+W, padx=15, pady=10)
        
        
    def calculate(self):    
        
        m, beta, k, g, s_init, v_init, total_time, dt = \
        self.m.get(), self.beta.get(), self.k.get(), self.g.get(), self.s_init.get(), self.v_init.get(), self.total_time.get(), self.dt.get()
        
        #Check user data
        self.text_1.delete('1.0', END)
        if m <= 0:
            self.text_1.insert('1.0', "Mass value should be greater than zero\n")
        elif beta < 0: 
            self.text_1.insert('1.0', "Damping value must be positive\n")
        elif k <=0:
            self.text_1.insert('1.0', "Spring coefficient value must be greater than zero\n")
        elif g < 0:
            self.text_1.insert('1.0', "Gravity force value must be positive\n")
        elif total_time <= 0: 
            self.text_1.insert('1.0', "Time value must be greater than zero\n")
        elif total_time < dt:
            self.text_1.insert('1.0', "Time step value must be smaller than time value\n")
        elif dt <=0:
            self.text_1.insert('1.0', "Time step value must be greater than zero\n")
        else:
            solver = RungeKutta4th(s_init, v_init, m, beta, k, g)
        
            S, V, T = solver.solve(total_time, dt)
        
            N = int(total_time/dt)   #N - Steps to make
            
            #Show results in right text box
            self.text_1.insert('1.0', "Time(sec):\t\t   Stretch(m):      Velocity(m/s):\n")
            for i in range(N):
                self.text_1.insert("%d.%d" % (i+2, 0) ,"%13.10f %18.15f %18.15f \n" % (T[i] ,S[i], V[i]))
            
            #Create results plot 
            plt.plot(T, S, 'r', T, V, 'b', xlabel='time(sec)', grid='True', legend=('Stretch(m)', 'Velocity(m/s)'), title=('RungeKutta-4th Results'))        
            plt.show()


    def test(self):
        solver = RungeKutta4th(s_init=1, v_init=0, m=1, beta=0, k=1, g=0)
        
        #Set initial values for test conditions 
        self.m.set(1.)
        self.beta.set(0.)
        self.k.set(1.)
        self.g.set(0.)
        self.s_init.set(1.)
        self.v_init.set(0.)
        
        total_time=self.total_time.get()
        dt=self.dt.get()
        
        #Check user data
        self.text_1.delete('1.0', END)
        if total_time <= 0: 
            self.text_1.insert('1.0', "Time value must be greater than zero\n")
        elif total_time < dt:
            self.text_1.insert('1.0', "Time step value must be smaller than time value\n")
        elif dt <=0:
            self.text_1.insert('1.0', "Time step value must be greater than zero\n")
        else:

            N = int(total_time/dt)   #N - Steps to make
            #Create arrays
            V_error = [0.0]*(N+1)
            S_error = [0.0]*(N+1)
            V_exact = [0.0]*(N+1)
            S_exact = [0.0]*(N+1) 
        
            S_solved, V_solved, T = solver.solve(total_time, dt)
        
            self.text_1.insert('1.0', "Time(sec):\t    Stretch Error(m): Velocity Error(m/s):\n")
            
            #Calculate solution by direct method
            for i in range(N):
                S_exact[i] = cos(T[i])
                V_exact[i] = -sin(T[i])
            
                S_error[i] = S_exact[i] - S_solved[i]
                V_error[i] = V_exact[i] - V_solved[i] 
                
                #Insert results in right text box
                self.text_1.insert("%d.%d" % (i+2, 0) ,"%13.10f %18.15f %18.15f \n" % (T[i] ,S_error[i], V_error[i]))
     
            #Create plot of Error Values
            plt.figure(1)    
            plt.plot(T, S_error, 'r', T, V_error, 'b', xlabel='time(sec)', grid='True', \
                 legend=('Stretch(m)', 'Velocity(m/s)'), title=('Error Values'))  
        
            #Create plot of RungeKutta-4th Results
            plt.figure(2)
            plt.plot(T, S_solved, 'r', T, V_solved, 'b', xlabel='time(sec)', grid='True', \
                 legend=('Stretch(m)', 'Velocity(m/s)'), title=('RungeKutta-4th Results')) 
        
            #Create plot of results calculated by direct method
            plt.figure(3)
            plt.plot(T, S_exact, 'r', T, V_exact, 'b', xlabel='time(sec)', grid='True', \
                 legend=('cos(t)', '-sin(t)'), title=('Exact Values')) 
        
     
root = Tk()
root.wm_title("Spring Mass")
gui = Menu(root)
root.mainloop()