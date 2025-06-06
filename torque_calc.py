import sympy as sym

# Variables simbólicas
t, omega= sym.symbols('t, omega')
I_1 = 1.5

# Función dependiente del tiempo
I_2 = sym.Function('I_2')(t)

# Definimos theta y las inductancias
theta = omega * t
L_12 = 0.8 * sym.cos(theta)
L_22 = 0.5 + 0.2 * sym.cos(2 * theta)

# Derivadas necesarias
dI2_dt = sym.diff(I_2, t)
dL12_dt = sym.diff(L_12, t)
dL22_dt = sym.diff(L_22, t)

# Ecuación diferencial
eq = sym.Eq(dI2_dt * L_22 + I_1 * dL12_dt + I_2 * dL22_dt, 0)
print("Se resolverá la ecuación ahora?")
# Resolver la ecuación
sol = sym.dsolve(eq, I_2)
sol_with_omega = sol.subs(omega,314)
# Mostrar solución
sym.pprint(sol)
