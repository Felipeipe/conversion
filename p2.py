import sympy as sym
import numpy as np

G = 0.05 # [H]
R_c = 0.4 # [Ohms]
R_a = 0.1 # [Ohms]
V_a = 600 # [V]

I_a, omega, E_a, R_s = sym.symbols('I_a, omega, E_a, R_s') 

expr = 2*G**2- 12 - 2.2*omega 