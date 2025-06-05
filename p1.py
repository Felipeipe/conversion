import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constantes
omega = 314 # [rad/s]
delta = 0.1 # [rad]

def L_11(theta):
    return 0.75 + 0.35 * np.cos(2*theta)

def dot_L_11(theta):
    return -0.7*omega*np.sin(2*theta)

def L_22(theta):
    return 0.5 + 0.2*np.cos(2*theta)

def dot_L_22(theta):
    return -0.4*omega*np.sin(2*theta)

def L_12(theta):
    return 0.8*np.cos(theta)

def dot_L_12(theta):
    return -0.8*omega*np.sin(theta)

def theta(t):
    return omega * t + delta

def I_1(t):
    return np.sqrt(2)*np.sin(omega * t)

def dot_I_1(t):
    return omega*np.sqrt(2)*np.cos(omega*t)

def dot_rotor_current(I_2,t):
    a = -(I_1(t)*dot_L_12(theta(t)))
    b = -(dot_I_1(t)*L_12(theta(t)))
    c = -(I_2*dot_L_22(theta(t)))
    return (a+b+c)/L_22(theta(t))


T = np.linspace(0,6*np.pi/omega,1000)
z = odeint(dot_rotor_current,0,T)
plt.plot(T,z,label='Corriente en rotor')
plt.xlabel('')
plt.show()