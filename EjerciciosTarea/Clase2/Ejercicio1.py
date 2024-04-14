#Problema 1
#En un experimento que consiste en lanzar 3 monedas legales, se define una variable aleatoria
#asignando 0 a una "cara" y 1 a una "cruz" y luego sumando los números. Determine y grafique
#mediante una simulación de Monte Carlo la función de distribución acumulativa.
import random
import matplotlib.pyplot as plt

def calcular_probabilidad(numero_simulaciones):
    cant_1 = 0  # 000
    cant_2 = 0  # 001, 010, 100
    cant_3 = 0  # 110, 101, 011
    cant_4 = 0  # 111

    for i in range(numero_simulaciones):
        moneda1 = random.randint(0, 1)
        moneda2 = random.randint(0, 1)
        moneda3 = random.randint(0, 1)

        suma = moneda1 + moneda2 + moneda3

        if suma == 0:   # Todas las monedas salieron en cara
            cant_1 += 1
        elif suma == 1: # Solo una moneda salió en cruz
            cant_2 += 1
        elif suma == 2: # Solo una moneda salió en cara
            cant_3 += 1
        else:
            cant_4 += 1  # Todas las monedas salieron en cruz  

    probUno = cant_1 / numero_simulaciones     # Probabilidad de 000 //ultimo valor
    probDos = cant_2 / numero_simulaciones     # Probabilidad de 001, 010, 100
    probTres = cant_3 / numero_simulaciones    # Probabilidad de 110, 101, 011
    probCuatro = cant_4 / numero_simulaciones  # Probabilidad de 111

    # Calcular la CDF acumulando las probabilidades
    # CDF: Función de Distribución de Probabilidad o Función de Masa de Probabilidad Acumulada 
    #Lista con las sumas de cada probabilidad
    cdf = [probUno, probUno + probDos, probUno + probDos + probTres, 1] #Prob de cero, 1,2,3 //vector

    # Crear el gráfico de la CDF Fucnion Probabilidad Acumulada
    etiquetas = ['Todas cara', 'Una en cruz', 'Una en cara', 'Todas cruz']
    plt.step(etiquetas, cdf, where='post')

    return (probUno, probDos, probTres, probCuatro)

num_simulaciones = int(input("Ingrese el número de simulaciones: "))

results = calcular_probabilidad(num_simulaciones)

print(f'La probabilidad de que salgan todos cara: {results[0]}')
print(f'La probabilidad de que salga solo uno cruz: {results[1]}')
print(f'La probabilidad de que salga solo uno cara: {results[2]}')
print(f'La probabilidad de que salgan todos cruz: {results[3]}')

plt.title('Función de distribución acumulativa (CDF) de tres monedas')
plt.ylabel('Probabilidad acumulada')
plt.xlabel('Suma de resultados')
plt.ylim(0, 1)  # Asegurar que el eje y esté en el rango [0, 1]

# Establecer ticks y etiquetas personalizadas en el eje y
plt.yticks([1/8, 4/8, 7/8, 1], ['1/8', '4/8', '7/8', '1'])
plt.grid()
plt.show()