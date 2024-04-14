#PROBLEMA 2
#Frecuencia de ocurrencia relativa
#¿Cúal es la probabilidad de que aparezca un entero par en la suma del lanzamiento de dos dado?
import random
import matplotlib.pyplot as plt

def calcular_probabilidad_par(num_simulaciones):
    contador_pares = 0
    contador_impares = 0

    for i in range(num_simulaciones):
        dado1 = random.randint(1,6) #Tiro el dado 1
        dado2 = random.randint(1,6) #Tiro el dado 2
        
        suma = dado1 + dado2

        if suma % 2 == 0:           #Si es par
            contador_pares += 1
        else:                       #Si es impar
            contador_impares +=1

    probabilidad_par = contador_pares/num_simulaciones

    # Datos de la tirada de dados
    etiquetas = ['Impar', 'Par']
    datos = [contador_impares, contador_pares]

    # Crear el histograma con etiquetas
    plt.bar(etiquetas, datos, color=['blue', 'red'])
    
    return probabilidad_par

num_simulaciones = int(input("Ingrese el número de simulaciones: "))
print(f'La probabilidad de que salga un número par en la suma de dos dados es:{calcular_probabilidad_par(num_simulaciones)}')

# Agregar título
plt.title('Histograma suma de dos dados')
# Agregar etiqueta al eje y
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()

