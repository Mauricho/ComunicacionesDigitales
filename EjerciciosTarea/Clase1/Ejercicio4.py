#PROBLEMA 4
#Considere el experimento de lanzar dos dados. 
#Los eventos son las sumas de los números de las caras superiores 
#¿Cuál es la probabilidad de que esta suma sea menor que cinco?
import random
import matplotlib.pyplot as plt

def calcular_probabilidad(num_simulaciones):
    suma_menor_cinco = 0
    suma_mayor_cinco = 0

    for i in range(num_simulaciones):
        dado1=random.randint(1,6)   #Tiro el dado1
        dado2=random.randint(1,6)   #Tiro el dado2

        total = dado1 + dado2

        if total < 5:
            suma_menor_cinco += 1
        else:
            suma_mayor_cinco += 1

    probabilidad_menor_cinco = suma_menor_cinco / num_simulaciones
    probabilidad_mayor_cinco = suma_mayor_cinco / num_simulaciones

    #Datos de la tirada
    etiquetas = ['Mayor o igual a cinco','Menor a cinco']
    datos = [suma_mayor_cinco,suma_menor_cinco]

    #Crear el histograma con etiquetas
    plt.bar(etiquetas,datos,color=['blue','red'])

    return [probabilidad_menor_cinco,probabilidad_mayor_cinco]

def imprimir_lista(lista):
    print('La probabilidad de que salga un número menor a cinco es:',lista[0])
    print('La probabilidad de que salga un número mayor a cinco es:',lista[1])

num_simulaciones = int(input("Ingrese el número de simulaciones: "))
listaProbabilidad = calcular_probabilidad(num_simulaciones)
imprimir_lista(listaProbabilidad)

plt.title('Histograma de dos monedas')
plt.ylabel('Frecuencia')
plt.show()











