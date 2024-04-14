#PROBLEMA 6
#Se lanzan varios dados. Calcule la probabilidad de que en todos
#aparezca un dos si el número de dados lanzados es 2.
import random
import matplotlib.pyplot as plt

def calcular_probabilidad(numero_simulaciones):
    cant_uno = 0                        #Evento A: en ambos dados sale 1
    cant_otro = 0                       #Evento B: sale cualquier otro valor
    cant_compartidos = 0

    for i in range(numero_simulaciones):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)

        suma = dado1 + dado2
        
        if suma == 2: #en los dos dados salio 1
            cant_uno += 1
            cant_compartidos += 1
        else:         #en los dados salio otro número que no suman 2 
            cant_otro += 1 

    probUno = cant_uno/numero_simulaciones                      #Evento A
    probOtro = cant_otro/numero_simulaciones                    #Evento B    
    probCompartido = cant_compartidos/numero_simulaciones       #Evento AB

    probBdadoA = probCompartido / probUno              #P(B|A)
    probAdadoB = probCompartido / probOtro             #P(A|B)  

    #Datos de la tirada
    etiquetas = ['Evento A','Evento B']
    datos = [cant_uno,cant_otro]

    #Crear el histograma con etiquetas
    plt.bar(etiquetas,datos,color=['blue','red'])

    return (probUno, probOtro, probCompartido, probAdadoB, probBdadoA)

num_simulaciones = int(input("Ingrese el número de simulaciones: "))

results = calcular_probabilidad(num_simulaciones)

print(f'La probabilidad de que salga dos: {results[0]}')
print(f'P(A) tiene que ser igual a P(A/B) para que sean sucesos independientes, en este caso P(A) = {results[0]} y P(A/B) = {results[3]}')
print(f'P(B) tiene que ser igual a P(B/A) para que sean sucesos independientes, en este caso P(B) = {results[1]} y P(B/A) = {results[4]}')

#Para ser sucesos independientes:
#Se debe obtener P(A|B)=P(A) y de manera analítica: 0.0277 == 0.0277
#Se debe obtener P(B|A)=P(B) y de manera analítica: 1 == 1 
#Entonces son sucesos independientes!

plt.title('Histograma de dos dados')
plt.ylabel('Frecuencia')
plt.show()