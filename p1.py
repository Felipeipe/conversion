import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# from torque_calc import torque
# Constantes
omega = 314 # [rad/s]
delta = 0.0 # [rad]
A = 1.5 # [A]

def L_22(theta):
    return 0.5 + 0.2*np.cos(2*theta)

def dot_L_22(theta):
    return -0.4*omega*np.sin(2*theta)

def dL_22_dtheta(theta):
    return dot_L_22(theta)/omega

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
    a = -(1.5 * dot_L_12(theta(t)))
    c = -(I_2 * dot_L_22(theta(t)))
    return (a+c)/L_22(theta(t))

def torque(theta):
    delt = 1-np.cos(theta)
    den = np.cos(2*theta) + 2.5

    a = (2*delt*np.sin(theta)*L_22(theta)) 
    b = (delt**2 * dL_22_dtheta(theta))

    term1 = (a-b)*den**2
    c = delt**2 * L_22(theta) * 4 * (den)*np.sin(2*theta)
    sum1 = 8*A**2 * (term1 + c)/den**4
    d = (np.sin(theta)*np.cos(theta) - delt*np.sin(theta))*den
    e = delt*np.cos(theta)*np.sin(theta)*2
    sum2 = 3.2*A**2 * (d+e)/den**2
    sum3 = - A**2*0.35*np.sin(2*theta)
    return sum1 + sum2 + sum3

T = np.linspace(0,6*np.pi/omega,1000)
z = odeint(dot_rotor_current,0,T)
plt.plot(T,z,label='Corriente en rotor')
plt.xlabel('Tiempo [s]')
plt.ylabel('Corriente [A]')
plt.title('Corriente en rotor en función del tiempo')
plt.grid(True)
plt.show()

plt.plot(T, torque(omega*T), label = 'Torque en funcion del tiempo')
plt.xlabel('Tiempo [s]')
plt.ylabel('Torque [Nm]')
plt.title('Torque en funcion del tiempo')
plt.grid(True)
plt.show()