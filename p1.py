import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constantes
omega = 314 # [rad/s]
delta = 0.1 # [rad]

def stator_inductance(theta):
    return 0.75 + 0.35 * np.cos(2*theta)

def dot_stator_inductance(theta):
    return -0.7*np.sin(2*theta)

def rotor_inductance(theta):
    return 0.5 + 0.2*np.cos(2*theta)

def dot_rotor_inductance(theta):
    return -0.4*np.sin(2*theta)

def mutual_inductance(theta):
    return 0.8*np.cos(theta)

def dot_mutual_inductance(theta):
    return -0.8*np.sin(theta)

def theta(t):
    return omega * t + delta

def stator_current(t):
    return np.sqrt(2)*np.sin(omega * t)

def dot_stator_current(t):
    return omega*np.sqrt(2)*np.cos(omega*t)

def dot_rotor_current(rotor_current,t):
    a = -(stator_current(t)*dot_mutual_inductance(theta(t)))
    b = -(dot_stator_current(t)*mutual_inductance(theta(t)))
    c = -(rotor_current*dot_rotor_inductance(theta(t)))
    return (a+b+c)/rotor_inductance(theta(t))


T = np.linspace(0,100*np.pi/omega,1000)
z = odeint(dot_rotor_current,0,T)
plt.plot(T,z)
plt.show()