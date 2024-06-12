import numpy as np

# Recibe dos parámetros: Señal e intervalo de tiempo entre los elementos
def correlador(signal,T):
  t = np.arange(0,2+T,T)                 # Vector tiempo

  waveform = np.zeros(len(t))            # Vector forma de onda 

  # Generación de la forma de onda triángular
  for i in range(len(t)):
    if t[i] <= 1:
      waveform[i] = t[i]
    else:
      waveform[i] = 2 - t[i]
  
  # La correlación se calcula como:
  min_len = len(signal) if len(signal)<len(waveform) else len(waveform)
  corr = 0

  for i in range(min_len):
    corr +=  signal[i] * waveform[i]    

  return corr*T

# Esto es parte del test - No va en la respuesta 
# Prueba 1
r =[0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0. ]
print(round(correlador(r,0.1),2))

# Prueba 2
r =[0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0. ]
np.random.seed(1234)
r = r + np.random.normal(0,0.5,len(r))
print(round(correlador(r,0.1),2))