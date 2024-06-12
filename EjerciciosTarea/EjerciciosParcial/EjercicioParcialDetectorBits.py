import numpy as np

# Hypothesis source : BIT 0, BIT 1
# p_0: probabilidad de que sea 0. Referencia de la probabilidad
# nb: 
def get_hypothesis(p_0,nb):   
    z = np.random.uniform(size = nb) # Se crea un vector con variables aleatorias tamaño nb
    out = [0 if z[i]<p_0 else 1 for i in range(len(z))]     # Se crea el vector que contiene 0 con la probabilidad indicada
    return out

# Output of instrument
def get_instrument(hypothesis, alfa0, alfa1):
    out = [np.random.exponential(1/alfa0) if hypothesis[i]<alfa0 else np.random.exponential(1/alfa1) for i in range(len(hypothesis))]
    return out


# Bit Detector
def detect(input, alpha0, alpha1, p_0):
       
       return [theta, out_hypothesis]


def simulador_pe(alpha0, alpha1, p_0, nb):  

  return pe