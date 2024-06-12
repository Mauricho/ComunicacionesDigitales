import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

# función = T/2 en [-1/T, 1/T]
T = 4
Nsamples = 1000
paso = 10/T/Nsamples
frecs = np.arange(-5/T,5/T,paso)
psi = np.array([T/2 if abs(f) < 1/T else 0 for f in frecs])

#hacemos el espectro plegado
plegado = np.zeros(psi.size)
psis = []
for i in range(-5,6):
    psi_desplazada = np.array([T/2 if abs(f-i/T) <= 1/T else 0 for f in frecs])
    psis.append(psi_desplazada)
    plegado += psi_desplazada

plt.figure()
plt.subplot(2,1,1)
plt.grid()
plt.plot(frecs,psi)
plt.ylim([-1,T+1])
plt.plot(frecs,plegado)
plt.plot(frecs,psis[6],'--')
plt.plot(frecs,psis[7],'--')
plt.legend([r'$|\phi|^2$',"espectro plegado"])

# El espectro plegado demuestra que la función es ortonormal a intervalos de T

# Función sinc^2(fT)
T = 4
Nsamples = 1000
paso = 10/T/Nsamples
frecs = np.arange(-5/T, 5/T, paso)
psi = np.sinc(frecs*T)**2

# Hacemos el espectro plegado
plegado = np.zeros(psi.size)
psis = []
for i in range(-40,40):
    psi_desplazada = np.sinc((frecs-i/T)*T)**2
    psis.append(psi_desplazada)
    plegado += psi_desplazada

plt.subplot(2,1,2)
plt.grid()
plt.plot(frecs,psi)
plt.ylim([-1,2])
plt.plot(frecs,plegado)
plt.plot(frecs,psis[41],'--')
plt.plot(frecs,psis[42],'--')
plt.show()
# El espectro plegado demuestra que la función es ortonormal a intervalos de T pero no tiene norma unitaria
