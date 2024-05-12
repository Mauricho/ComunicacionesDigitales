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

