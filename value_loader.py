import numpy as np

E_a = np.load('E_a.npy')
I_a = np.load('I_a.npy')
omega = np.load('omega.npy')

print(f'{omega[9] = }, {E_a[9] = }, {I_a[9] = }')