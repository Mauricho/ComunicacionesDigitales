#incluir librerías necesarias  
import numpy as np
from scipy.special import erf

kb=1.381e-23 #Constante de Boltzmann

def BER(pt,lda,gt,gr,d,tn,rb):
    """
    El problema nos dice que la distancia esta en Kilómetros y 
    los bit rate en kilo bits por segundo. Por eso lo multiplicamos por 1000.
    """
    tau = 1/(rb*1000)                    # Duración de la señal                      
    ls = ((4*np.pi*d*1000)/(lda))**2         # Free Space Path Loss

    # Relación energía por bit / Potencia ruido
    x = (pt*tau*gt*gr)/(ls*kb*tn)

    # The error rate for antipodal signaling is
    bit_error_rate = Q_function(np.sqrt(2*x))

    return bit_error_rate

def Q_function(x):
	return 0.5 * (1 - erf(x/np.sqrt(2)))

# Esto es parte del test - No va en la respuesta
print(BER(16.8 ,0.13,575.44 ,1.38e6 ,1.6e8,13.5 ,117.6))