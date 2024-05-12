import numpy as np 
from scipy.special import erf

def Q_function(x):
	return 0.5 * (1 - erf(x/np.sqrt(2)))

# Método abreviado - Distintos valores de x de acuerdo al ejercicio
#x = (0.002 - 1)/np.sqrt(0.5)
x = 0.01
#x = np.sqrt(2*2.544)

q_value = Q_function(x)
print('Q({}) = {:.15f}'.format(x, q_value))