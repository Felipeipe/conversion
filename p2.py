import numpy as np
import matplotlib.pyplot as plt

E_a = np.load('E_a.npy')
I_a = np.load('I_a.npy')
omega = np.load('omega.npy')
N_steps = len(E_a)
V_a = 600 # [V]
R = np.linspace(0,2,N_steps)
eta = 2*E_a/V_a
v = (65*60/(1000*2*np.pi))*omega
tau = 12 + 2.2*omega

plt.plot(R, I_a, color = 'red')
plt.title('Corriente de armadura en funcion de resistencia variable')
plt.xlabel(r'Resistencia [$\Omega$]')
plt.ylabel('Corriente de armadura [A]')
plt.grid(True)
plt.show()

plt.plot(R, tau, color = 'green')
plt.title('Torque efectivo en funcion de resistencia variable')
plt.xlabel(r'Resistencia [$\Omega$]')
plt.ylabel('Torque [Nm]')
plt.grid(True)
plt.show()

plt.plot(R, eta, color = 'blue')
plt.title('Eficiencia de los motores en funcion de resistencia variable')
plt.xlabel(r'Resistencia [$\Omega$]')
plt.ylabel('Eficiencia')
plt.grid(True)
plt.show()

plt.plot(R, v, color = 'orange')
plt.title('Velocidad del tren en funcion de resistencia variable')
plt.xlabel(r'Resistencia [$\Omega$]')
plt.ylabel('Velocidad del tren [km/h]')
plt.grid(True)
plt.show()
 