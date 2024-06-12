#Problema 
#Se define a la función de distribución acumulativa de una variable aleatoria X de la 
#siguiete manera: 
#Fx(X) = P(X<=x) con X una variable real
#Para el experimento del lanzamiento de un dado, X es la variable que identifica la cara del dado que salió. 
#Determine Fx(3,3)
import random
import matplotlib.pyplot as plt

def calcular_probabilidad(num_simulaciones):
    suma_menor_tres = 0

    for i in range(num_simulaciones):
        dado1=random.randint(1,6)   #Tiro el dado1

        total = dado1

        if total <= 3:
            suma_menor_tres += 1

    probabilidad_menor_tres = suma_menor_tres / num_simulaciones

    #Datos de la tirada
    etiquetas = ['Menor o igual a tres']
    datos = [suma_menor_tres]

    #Crear el histograma con etiquetas
    plt.bar(etiquetas,datos,color=['blue'])

    return [probabilidad_menor_tres]

def imprimir_lista(lista):
    print('La probabilidad de que salga un número menor a tres es:',lista[0])

num_simulaciones = int(input("Ingrese el número de simulaciones: "))
listaProbabilidad = calcular_probabilidad(num_simulaciones)
imprimir_lista(listaProbabilidad)

plt.title('Histograma de dos monedas')
plt.ylabel('Frecuencia')
plt.show()