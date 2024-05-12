import numpy as np

def waveformer(c):
    f = 1                               # Frecuencia
    T = 1/f                             # Periodo 
    delta = 0.1                         # Intervalo de muestreo            
    
    #Valores que toman las funciones trigonométricas
    samples = np.arange(0, T+delta, delta)* 2 * np.pi * f     # Muestreo
    
    # Bases
    phi_1 = np.sqrt(2/T) * np.cos(samples)    
    phi_2 = (np.sqrt(2/T) * np.sin(samples))

    #Cálculo de w_i
    w = c[0] * phi_1 + c[1] * phi_2
    return w

# Esto es parte del test - No va en la respuesta
c = [2,-2]
print(waveformer(c))