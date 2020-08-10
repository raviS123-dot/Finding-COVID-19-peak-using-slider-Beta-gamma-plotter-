import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider #Button, RadioButtons
import pandas as pd
from scipy.integrate import odeint

a=[]
b=[]
c=[]
count = 0
for x in range(100):
        count = count+1
        y_infected = 0.001*x*x*x-0.0226*x*x-0.6304*x+17.387  #infected best fit equation of real data 
        y_recovered = 0.0013*x*x*x-0.1304*x*x+3.8718*x-23.092  #recovered best fit equation of real data
        a.append(x)
        b.append(y_infected)
        c.append(y_recovered)
        

N = 6800000
I0, R0 = 10, 0
S0 = N - I0 - R0
##beta, gamma = 0.0731, 0.03125
t = np.linspace(0, 100, 1000)


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)




axbeta = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='white')
axgamma = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='white')

Beta = Slider(axbeta, 'Beta', 0.0, 1.0, valstep=0.0001)
Gamma = Slider(axgamma, 'gamma', 0.0, 0.2, valstep=0.0001)

def plot(S, I, R):
        ax.cla()
        ax.plot(a,b,c, label='actual data_I')
##        ax.plot(c/N, label='actual data_R')
        ax.plot(t, I, 'r', label='Infected')
        ax.plot(t, R, 'g', label='Recovered with immunity')
        

def deriv(y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

def update(val):
        beta = Beta.val
        gamma = Gamma.val
        print("Beta=",beta,"  Gamma=", gamma)
        y0 = S0, I0, R0
        ret = odeint(deriv, y0, t, args=(N, beta, gamma))
        S, I, R = ret.T
        plot(S, I, R)


Beta.on_changed(update)
Gamma.on_changed(update)

plt.show()
