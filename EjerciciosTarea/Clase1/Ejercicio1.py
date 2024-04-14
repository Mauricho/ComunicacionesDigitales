#PROBLEMA 1
#Frecuencia de ocurrencia relativa
#¿Cúal es la probabilidad de que aparezca un entero par en el lanzamiento de un dado?
import random
import matplotlib.pyplot as plt

num_simulaciones = int(input("Ingrese el número de simulaciones: ")) #ingresa un n° y lo convierto en entero

#función para calcular la probabilidad
def calcular_probabilidad_par(num_simulaciones): 

    contador_pares = 0
    contador_impares = 0

    for i in range(num_simulaciones):
        dado = random.randint(1, 6)  #Tiro el dado
        if dado % 2 == 0:           #Si es par 
            contador_pares += 1         
        else:                       #Si es impar
            contador_impares +=1

    #probabilidad = resultados_favorables / resultados_posibles
    probabilidad_par = contador_pares / num_simulaciones 

    # Datos de la tirada de dados
    etiquetas = ['Impar', 'Par']
    datos = [contador_impares, contador_pares]

    # Crear el histograma con etiquetas
    plt.bar(etiquetas, datos, color=['blue', 'red'])

    return probabilidad_par

print(f'La probabilidad de que salga un número par en un dado es: {calcular_probabilidad_par(num_simulaciones)}')

# Agregar título
plt.title('Histograma de números pares e impares en el lanzamiento de un dado')
# Agregar etiqueta al eje y
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()