import numpy as np
from Calculator import N_steps, V_a
import matplotlib.pyplot as plt
R = np.linspace(0,2,N_steps)
E_a = np.load('E_a.npy')
I_a = np.load('I_a.npy')
omega = np.load('omega.npy')

# Aquí hay que graficar la corriente que circula por los motores
# La velocidad del tren en régimen permanente v = (65 / (1000*2*pi/60))*omega
# torque efectivo 12+2,2*omega
# eficiencia del conjunto de motores 2*E_a/V_a
# todo eso en funcion de R_s

eta = 2*E_a/V_a
v = (65*60/(1000*2*np.pi))*omega
tau = 12 + 2.2*omega

plt.plot(R, I_a)
plt.title('Corriente de armadura en funcion de resistencia variable')
plt.xlabel(r'Resistencia [$\Omega$]')
plt.ylabel('Corriente de armadura [A]')
plt.grid(True)
plt.show()

plt.plot(R, tau)
plt.title('Torque efectivo en funcion de resistencia variable')
plt.xlabel(r'Resistencia [$\Omega$]')
plt.ylabel('Torque [Nm]')
plt.grid(True)
plt.show()

plt.plot(R, eta)
plt.title('Eficiencia de los motores en funcion de resistencia variable')
plt.xlabel(r'Resistencia [$\Omega$]')
plt.ylabel('Eficiencia')
plt.grid(True)
plt.show()

plt.plot(R, v)
plt.title('Velocidad del tren en funcion de resistencia variable')
plt.xlabel(r'Resistencia [$\Omega$]')
plt.ylabel('Velocidad del tren [km/h]')
plt.grid(True)
plt.show()
 