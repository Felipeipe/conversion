import sympy as sym
import numpy as np
G = 0.05 # [H]
R_c = 0.4 # [Ohms]
R_a = 0.1 # [Ohms]
V_a = 600 # [V]
N = 10 # Number of plotted points
R = np.linspace(0,2,N)
armor_current = np.zeros(N)
internal_tension = np.zeros(N)
motor_angular_vel = np.zeros(N)

I_a, omega, E_a = sym.symbols('I_a, omega, E_a') 

expr_1 = 2* G *I_a**2 - 12 - 2.2*omega 
expr_2 = G*omega*I_a - E_a

for i,R_s_np in enumerate(R):
    R_s = float(R_s_np)
    expr_3 = I_a*(R_s + 2*R_c + 2*R_a) + 2*E_a - V_a
    sols = sym.solve([expr_1, expr_2, expr_3], I_a, omega, E_a, dict = True)[0]
    armor_current[i], internal_tension[i], motor_angular_vel[i] = sols[I_a], sols[E_a], sols[omega]
print('Listo! Guardando valores :)') 
np.save('I_a.npy', armor_current)
np.save('E_a.npy', internal_tension)
np.save('omega.npy', motor_angular_vel)