#PROBLEMA 3
#Frecuencia de ocurrencia relativa
#Considérese el experimento de lanzar dos monedas legales 
#¿Cuál es la probabilidad de obtener dos caras o dos cruces?
import random
import matplotlib.pyplot as plt

def calcular_probabilidad_moneda(num_simulaciones):
    contador_igual = 0
    contador_dist = 0

    for i in range(num_simulaciones):
        moneda1=random.randint(1,2) #Tiro moneda 1: cara o cruz
        moneda2=random.randint(1,2) #Tiro moneda 2: cara o cruz

        if moneda1 == moneda2:
            contador_igual += 1
        else:
            contador_dist += 1    

    probabilida_igual = contador_igual / num_simulaciones

    #Datos de la tirada
    etiquetas = ['Igual','Distinto']
    datos=[contador_igual,contador_dist]

    #Crear el histograma con etiquetas
    plt.bar(etiquetas,datos, color=['blue','red'])

    return probabilida_igual

num_simulaciones = int(input("Ingrese el número de simulaciones: "))
print(f'La probabilidad de que salga cara o cruz en ambas monedas es:{calcular_probabilidad_moneda(num_simulaciones)}')        

#Agregar título
plt.title('Histograma de dos monedas')
plt.ylabel('Frecuencia')
plt.show()